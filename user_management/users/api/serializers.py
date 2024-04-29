from rest_framework import serializers
from ..models import User

# serialziers converts complex queryset and model instace into python data type.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # list of fields
