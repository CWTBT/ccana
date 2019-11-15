from django.db import models

class Event(models.Model):
    name = models.CharField('Event Name', max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=120)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.first_name+ " " + self.last_name

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
