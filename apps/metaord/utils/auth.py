from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from worker.models import Operator
from metaord.models import Order


class Groups:
    @staticmethod 
    def is_user_chief(user):
        return user.groups.filter(name='chief').exists()

    @staticmethod
    def get_or_create_worker():
        group, created = Group.objects.get_or_create(name='worker')
        if created:
            group.permissions.add(Permissions.change_order_status())
            # logger.info('operator_user Group created')
        return group

    @staticmethod
    def get_or_create_chief():
        group, created = Group.objects.get_or_create(name='chief')
        if created:
            group.permissions.add(Permissions.delete_orders(), Permissions.delete_operators())
            # logger.info('chief Group created')
        return group
        

class Permissions:
    @staticmethod
    def change_order_status():
        perm = Permission.objects.filter(codename='change_order_status').first()
        if perm is not None:
            return perm
        else:
            content_type = ContentType.objects.get_for_model(Order)
            return Permission.objects.create(codename='change_order_status',
                                            name='Can change order status',
                                            content_type=content_type)

    @staticmethod
    def delete_orders():
        content_type = ContentType.objects.get_for_model(Order)
        return Permission.objects.create(codename='delete_orders',
                                       name='delete_orders',
                                       content_type=content_type)

    @staticmethod
    def delete_operators():
        content_type = ContentType.objects.get_for_model(Operator)
        return Permission.objects.create(codename='delete_operators',
                                       name='delete_operators',
                                       content_type=content_type)