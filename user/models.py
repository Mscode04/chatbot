from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feedbacks(models.Model):
    feedback=models.CharField(max_length=300)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)