# Generated by Django 4.2.1 on 2023-06-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('poster', models.ImageField(upload_to='pintrest_posters')),
                ('watch_count', models.IntegerField(null=True)),
                ('likes', models.IntegerField(null=True)),
                ('season', models.CharField(max_length=50)),
                ('episode', models.CharField(max_length=50)),
                ('casts', models.ManyToManyField(to='movie.casts')),
                ('categories', models.ManyToManyField(to='movie.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('poster', models.ImageField(upload_to='pintrest_posters')),
                ('watch_count', models.IntegerField(null=True)),
                ('likes', models.IntegerField(null=True)),
                ('casts', models.ManyToManyField(to='movie.casts')),
                ('categories', models.ManyToManyField(to='movie.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
