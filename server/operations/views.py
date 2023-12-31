from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OperationSerializer
from .models import Operation


class OperationListCreateView(ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

operation_list_create = OperationListCreateView.as_view()
operation_retrieve_update_destroy = CustomerRetrieveUpdateDestroyAPIView.as_view()