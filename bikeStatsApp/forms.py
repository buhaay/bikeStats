from .models import Statistics
from django import forms

class StatisticsForm(forms.ModelForm):
	class Meta:
		model = Statistics
		fields = '__all__'
		widgets = {
			'date' : forms.DateInput(format='%Y-%m-%d')
		}