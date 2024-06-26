from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    #modelo do carro brand
    model = models.CharField(max_length=200)
    #marca do carro brand
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    #ano do modelo do carro factory_year
    factory_year = models.IntegerField(blank=True, null=True)
    #ano do carro model_year
    model_year = models.IntegerField(blank=True, null=True)
    #
    plate = models.CharField(null=True, blank=True, max_length=50)
    #valor do carro value
    value = models.IntegerField()

    #
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    #
    bio = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.model
    

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'