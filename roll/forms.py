from pyexpat import model
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields = "__all__"
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
            'last_name':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
            'dept': forms.Select(attrs={'class':'form-control p-2 mt-2'}),
            'saalry':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
            'bonus':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
            'role':forms.Select(attrs={'class':'form-control p-2 mt-2'}),
            'emp': forms.Select(attrs={'class':'form-control p-2 mt-2'}),
            'phone':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
            'email':forms.EmailInput(attrs={'class':'form-control p-2 mt-2'}),
            'hire_date':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),

        }

class FilterEmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields = ['first_name','dept','role']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control p-2 mt-2','required':False}),
            'dept': forms.Select(attrs={'class':'form-control p-2 mt-2'}),
            'role':forms.Select(attrs={'class':'form-control p-2 mt-2'}),
    
            
            

        }