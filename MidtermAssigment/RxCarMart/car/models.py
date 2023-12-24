from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User

class CarModel(models.Model):
    car_name = models.CharField(max_length=30)
    price = models.IntegerField()
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE,null = True, blank = True)
    image = models.ImageField(upload_to='car/media/uploads')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, blank = True, null = True)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.car_name


class Comment(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented by {self.name}" 
    

class Purcehase_history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} buy this car name: {self.car.car_name}"    