from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.exceptions import ValidationError
import logging
from datetime import datetime
import re  # Add this import at the top


User = get_user_model()
logger = logging.getLogger(__name__)

# Utility function for email validation
def is_valid_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

# Utility function for password validation
def is_valid_password(password):
    import re
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Sign Up View
class SignUpView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        try:
            # Extract data from request
            full_name = request.data.get('full_name')
            email = request.data.get('email')
            cine = request.data.get('cine')
            date_of_birth = request.data.get('date_of_birth')
            place_of_birth = request.data.get('place_of_birth')
            id_card = request.FILES.get('id_card')  # File uploads
            password = request.data.get('password')

            # Validate required fields
            if not all([full_name, email, cine, date_of_birth, place_of_birth, id_card, password]):
                return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate full name (no digits allowed)
            if not re.match(r"^[a-zA-Z\s]+$", full_name):
                return Response({'error': 'Full name should only contain letters and spaces.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate email
            if not re.match(r'\S+@\S+\.\S+', email):
                return Response({'error': 'Invalid email format.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate CINE format
            if not re.match(r'^[A-Z]{2}[0-9]{5,6}$', cine):
                return Response({'error': 'CINE must start with two uppercase letters followed by 5-6 digits.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate date of birth format
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_of_birth):
                return Response({'error': 'Date of Birth must be in YYYY-MM-DD format.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate file size and type
            if id_card.size > 2 * 1024 * 1024:  # File size limit of 2MB
                return Response({'error': 'File size exceeds 2MB.'}, status=status.HTTP_400_BAD_REQUEST)
            if not id_card.name.endswith(('.jpg', '.jpeg', '.png', '.pdf')):
                return Response({'error': 'Only JPG, PNG, and PDF file formats are allowed.'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if email already exists
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create new user
            user = User.objects.create_user(
                full_name=full_name,
                email=email,
                password=password,
                cine=cine,
                date_of_birth=date_of_birth,
                place_of_birth=place_of_birth
            )
            # Save the ID card to the user
            user.id_card.save(id_card.name, id_card)
            user.save()

            return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            logger.error(f'Validation error: {str(e)}')
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Unexpected error: {str(e)}')
            return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignInView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Validate required fields
        if not email or not password:
            return Response({'error': 'Both email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        user = authenticate(username=email, password=password)

        if user is None:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate or retrieve token
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'message': 'Sign in successful.'
        }, status=status.HTTP_200_OK)


class ValidateTokenView(APIView):
    """
    An additional endpoint to validate a token.
    """
    def post(self, request):
        token_key = request.data.get('token')

        if not token_key:
            return Response({'error': 'Token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = Token.objects.get(key=token_key)
            return Response({'message': 'Token is valid.', 'user_id': token.user_id}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)