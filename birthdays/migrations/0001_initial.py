# Generated by Django 2.2.6 on 2019-11-05 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picture', models.URLField(max_length=400)),
                ('fun_fact', models.CharField(max_length=300)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birthdays.Person')),
            ],
        ),
    ]
