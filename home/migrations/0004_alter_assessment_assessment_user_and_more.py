# Generated by Django 4.0.4 on 2022-05-18 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_plans_plan_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='assessment_user',
            field=models.CharField(max_length=100, verbose_name='评估人'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.city', verbose_name='评估城市'),
        ),
        migrations.AlterField(
            model_name='plans',
            name='plan_des',
            field=models.TextField(blank=True, null=True, verbose_name='方案描述'),
        ),
    ]
