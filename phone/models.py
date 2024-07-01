from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    DisplayFields = ['name','phone']
    SearchableFields = ['name','phone']

    def __str__ (self):
        full = f"{self.name}"
        return full
    
class Phone(models.Model):
    post = models.ForeignKey(Info, on_delete=models.SET_NULL, null=True, related_name='dec')
    phone = models.CharField(max_length=500)