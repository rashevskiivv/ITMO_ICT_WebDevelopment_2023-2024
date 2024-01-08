# Generated by Django 3.0.7 on 2020-06-05 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField()),
                ('admission_quantity', models.IntegerField()),
                ('admission_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Disks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_date', models.DateField()),
                ('firm', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateField()),
                ('sale_quantity', models.IntegerField()),
                ('sale_price', models.FloatField()),
                ('disk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LR1_secondApp.Disks')),
            ],
        ),
        migrations.CreateModel(
            name='Sale_point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_point_name', models.CharField(max_length=45)),
                ('sale_point_address', models.CharField(max_length=100)),
                ('number_of_stuff', models.IntegerField()),
                ('sale_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LR1_secondApp.Sale')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=100)),
                ('disk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LR1_secondApp.Disks')),
            ],
        ),
        migrations.CreateModel(
            name='Admission_point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_point_name', models.CharField(max_length=45)),
                ('admission_point_address', models.CharField(max_length=100)),
                ('number_of_stuff', models.IntegerField()),
                ('admission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LR1_secondApp.Admission')),
            ],
        ),
        migrations.AddField(
            model_name='admission',
            name='disk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LR1_secondApp.Disks'),
        ),
    ]