from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    token = models.fields.CharField('Token', max_length=256)
    username = models.CharField(_('username'), max_length=100, default='', unique=True)
    email = models.EmailField(_('email_address'), max_length=80, unique=True)
    first_name = models.CharField(_('first_name'), max_length=100, default='', blank=False)
    last_name = models.CharField(_('surname'), max_length=100, default='', blank=False)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'
        )
    )
    is_staff = models.BooleanField(
        _('staff_status'),
        default=False,
        help_text='Designates whether the user can log into this admin site.'
    )
    is_superuser = models.BooleanField(
        _('super_user'),
        default=False,
    )
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'last_name', 'first_name',)