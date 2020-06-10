import os

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True, is_admin=False):
        if not email:
            raise ValueError("User must have an email address")

        if not password:
            raise ValueError("User must have an password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        # user.is_superuser = is_superuser
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        user.is_superuser = True
        user.save(using=self._db)
        # user.is_superuser = True
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in thr system"""
    first_name = models.CharField('First Name', max_length=20, null=True, blank=True)
    last_name = models.CharField('Last Name', max_length=20, null=True, blank=True)
    email = models.EmailField('Email ID', max_length=255, unique=True)
    contact = models.CharField('Contact Number', max_length=10, null=True, blank=True)
    address1 = models.CharField('Address Line 1', max_length=255, null=True, blank=True)
    address2 = models.CharField('Address Line 2', max_length=255, null=True, blank=True)
    postal_code = models.CharField('Pin code', max_length=10, null=True, blank=True)
    city = models.CharField('City', max_length=100, null=True, blank=True)
    state = models.CharField('State', max_length=100, null=True, blank=True)

    timestamp = models.DateTimeField('Registered Date', auto_now_add=True)
    password = models.CharField(max_length=255)
    active = models.BooleanField('Active User', default=False)
    staff = models.BooleanField('Staff User', default=False)
    admin = models.BooleanField('Superuser', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin


class Nursery(models.Model):
    name = models.CharField('Name', max_length=100)
    address = models.TextField(verbose_name='Address')
    contact = models.CharField(max_length=10, verbose_name='Contact Number')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.CASCADE,
                                verbose_name=u'User ID')
    opening_time = models.TimeField('Opening Time')
    closing_time = models.TimeField('Closing Time')

    class Meta:
        verbose_name = "Nursery"
        verbose_name_plural = "Nurseries"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Category name', max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


def upload_img_to(instance, filename):
    print(instance, filename)
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    final_filename = f'{instance.name}{ext}'
    return f'{instance.nursery.name}/{final_filename}'


class Plants(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    category = models.ForeignKey('Category', to_field='id', on_delete=models.DO_NOTHING, verbose_name='Category')
    nursery = models.ForeignKey('Nursery', to_field='id', on_delete=models.CASCADE, verbose_name='Nursery')
    image = models.ImageField(upload_to=upload_img_to, verbose_name="Plant Image")

    class Meta:
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

    def __str__(self):
        return self.name + "(" + str(self.nursery) + ")"


class Orders(models.Model):
    STATUS = (
        (0, 'In Cart'),
        (1, 'Order Placed')
    )

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.CASCADE, verbose_name='User')
    plant_id = models.ForeignKey(Plants, to_field='id', on_delete=models.CASCADE, verbose_name='Plant')
    quantity = models.IntegerField(default=1, verbose_name='Quantity')
    checkout_date = models.DateField(verbose_name='Checkout Date')
    status = models.IntegerField(choices=STATUS, verbose_name='Status of order')

    class Meta:
        verbose_name = "Orders"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.user_id) + "_" + str(self.plant_id) + "_" + str(self.quantity)
