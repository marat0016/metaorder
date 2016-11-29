from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from worker.models import Operator
from metaord.models import Order # todo .


def has_model_permissions(entity, model, perms, app):
    for p in perms:
        if not entity.has_perm("%s.%s_%s" % (app, p, model.__name__ )):
            return False
        return True


class Groups:
    @staticmethod
    def get_or_create_operator():
        group, created = Group.objects.get_or_create(name='operator')
        if created:
            group.permissions.add(Permissions.change_order_status())
            # logger.info('operator_user Group created')
        return group

    @staticmethod
    def get_or_create_boss():
        group, created = Group.objects.get_or_create(name='boss')
        if created:
            group.permissions.add(Permissions.delete_orders(), Permissions.delete_operators())
            # logger.info('boss Group created')
        return group
        

class Permissions:
    @staticmethod
    def change_order_status():
        perm = Permission.objects.filter(codename='change_order_status').first()
        if perm is not None:
            return perm
        else:
            content_type = ContentType.objects.get_for_model(Order)
            return Permission.objects.create(codename='change_order_status', # mb ADD worker
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