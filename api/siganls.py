from .models import Item,Cart,Book
from django.db.models.signals import post_save, post_delete,pre_save
from django.dispatch import receiver


@receiver(post_save, sender=Item)
def create_total_price(sender, instance, created, **kwargs):
    instance.cart.set_total_price()
@receiver(pre_save, sender=Item)
def update_total_price(sender, instance, **kwargs):
    instance.unit_price = instance.book.price
    instance.total_price = instance.quantity * instance.book.price

@receiver(post_delete, sender=Item)
def delete_total_price(sender, instance, **kwargs):
    instance.cart.set_total_price()
@receiver(post_save, sender=Book)
def create_total_price(sender, instance, created, **kwargs):
    if not created:
        items = Item.objects.filter(book=instance)
        for item in items:
            item.unit_price = instance.price
            item.total_price = item.quantity * instance.price
            item.save()