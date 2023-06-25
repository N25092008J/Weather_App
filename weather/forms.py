from .models import cities # importing classes from other files

from django.forms import ModelForm, TextInput # importing from django library

class user_input(ModelForm): # creating a form

    class Meta: # class to store the metadata

        model = cities # variable to store database

        fields = ["City"] # column_names inside the table

        widgets = {'City':TextInput(attrs = {'class':'input','placeholder':'Eg: Dubai'})} # taking input