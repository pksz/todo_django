from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    date_of_creation=models.DateTimeField(auto_now_add=True)
    date_of_expiry=models.DateField()

    def __str__(self) -> str:
        return self.title
    
        class Meta:
            ordering=['date_of_creation']