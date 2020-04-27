# Generated by Django 3.0.4 on 2020-04-27 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'BooksCategory',
                'verbose_name_plural': 'BooksCategories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('author', models.TextField(max_length=300)),
                ('image', models.TextField(default='')),
                ('rating', models.FloatField(default=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BooksCategory')),
            ],
        ),
    ]
