from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Statistics 
from .forms import StatisticsForm
from django.views import View

# Create your views here.
class StatisticsView(View):
	def get(self, request):
		statistics = Statistics.objects.all()
		form = StatisticsForm()
		context = {'statistics' : statistics,
				   'form'       : form}
		return render(request, 'statistics.html', context)

	def post(self, request):
		statistics = Statistics.objects.all()
		form = StatisticsForm(request.POST)
		context = {'statistics' : statistics,
				   'form'       : form}
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		return render(request, 'statistics.html', context)