from django.db import models


class Book(models.Model):
    b_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    price=models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.b_name


