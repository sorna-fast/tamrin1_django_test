from django.urls import path
from .views import *
from rest_framework.authtoken import views as auth_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    #path("",index,name="index")
    #path("",api_index,name='api_index')
    #path("index/<str:name>/<str:family>/<int:age>",indexApi.as_view(),name="api_index")
    #path("index/",indexApi.as_view(),name="api_index")
    path("people/",PersonList.as_view(),name="PersonList"),
    path("people/<int:code>",SearchPersonById.as_view(),name="SearchPersonById"),
    path("people/add/",PersonAdd.as_view(),name="PersonAdd"),
    path("Product/add/",Productadd.as_view(),name="Productadd"),
    path('api-token-auth/', auth_view.obtain_auth_token),
    path('create_token/', CreateTokenForAllUser.as_view()),
    path("product/",ProductList.as_view()),
    path("product/delete/<int:pk>/",DeleteProductFeature.as_view()),
    path("token/",TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh")
    
]
 