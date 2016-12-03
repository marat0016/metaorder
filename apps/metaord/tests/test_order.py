from django.test import TestCase
from django.db.utils import IntegrityError
from metaord.models import Order

class OrderTestCase(TestCase):
    author1 = 'lion'
    email1 = 'lion@qwevhj.ru'
    status = 1

    def setUp(self):
        Order.objects.create(author=self.author1, email=self.email1, status=self.status)

    def test_canCreateOrder(self):
        has_order = Order.objects.filter(author=self.author1).exists()
        self.assertEqual(has_order, True)

    def test_canFetchOrder(self):
        order = Order.objects.get(author=self.author1)
        same_order = Order.objects.get(email=self.email1)
        the_same_order = Order.objects.get(status=self.status)
        self.assertEqual(self.email1, order.email)
        self.assertEqual(self.author1, same_order.author)
        self.assertEqual(self.status, the_same_order.status)

    def test_cannotCreateWithoutRequired_email(self):
        self.assertRaises(IntegrityError, Order.objects.create, email=None)

    def test_cannotCreateWithoutRequired_author(self):
        self.assertRaises(IntegrityError, Order.objects.create, author=None)
