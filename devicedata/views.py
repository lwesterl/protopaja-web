from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic

from .models import Data

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

# Testing json serialization
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json




"""
class IndexView(generic.ListView):
    template_name = 'devicedata/index.html'
    context_object_name = 'latest_data_list'

    def get_queryset(self):
        # Return the last three datapoints.
        return Data.objects.order_by('-collection_date')[:3]
"""


def index(request):
    latest_data_list = Data.objects.order_by('-collection_date')[:3]
    context = {
        'latest_data_list': latest_data_list,
    }
    return render(request, 'devicedata/index.html', context)



# not requiring csrf
#@csrf_exempt

# requires login and redirects to /accounts/login/ if not logged in
#@login_required
def send_json(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = 'POST request has arrived. Here is the data: {0}' .format(request.body)
            return HttpResponse(response)

    return HttpResponse('Page was found')

def charts(request):
    context = {}
    return render(request, 'devicedata/charts.html', context)



# API data, in product should require authentication, for example Django REST
def get_data(request):
    # data_list = Data.objects.order_by('-collection_date')
    # Serialize data for JsonResponse
    # output = serializers.serialize('json', data_list)

    # Get data as dictionary, newest first
    data_list = [ Data.as_dict() for Data in Data.objects.order_by('-collection_date')]


    # To get safe=True, we would have to write our own serializer
    return JsonResponse(({'data': data_list}), safe=False)