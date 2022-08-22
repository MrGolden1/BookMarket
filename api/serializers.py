from asyncore import write
from rest_framework import serializers
from .models import Book, CustomUser,Item,Cart

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'pages', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'is_staff', 'is_active', 'date_joined', 'role','password')
        read_only_fields = ('date_joined',)
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'book', 'quantity', 'total_price', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'total_price')
    def create(self, validated_data):
        item = super().create(validated_data)
        item.set_total_price()
        return item
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'items', 'total_price', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'total_price')
    def create(self, validated_data):
        items = validated_data.pop('items')
        cart = Cart(**validated_data)
        for item in items:
            cart.items.add(Item.objects.get(id=item['id']))
        cart.set_total_price()
        cart.save()