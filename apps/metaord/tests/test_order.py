from django.test import TestCase
from django.db.utils import IntegrityError
from metaord.models import Order

class OrderTestCase(TestCase):
    author1 = 'lion'
    email1 = 'lion@qwevhj.ru'

    def setUp(self):
        Order.objects.create(author=self.author1, email=self.email1)

    def test_canCreateOrder(self):
        has_order = Order.objects.filter(author=self.author1).exists()
        self.assertEqual(has_order, True)

    def test_canFetchOrder(self):
        order = Order.objects.get(author=self.author1)
        same_order = Order.objects.get(email=self.email1)
        self.assertEqual(order.email, self.email1)
        self.assertEqual(same_order.author, self.author1)

    def test_cannotCreateWithoutRequired_email(self):
        self.assertRaises(IntegrityError, Order.objects.create, email=None)

    def test_cannotCreateWithoutRequired_author(self):
        self.assertRaises(IntegrityError, Order.objects.create, author=None)
