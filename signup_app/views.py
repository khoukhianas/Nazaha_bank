from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class DashboardStats(APIView):
    def get(self, request):
        total_users = User.objects.count()
        data = {
            "users": total_users,
            "accounts": 950,  # Remplacez par la logique réelle
            "revenue": 50000,  # Remplacez par la logique réelle
            "transactions": 3000,  # Remplacez par la logique réelle
        }
        return Response(data)
