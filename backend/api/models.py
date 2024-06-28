from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Since django uses an ORM hence we only need to write our models in python itself
# i.e we need to define the models attributes and stuff.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    # on_delete basically says what should we do when we delete the foreign key, so here by CASCADE
    # we mean that it should delete all the notes related the user as well.
    # The related_name helps create the name of this models attribute in the foreign key model,
    # basically here it says we could get all the notes of the user by User.notes .
    # By default if use the ForeignKey() function it creates a many-to-one relationship, to create 
    # other kind of relationship you could use: models.OneToOneField() or models.ManyToMany() function 
    # instead.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")


    def __str__(self):
        return self.title