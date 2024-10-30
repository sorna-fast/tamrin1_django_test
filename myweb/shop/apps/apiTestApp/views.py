# from django.shortcuts import render

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from rest_framework.views import APIView

# # def index(request):
# #     context={
# #         "title":"اموزش = Django Rest Framework"
# #         }
# #     return render(request,'apiTestApp/index.html',context)

# @api_view(["GET","POST"])
# def api_index(request):
#     context={
#         'name':'masud'
#         }
#     return Response(context)

### call by parameters
# from rest_framework.views import APIView
# from rest_framework.response import Response
# class indexApi(APIView):
#     def get(self,request,name,family,age):
#         context={
#             'name':name,
#             'family':family,
#             'age':age
#             }
#         return Response(context)



# class indexApi(APIView):
#     def get(self,request):
#         #name=request.query_params.get('name')
#         #name=request.query_params['name']
#         #name=request.GET['name']
#         name=request.GET.get('name')
#         family=request.GET.get('family')
#         age=request.GET.get('age')
#         context={
#             'name':name,
#             'family':family,
#             'age':age
#             }
#         return Response(context)

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Person
from .Serializers import PersonSerializers,ProductSerializers

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly

class PersonList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        peple=Person.objects.all()
        ser_data=PersonSerializers(instance=peple,many=True)
        
        return Response(data=ser_data.data)
        
    
class SearchPersonById(APIView):
    def get(self,request,code):
        try:
            people=Person.objects.get(id=code)
            # عملیات سریالاز
            ser_data=PersonSerializers(instance=people)
            
            return Response(data=ser_data.data)
        except:
            return Response("Not found")

# class PersonAdd(APIView):
#     def post(self,request):
#         ser_data=PersonSerializers(data=request.POST)
#         if ser_data.is_valid():
#             Person.objects.create(
#                     name=ser_data.validated_data['name'],
#                     family=ser_data.validated_data['family'],
#                     email=ser_data.validated_data['email'],
#                     age=ser_data.validated_data['age'],
#                     username=ser_data.validated_data['username'],
#                     password=ser_data.validated_data['password']
#                 )
#             return Response(data=ser_data.data,status=status.HTTP_201_CREATED)
#         return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

# روش دوم درج
class PersonAdd(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
        ser_data=PersonSerializers(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(data=ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)



class Productadd(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self,request):
        ser_data=ProductSerializers(data=request.data)
        
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class CreateTokenForAllUser(APIView):
    def get(self,request):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_200_OK)



from .models import Product,ProductFeature
class ProductList(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        product=Product.objects.all()
        ser_data=ProductSerializers(instance=product,many=True)
        
        return Response(data=ser_data.data)

from CustomPermissions import CustomPermissionForProductFeature

class DeleteProductFeature(APIView):
    permission_classes = [CustomPermissionForProductFeature]
    def delete(self,request,pk):
        try:
           product_feature= ProductFeature.objects.get(pk=pk)
           self.check_object_permissions(request,product_feature)
           product_feature.delete()
           return Response(f'حذف با موفقیت انجام شد با ایدی')
        except ProductFeature.DoesNotExist:
            return Response("ویژگی مورد نظر یافت نشد")