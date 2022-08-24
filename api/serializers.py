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
        fields = ('id', 'book', 'quantity', 'total_price', 'created_at', 'updated_at','unit_price','cart')
        read_only_fields = ('created_at', 'updated_at', 'total_price')

class CartSerializer(serializers.ModelSerializer):
    useremail = serializers.CharField(source='user.email')
    class Meta:
        model = Cart
        fields = ('id', 'useremail','total_price', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'total_price')
    def is_valid(self, raise_exception = True):
        useremail =  self.initial_data['useremail']
        if CustomUser.objects.filter(email = useremail).exists():
            return True
        return False
    def create(self, validated_data):
            user = CustomUser.objects.get(email = validated_data.get('usermail'))
            cart = Cart(user = user)
            cart.save()
            return cart
