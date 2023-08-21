import factory
from accounts.models import Account, UserProfile, MyAccountManager
from django.contrib.auth.hashers import make_password
from phonenumber_field.phonenumber import PhoneNumber
from faker import Faker
import pytest

fake = Faker()


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("user_name")
    email = factory.Faker("email@email.com")
    password = make_password("password")
    phone_number = PhoneNumber.from_string("010-1234-5678", region="KR")

    is_admin = False
    is_staff = False
    is_active = True
    is_superadmin = False


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile
    user = factory.SubFactory(AccountFactory)
    address_line_1 = factory.Faker('address_line_1')
    address_line_2 = factory.Faker('address_line_2')
    profile_picture = factory.django.ImageField(filename="example.jpg")
    city = factory.Faker("city")
    state = factory.Faker("state_abbr")
    country = factory.Faker("country_code")



