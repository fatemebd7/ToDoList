from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey( User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Task (models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)   
    Category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField( null=True , blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True , blank=True)
    priority=models.CharField(max_length=10 , choices=[
        ("low" , "Low"),
        ("medium" , "Medium"),
        ("high" , "High"),
    ] , default="medium")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title