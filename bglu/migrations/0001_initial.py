# Generated by Django 3.2.12 on 2022-03-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bloodglu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField(max_length=10)),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '其他')])),
                ('Mbglu', models.CharField(max_length=10)),
                ('Abglu', models.CharField(max_length=10)),
                ('Nbglu', models.CharField(max_length=10)),
            ],
        ),
    ]