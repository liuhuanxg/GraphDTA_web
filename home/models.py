from django.db import models


class DataSet(models.Model):
    class Meta:
        verbose_name = "数据集"
        verbose_name_plural = "数据集"

    file_name = models.CharField(verbose_name="数据集名称", max_length=30)
    path = models.FileField(verbose_name="路径", max_length=30, upload_to="upload/data_set/")

    def __str__(self):
        return self.file_name


class Algorithm(models.Model):
    class Meta:
        verbose_name = "算法"
        verbose_name_plural = "算法"

    algorithm_name = models.CharField(verbose_name="算法名称", max_length=30)
    path = models.FileField(verbose_name="算法文件路径", max_length=30)

    def __str__(self):
        return self.algorithm_name


# 运行结果
class DataHouse(models.Model):
    class Meta:
        verbose_name = "运行结果"
        verbose_name_plural = "运行结果"

    data = models.ForeignKey("Algorithm", verbose_name="数据", on_delete=models.DO_NOTHING)
    algorithm = models.ForeignKey("DataSet", verbose_name="算法", on_delete=models.DO_NOTHING)
    results = models.TextField(verbose_name="运行结果")

    def __str__(self):
        return self.data
