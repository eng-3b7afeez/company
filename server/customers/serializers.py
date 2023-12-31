from rest_framework.serializers import ModelSerializer
from .models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name", "mobile", "mobile2", "company", "rating", "comment"]


class MyCustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name"]
