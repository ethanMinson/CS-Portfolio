from django import forms

from PortfolioDatabase.models import Portfolio

class PortfolioAdd(forms.ModelForm):
    template_name = 'PortfolioDatabase/form_snippit.html'
    class Meta:
        model = Portfolio
        fields = ('name', 'description', 'image', 'slug')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter project name",'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': "Enter project description",'class': 'form-control','rows': 5, 'cols': 50}),
        }

class PortfolioEdit(forms.ModelForm):
    template_name = 'PortfolioDatabase/form_snippit.html'
    class Meta:
        model = Portfolio
        fields = ('name', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter project name",'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': "Enter project description",'class': 'form-control','rows': 5, 'cols': 50}),
        }