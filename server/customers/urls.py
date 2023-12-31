from django.urls import path
from . import views

urlpatterns = [
    path("", views.customer_list_create),
    path("<int:pk>/", views.customer_retrieve_update_destroy),
]
