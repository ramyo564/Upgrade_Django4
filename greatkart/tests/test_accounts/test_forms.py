from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from accounts.forms import RegistrationForm, UserForm, UserProfileForm


class FormsTestCase(TestCase):
    def setUp(self):
        # Create test data or other setup if needed
        pass

    def test_registration_form_password_match(self):
        form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "010-1234-5678",
            "email": "john@example.com",
            "password": "securepassword",
            "confirm_password": "securepassword",
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_password_mismatch(self):
        form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "010-1234-5678",
            "email": "john@example.com",
            "password": "securepassword",
            "confirm_password": "differentpassword",
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Password does not match!", form.errors["__all__"])

    def test_user_form(self):
        form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "010-1234-5678",
        }
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_profile_form(self):
        form_data = {
            "address_line_1": "123 Main St",
            "address_line_2": "Apt 4B",
            "city": "New York",
            "state": "NY",
            "country": "USA",
        }
        uploaded_file = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
        form = UserProfileForm(data=form_data, files={"profile_picture": uploaded_file})

        self.assertFalse(form.is_valid())  # Check if form is invalid

        # Print errors for debugging
        if form.errors:
            print(form.errors)
