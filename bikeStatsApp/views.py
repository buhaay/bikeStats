from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Statistics 
from .forms import StatisticsForm
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StatisticsSerializer

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

@csrf_exempt
def stats_list(request):
	"""
	List all code snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		stats = Statistics.objects.all()
		serializer = StatisticsSerializer(stats, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = StatisticsSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def stat_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        stat = Statistics.objects.get(pk=pk)
    except Statistics.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StatisticsSerializer(stat)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StatisticsSerializer(stat, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        stat.delete()
        return HttpResponse(status=204)