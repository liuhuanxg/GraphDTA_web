# Generated by Django 4.0.4 on 2022-05-26 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_algorithm_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datahouse',
            name='algorithm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.algorithm', verbose_name='算法'),
        ),
        migrations.AlterField(
            model_name='datahouse',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.dataset', verbose_name='数据'),
        ),
    ]