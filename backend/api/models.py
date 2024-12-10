from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required.")
        email = self.normalize_email(email)
        extra_fields.setdefault('admin', 0)  # Par défaut, non administrateur
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('admin', 1)  # Superuser est administrateur
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cine = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    id_card = models.FileField(upload_to='id_cards/')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    admin = models.IntegerField(default=0)  # 0 pour utilisateur normal, 1 pour admin

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    account_type = models.CharField(max_length=50, choices=[("Courant", "Courant"), ("Épargne", "Épargne")])

    def __str__(self):
        return f"{self.user.full_name} - {self.account_number}"

class Transaction(models.Model):
    sender = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="sent_transactions")
    receiver = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="received_transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Transaction from {self.sender.account_number} to {self.receiver.account_number}"
        
class OnlinePayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    merchant = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.user.full_name} to {self.merchant}"
