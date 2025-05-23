from rest_framework import serializers
from profiles_api import models
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""
    name = serializers.CharField(max_length=10) # serializer takes care of validation
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Seraialize a user profile object"""
    
    class Meta:
        model = models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{
                    'input':'password'
                }
            }
        }
    
    def create(self,validatede_data):
        """Create and a return user data"""
        user=models.UserProfile.objects.create(
            email=validatede_data['email'],
            name=validatede_data['name'],
            password=validatede_data['password']
        )
        
        return user