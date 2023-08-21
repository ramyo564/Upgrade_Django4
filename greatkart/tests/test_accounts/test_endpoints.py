# import pytest
# from django.test import TestCase
# from accounts.models import Account
# from ..factories import AccountFactory
# pytestmark = pytest.mark.django_db


# class TestAccountModel(TestCase):
#     def test_create_user(self):
#         account = AccountFactory()
#         db_account = Account.objects.get(id=account.id)

#         self.assertEqual(account.first_name, db_account.first_name)
#         self.assertEqual(account.last_name, db_account.last_name)
#         self.assertEqual(account.username, db_account.username)
#         self.assertEqual(account.email, db_account.email)
#         self.assertEqual(account.phone_number, db_account.phone_number)
#         self.assertEqual(account.is_admin, db_account.is_admin)
#         self.assertEqual(account.is_staff, db_account.is_staff)
#         self.assertEqual(account.is_active, db_account.is_active)
#         self.assertEqual(account.is_superadmin, db_account.is_superadmin)