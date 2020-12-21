
from django import forms
from app17.models import EmployeeModel

class EmployeeForm(forms.ModelForm):

    genders = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
    gender = forms.ChoiceField(choices=genders,widget=forms.RadioSelect)

    desig = (('Select','Select'),('Developer','Developer'),('Tester','Tester'),('Manager','Manager'))
    designation = forms.ChoiceField(choices=desig)

    class Meta:
        model = EmployeeModel
        fields = "__all__"
        #fields = ['name','gender']
        #exclude = ['designation']
        labels = {
            "name":"Employee Name",
            "salary":"Employee Salary",
            "designation":"Employee Designation",
            "photo":"Employee Photo",
            "file":"Employee Documents"
        }


    def clean_designation(self):
        des = self.cleaned_data["designation"]
        if des == "Manager":
            sal = self.cleaned_data["salary"]
            if sal >= 250000:
                return des
            else:
                raise forms.ValidationError("Manager Salary Min is 250000")
        else:
            return des


