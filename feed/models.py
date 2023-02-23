from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    text=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )


    def __str__(self) -> str:
        return self.text[0:100]

