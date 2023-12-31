from rest_framework.serializers import ModelSerializer
from .models import Operation
from customers.serializers import MyCustomerSerializer
from core.serializers import MyUserSerializer


class OperationSerializer(ModelSerializer):
    #customer = MyCustomerSerializer()
    #user = MyUserSerializer()

    class Meta:
        model = Operation
        fields = "__all__"
