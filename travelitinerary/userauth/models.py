from django.db import models

class Home(models.Model):  # ✅ Use PascalCase
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122) 
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name  # ✅ Helps in debugging (shows name in Django Admin)
