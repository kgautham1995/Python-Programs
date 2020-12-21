
from django import forms
from app20.models import EmployeeModel

class EmployeeForm(forms.ModelForm):

    desig = (('Developer','Developer'),('Tester','Tester'),('Designer','Designer'),('Manager','Manager'))
    designation = forms.ChoiceField(choices=desig)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = "__all__"
        model = EmployeeModel
        labels = {"name":"Employee Name",
                  "salary":"Employee Salaey",
                  "designation":"Employee Designation",
                  "contactno":"Employee Contact No"}

