from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs') #Note to self: on_delete=models This part makes it where deleting a breed also deletes existing dogs of that breed. Breed is also unique, each dog is only assigned one breed, hence the foreign key!
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
