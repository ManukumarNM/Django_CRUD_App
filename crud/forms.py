# import form class from django
from django import forms 

# import model from models.py 
from .models import Students 

# create a ModelForm 
class StudentsForm(forms.ModelForm):

# specify the name of model to use 
    class Meta:
        model = Students
        # exclude = ['student_mobile']
        fields = '__all__'

        #fields = ['std_course','std_semester']

    
