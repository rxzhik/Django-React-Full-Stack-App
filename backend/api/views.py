from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create a view that is goign to allow us to implement creating a new User.
class CreateUserView(generics.CreateAPIView):
        # Here User is a predefined model in django
        # Defines the set of User objects the view will interact with, hence determines the queryset.
        queryset = User.objects.all()
        # Specifies the serializer class to be used for validating and deserializing input, and for serializing output.
        serializer_class = UserSerializer
        # Defines the permission classes that determine who is allowed to access this view.
        permission_classes = [AllowAny]


# Creating views for the Note model
# So this generic view gives to functions get a List of notes or create the note,
# Concrete view for listing a queryset or creating a model instance.
class NoteListCreate(generics.ListCreateAPIView):
        serializer_class = NoteSerializer
        # So this permission basically says that a user can access this view only if the
        # the user passes a JWT token.
        permission_classes = [IsAuthenticated]
        # WHY DO WE NEED TO DEFINE THIS FUNCTION?
        # https://www.django-rest-framework.org/api-guide/generic-views/#attributes
        # here instead of just specifying the queryset, we called get_querset() cuz
        # we need to filter the list of notes based on the user and we need to get the
        # current user, hence its dynamic.
        def get_queryset(self):
                # request: An attribute of the view instance that contains the HTTP request being processed. 
                # It is an instance of HttpRequest.
                # user: A property of the request object that represents the currently authenticated user. 
                # It is set by Django's authentication middleware.
                # So basically every view when instantiated upon a request from a user(authenticated one here),
                # gets access to the HTTPRequest itself and the user as well.
                user = self.request.user
                # Filters the notes based on author himself.
                return Note.objects.filter(author=user)
        # This is because we want to do some custom changes to the create Note functionality hence we are overriding
        # this method. 
        # Since the author in the serualizer was 'read-only', hence here when we try to create a custom method. Hence
        # we need to manually check for serializer validation and if true then manually add the author attribute.
        def perform_create(self, serializer):
                if serializer.is_valid():
                        # When you mark a field as read_only in a Django REST Framework (DRF) serializer, it means that 
                        # the field will not be included in input data when creating or updating an instance through the
                        # serializer. However, you can still set the value of that field manually within your view or 
                        # other business logic, such as in the perform_create method.
                        serializer.save(author=self.request.user)
                else:
                        print(serializer.errors)
        
class NoteDelete(generics.DestroyAPIView):
        serializer_class = NoteSerializer
        permission_classes = [IsAuthenticated]
        
        def get_query(self):
                # Similarly here we want a user to be able to delete only its notes.
                user = self.request.User
                # Filters the notes based on author himself.
                return Note.objects.filter(author=user)


