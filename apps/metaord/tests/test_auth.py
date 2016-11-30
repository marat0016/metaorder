from django.test import TestCase
from metaord.utils.auth import *


class AuthTestCase(TestCase):
    user = None

    def setUp(self):
        self.user = User.objects.create_user(username='u', email='a@b.ru')
        self.user.groups.add(Groups.get_or_create_operator())

    def test_operatorGroupCreated(self):
        self.assertTrue(self.user is not None)

    def test_operatorGroupPermissions(self):
        has_perm = self.user.has_perm('metaord.change_order_status')
        self.assertTrue(has_perm)
