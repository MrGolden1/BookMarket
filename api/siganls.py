from .models import Item,Cart,Book
from django.db.models.signals import post_save, post_delete,pre_save
from django.dispatch import receiver


@receiver(post_save, sender=Item)
def create_total_price(sender, instance, created, **kwargs):
    print('salam')
    instance.cart.set_total_price()
@receiver(pre_save, sender=Item)
def update_total_price(sender, instance, **kwargs):
    instance.unit_price = instance.book.price
    instance.total_price = instance.quantity * instance.book.price

@receiver(post_delete, sender=Item)
def delete_total_price(sender, instance, **kwargs):
    instance.cart.set_total_price()
