from django import forms
from myapp.models import Student

class StudentForm(forms.ModelForm):
    StudentId = forms.IntegerField()
    StudentName = forms.CharField(max_length=50)
    StudentMarks =forms.IntegerField()
    class Meta:
        model = Student
        fields ='__all__'  