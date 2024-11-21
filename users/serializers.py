from rest_framework import serializers 
from users.models import user
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['id','name','email','password']
    
    def update(self,validated_data):
        validated_data.pop('password')
        return validated_data
       
        
class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['id','name','email','password']
        
    

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()



