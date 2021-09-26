# Generated by Django 3.2.7 on 2021-09-26 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('downvotes', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('chart_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
                ('views', models.IntegerField()),
                ('films', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chartit.film')),
            ],
        ),
    ]