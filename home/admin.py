from django.contrib import admin

from home.models import *


# 方案模板管理
@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    list_display = ["file_name", "path"]
    list_per_page = 50


# 方案模板管理
@admin.register(Algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ["algorithm_num", "algorithm_name", "path"]
    list_per_page = 50


# 方案模板管理
@admin.register(DataHouse)
class DataHouseAdmin(admin.ModelAdmin):
    list_display = ["data", "algorithm", "results", "results1", "results2", "results3", "results4"]
    list_per_page = 50
