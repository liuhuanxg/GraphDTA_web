from django.shortcuts import render

from .models import *
import os


def index(request):
    if request.method == "POST":
        params = request.POST
        data_set = params.GET("data_set")
        algorithm = params.GET("algorithm")
        data_houses = DataHouse.objects.filter(data_set_id=data_set, algorithm_id=algorithm)
        if data_houses.exists():
            return render(request, "index.html", {"data_houses": data_houses})
        else:
            os.system("python3 GraphDTA/{} {} {} {}".format(data_set, algorithm))
    data_sets = DataSet.objects.all()
    algorithms = Algorithm.objects.all()
    print(data_sets)
    return render(request, "index.html", {"data_sets": data_sets, "algorithms": algorithms})
