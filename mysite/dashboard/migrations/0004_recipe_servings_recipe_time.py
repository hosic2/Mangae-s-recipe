# Generated by Django 5.1.1 on 2024-10-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_recipe_link_alter_ingredient_recipe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.CharField(max_length=20, null=True, verbose_name='인분'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.CharField(max_length=50, null=True, verbose_name='요리 시간'),
        ),
    ]
