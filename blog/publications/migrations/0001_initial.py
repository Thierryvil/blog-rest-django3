# Generated by Django 3.2.5 on 2021-07-01 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.author')),
            ],
            options={
                'verbose_name_plural': 'publications',
                'db_table': 'publications',
            },
        ),
    ]
