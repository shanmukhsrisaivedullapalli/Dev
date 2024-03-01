from django.db import models

# Create your models here.
class Contactform(models.Model):
    email=models.EmailField()
    message=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.email +' | '+ self.message[:10] + '...'