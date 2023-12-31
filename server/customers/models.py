from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    mobile = models.CharField(max_length=15)
    mobile2 = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(default=6)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("name", "mobile")
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["mobile"]),
            models.Index(fields=["mobile2"]),
            models.Index(fields=["company"]),
        ]

    def __str__(self):
        return self.name
