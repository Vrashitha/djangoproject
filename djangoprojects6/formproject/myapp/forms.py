from django import forms
class StudentForm(forms.Form):
	name = forms.CharField()
	USN = forms.CharField()
	mob = forms.IntegerField()
	branch = forms.CharField()
	Email = forms.CharField()

