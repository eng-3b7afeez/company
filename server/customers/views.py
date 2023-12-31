from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Customer
from .serializers import CustomerSerializer


class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


customer_list_create = CustomerListCreateView.as_view()
customer_retrieve_update_destroy = CustomerRetrieveUpdateDestroyAPIView.as_view()
