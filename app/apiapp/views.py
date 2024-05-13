from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import ApiTestModel

# Create your views here.
def index(request):
    Q = ApiTestModel.objects.all()
    Data = serialize('json', Q, fields=('id', 'title'))
    return HttpResponse(Data, content_type='application/json')

    