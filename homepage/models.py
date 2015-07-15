from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
	# Inherited from AbstractUser and AbstractBaseUser
	# password
	# last_login
	# first_name
	# last_name
	# email
	# is_staff
	# help_text
	# is_active
	# date_joined
	securtiy_question = models.TextField(max_length=150, null=True, blank=True)
	creation_date = models.DateField(null=True, blank=True)
	address1 = models.TextField(max_length=30, null=True, blank=True)
	address2 = models.TextField(max_length=30, null=True, blank=True)
	city = models.TextField(max_length=30, null=True, blank=True)
	state = models.TextField(max_length=30, null=True, blank=True)
	country = models.TextField(max_length=30, null=True, blank=True)
	zip = models.TextField(max_length=30, null=True, blank=True)
	# #family_name = models.TextField(max_length=30, null=True, blank=True)
	pass

class Account(models.Model):
	user = models.ForeignKey(Users, null=True)
	account_name = models.TextField(max_length=75, null=True, blank=True)
	amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	acc_type = models.TextField(max_length=75)

class Transaction(models.Model):
	User = models.ForeignKey(Users, null=True)
	date = models.DateField(null=True, blank=True)
	description = models.TextField(max_length=75, null=True, blank=True)
	original_description = models.TextField(max_length=75, null=True, blank=True)
	amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	transaction_type = models.TextField(max_length=75, null=True, blank=True)
	category = models.TextField(max_length=75, null=True, blank=True)
	account = models.ForeignKey(Account, null=True)
	account_name = models.TextField(max_length=75, null=True, blank=True)

class DebCred(models.Model):
	date = models.TextField(max_length=75, null=True, blank=True)
	cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	tran_type = models.TextField(max_length=75, null=True, blank=True)
	year = models.TextField(max_length=75, null=True, blank=True)
	month = models.TextField(max_length=75, null=True, blank=True)


