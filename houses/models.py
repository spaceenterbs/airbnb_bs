from django.db import models

# Create your models here.
class House(models.Model): # models와 Model 모두를 상속받는 것
    
    """Model Definition for Houses"""
    
    name = models.CharField(max_length=140) # CharField 어느 정도 길지만 길이 제한이 있는 텍스트
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)