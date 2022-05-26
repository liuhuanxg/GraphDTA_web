import os

from django.shortcuts import render, redirect

from .models import *


def index(request):
    data_houses = {}
    params = request.GET
    action = params.get("search")
    data_set = int(params.get("data_set", 3))
    algorithm = int(params.get("algorithm", 5))
    if action:
        if data_set >= 2:
            data_set = 2
        if algorithm >= 2:
            algorithm = 2
        if data_set and algorithm:
            data_houses = DataHouse.objects.filter(data_id=data_set, algorithm_id=algorithm)
            if not data_houses.exists():
                os.system("python3 GraphDTA/{} {} {} {}".format(data_set, algorithm))
            else:
                data_houses = data_houses[0]
    data_sets = DataSet.objects.all()
    algorithms = Algorithm.objects.all()
    print(data_houses)
    return render(request, "index.html",
                  {"data_sets": data_sets,
                   "algorithms": algorithms,
                   "data_houses": data_houses,
                   "data_set": data_set,
                   "algorithm": algorithm}
                  )


def upload_data_set(request):
    error = ""
    if request.method == "POST":
        file = request.FILES
        data_set = file.get("data_set", "")
        file_name = data_set.name
        print(file_name)
        if file_name.endswith(".txt"):
            DataSet.objects.create(
                file_name=file_name,
                path=data_set,
            )
            return redirect("/")
        error = "请提交.txt格式数据集"
    return render(request, "upload_data_set.html", {"error": error})
