# Generated by Django 4.1.2 on 2022-10-19 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_created_on_recipe_created_recipe_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.PositiveSmallIntegerField()),
                ('instruction', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipes.recipe')),
            ],
            options={
                'ordering': ['step_number'],
            },
        ),
    ]
