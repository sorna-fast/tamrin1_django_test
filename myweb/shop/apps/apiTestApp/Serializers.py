from rest_framework import serializers
from .models import Person,Product,ProductFeature

# class PersonSerializers(serializers.Serializer):
#     name=serializers.CharField(max_length=50)
#     family = serializers.CharField(max_length = 50)
#     email = serializers.EmailField(max_length=30)
#     age=serializers.IntegerField()
#     username = serializers.CharField(max_length = 50)
#     password = serializers.CharField(max_length = 60)


class PersonSerializers(serializers.ModelSerializer):
    re_password=serializers.CharField(write_only=True)
    class Meta:
      model=Person
      # یعنی فقط ایتم های توی لیست رو برام بیار
      #fields=['name','family',"age",'email']
      # یعنی همه باشن بجز این چیزی که توی لیست بهش میدیم
      #exclude=['password']
      fields="__all__"  
      extra_kwargs={
            "password":{"write_only":True}
          }

    def create(self, validated_data):
        del validated_data["re_password"]
        return Person.objects.create(**validated_data)

    def validate_username(self,value):
        if len(value)<6:
            raise serializers.ValidationError("نام کاربری نمی تواند کمتر از 6  کارکتر باشد")
        return value
    
    def validate(self,data):
        if data["password"]!=data["re_password"]:
            raise serializers.ValidationError("رمز عبور و تکرار ان یکسان نمیباشد")
        if len(data["name"])<3:
            raise serializers.ValidationError("نام نمی تواند از 3 کارکتر کمتر باشد")
        return data

def price_validate(value):
    if int(value)<3000:
        raise serializers.ValidationError("قیمت کالا نمی تواند زیر 3000 باشد")

class ProductSerializers(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields="__all__"
        extra_kwargs={
            "name":{"write_only":True},
            "price":{"validators":(price_validate,)}
          }

    def get_features(self,obj):
        res=obj.features.all()
        return ProductFeatureSerializers(instance=res,many=True).data

class ProductFeatureSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductFeature
        fields="__all__"
  