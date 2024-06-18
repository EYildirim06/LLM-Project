from django.db import models

class Voter(models.Model):
    CITY_CHOICES = [
        ('City1', 'City 1'),
        ('City2', 'City 2'),
        ('City3', 'City 3'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    SELECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    selection = models.CharField(max_length=1, choices=SELECTION_CHOICES)  

    def __str__(self):
        return self.name
