from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
  # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  name = models.CharField("タスク名", max_length=200)
  duration = models.IntegerField("所要時間")
  sharing_rate = models.IntegerField("分担率")
  wage = models.IntegerField("賃金換算")

  def __str__(self):
    return self.name