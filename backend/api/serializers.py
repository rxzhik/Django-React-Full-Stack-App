from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        # this tells django that we want to accept password when creating a user but don't
        # want to give the password when returning a user. See the documentation.
        extra_kwargs = {"password" : {"write_only": True}}
    
    # Check the documentation for this, and do chatgpt why we have a create method in the 
    # serializer itself. What this basically does though is that after the serializer validates
    # the data it passes it here to create a User in the database itself using the built-in method.
    # Also since the serializer handles the validation logic we can directly use that to create an obejct
    # here rather than creating a view, also this makes the serializer more reusable and modular. Plus
    # we keep the views only for handling http request itself hence creates a separation of concern. You could
    # create a view but this is better. 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

# Serializer for the note model
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
