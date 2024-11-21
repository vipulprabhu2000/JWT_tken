from django.shortcuts import render
from rest_framework.views import APIView 
from .serializers import UserSerializer,LoginSerializer,SuperUserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import user as User
import json


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



# Create your views here.
class RegisteradminAPI(APIView):
    def post(self,request):
        data=request.data
        print(data)
        serialized=SuperUserSerializer(data=data)
        if serialized.is_valid():
            print(serialized.data)
            user=User.objects.create_superuser(email=serialized.data["email"],name=serialized.data["name"],password=serialized.data["password"])
            print(user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    

# Create your views here.
class RegisterAPI(APIView):
    def post(self,request):
        data=request.data
        print(data)
        serialized=UserSerializer(data=data)
        if serialized.is_valid():
            user=User.objects.create_user(email=serialized.data["email"],name=serialized.data["name"],password=serialized.data["password"])
            data=serialized.update(serialized.data)
            return Response({"data":data},status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    

class LoginAPI(APIView):
    
    def post(self,request):
        data=request.data
        print(request.data)
        serialized=LoginSerializer(data=data)
        print(serialized)
        if serialized.is_valid():
            email=serialized.data["email"]
            password=serialized.data["password"]
            print(email)
            user=User.objects.get(email=email)
            print(user)
            if user is not None:
                if user.check_password(password):
                    token=get_tokens_for_user(user)
                    return Response({"token":token,"Code": "Active Login"})
            else :
                return Response({"code":"Not a Valid user"})
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)    

class Userdata(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=User.objects.all().values('id','email','last_login','name',)
        json_data=list(user)
        
        return Response({"data":json_data},status=status.HTTP_200_OK)
    