from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer


class Operation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    material = models.CharField(
        choices=(
            ("ST", "steel"),
            ("SUS", "stainless"),
            ("AL", "aluminium"),
            ("BR", "brass"),
        ),
        max_length=50,
    )
    material_from_storage = models.BooleanField(default=True)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    thickness = models.DecimalField(max_digits=10, decimal_places=2)
    work_duration = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    laser_cut = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True, editable=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Operation"
        verbose_name_plural = "Operations"
        ordering = ["-updated", "created"]

    def __str__(self):
        return f"{self.user} - {self.customer}"

    def weight(self):
        return round(self.height * self.width * self.thickness * 8, 2)
