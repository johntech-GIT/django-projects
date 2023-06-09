# Generated by Django 4.2.1 on 2023-05-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc_donalds', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(blank=True)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='mc_donalds.ProductOrder', to='mc_donalds.product'),
        ),
    ]
