from django.db import models
from datetime import datetime

class Person(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام")
    family = models.CharField(max_length = 50,verbose_name="فامیلی")
    email = models.EmailField(max_length=30,verbose_name="ایمیل")
    age=models.PositiveIntegerField(verbose_name="سن")
    username = models.CharField(max_length = 50,verbose_name="نام کاربری")
    password = models.CharField(max_length = 60,verbose_name="پسورد")
    
    def __str__(self):
        return f"{self.name} {self.family} {self.email} {self.username}"

def image_path(instance,filename):      #a.jpg
    ext=filename.split(".")[-1]         # jpg
    name=filename.split(".")[0]         # a
    courrent_date=datetime.utcnow().strftime("%Y%m%d%H%S")  # 202204151835624
    return f"images/products/{name}_{courrent_date}.{ext}"

# images/products/a_202204151835624.jpg

class Product(models.Model):
    name = models.CharField(max_length = 200,verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت",)
    register_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to=image_path,default="images/products/notphoto.png")

    def __str__(self):
        return f"{self.name} {self.price}"
    
from django.contrib.auth.models import User
class ProductFeature(models.Model):
    feature_name=models.CharField(max_length=200)
    feature_vlue=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,related_name="features")
    user_register = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)