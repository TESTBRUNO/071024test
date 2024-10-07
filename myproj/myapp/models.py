from django.db import models

# Create your models here.

class books(models.Model):
   author = models.CharField(max_length = 100)
   name = models.CharField(max_length = 100)
   description = models.CharField(max_length = 2000)
   size = models.IntegerField()
   img = models.ImageField(upload_to="myapp/static/img", blank=True)




class Animal(models.Model):
   name = models.CharField(max_length = 100)
   sound = models.CharField(max_length = 100)

   def speak(self):
      return  10+20 #f'The {self.name} says "{self.sound}"'
   

#python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# from myapp.models import books
#new = books(author = " Лев Толстой", name = "Война и мир", description = "test", size = 2000)
# new.save()
# res = books.objects.all()