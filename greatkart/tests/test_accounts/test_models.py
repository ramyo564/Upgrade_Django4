# import pytest
# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from accounts.models import MyAccountManager
# from django.utils.html import format_html
# from accounts.admin import UserProfileAdmin
# from accounts.models import UserProfile
# User = get_user_model()

# pytestmark = pytest.mark.django_db


# class TestMyAccountManager(TestCase):
#     def test_create_user_without_email(self):
#         manager = MyAccountManager()
#         with self.assertRaises(ValueError) as context:
#             manager.create_user(
#                 first_name="John",
#                 last_name="Doe",
#                 username="johndoe",
#                 email=None,  # Passing None to trigger the validation error
#                 password="testpassword"
#             )

#         self.assertEqual(
#             str(context.exception),
#             "User must have an email address"
#         )

#     def test_create_user_without_username(self):
#         manager = MyAccountManager()
#         with self.assertRaises(ValueError) as context:
#             manager.create_user(
#                 first_name="John",
#                 last_name="Doe",
#                 username=None,  # Passing None to trigger the validation error
#                 email="johndoe@example.com",
#                 password="testpassword"
#             )

#         self.assertEqual(
#             str(context.exception),
#             "User must have an username"
#         )

#     def test_create_user(self):
#         manager = User.objects
#         user = manager.create_user(
#             first_name="John",
#             last_name="Doe",
#             username="johndoe",
#             email="johndoe@example.com",
#             password="testpassword"
#         )

#         self.assertEqual(user.first_name, "John")
#         self.assertEqual(user.last_name, "Doe")
#         self.assertEqual(user.username, "johndoe")
#         self.assertEqual(user.email, "johndoe@example.com")
#         self.assertFalse(user.is_admin)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_active)
#         self.assertFalse(user.is_superadmin)

#     def test_create_superuser(self):
#         manager = User.objects
#         user = manager.create_superuser(
#             first_name="Admin",
#             last_name="User",
#             username="adminuser",
#             email="adminuser@example.com",
#             password="testpassword"
#         )

#         self.assertEqual(user.first_name, "Admin")
#         self.assertEqual(user.last_name, "User")
#         self.assertEqual(user.username, "adminuser")
#         self.assertEqual(user.email, "adminuser@example.com")
#         self.assertTrue(user.is_admin)
#         self.assertTrue(user.is_staff)
#         self.assertTrue(user.is_active)
#         self.assertTrue(user.is_superadmin)


# class TestAccountModel:
#     def test_create_user(self, account_factory):
#         create_user = account_factory(
#             first_name="first_name",
#             last_name="last_name",
#             username="username",
#             email="email@email.com",
#             password="password",
#             phone_number="010-1111-1111",
#             is_admin=False,
#             is_staff=False,
#             is_active=True,
#             is_superadmin=False,
#         )

#         assert create_user.full_name() == "first_name last_name"
#         assert create_user.__str__() == "email@email.com"
#         assert create_user.has_perm("some_permission") == False
#         assert create_user.has_module_perms("some_module") == True


# class TestUserProfile:
#     def test_user_profile(self, user_profile_factory, account_factory):
#         user = account_factory(
#             first_name="first_name",
#             last_name="last_name",
#             username="username",
#             email="email@email.com",
#             password="password",
#             phone_number="010-1111-1111",
#             is_admin=False,
#             is_staff=False,
#             is_active=True,
#             is_superadmin=False,
#         )
#         obj = user_profile_factory(
#             user=user,
#             address_line_1="address_line_1",
#             address_line_2="address_line_2",
#             profile_picture="123.jpg",
#             city="city",
#             state="state",
#             country="1234"
#         )
#         assert obj.__str__() == "first_name"
#         assert obj.full_address() == "address_line_1 address_line_2"


# class TestUserProfileAdmin(TestCase):
#     def test_thumbnail_method(self):
#         admin = UserProfileAdmin(model=UserProfile, admin_site=None)
#         user_profile = UserProfile(profile_picture="example.jpg")

#         thumbnail_html = admin.thumbnail(user_profile)
#         expected_html = format_html(
#             '<img src="{}" width="30" style="border-radius:50%;">'.format(
#                 user_profile.profile_picture.url
#             )
#         )

#         self.assertEqual(thumbnail_html, expected_html)
