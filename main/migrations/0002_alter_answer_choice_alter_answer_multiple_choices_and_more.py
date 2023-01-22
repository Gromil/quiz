# Generated by Django 4.1.5 on 2023-01-22 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.choice'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='multiple_choices',
            field=models.ManyToManyField(null=True, to='main.multiplechoice'),
        ),
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(null=True, to='main.choice'),
        ),
        migrations.AlterField(
            model_name='question',
            name='multiple_choices',
            field=models.ManyToManyField(null=True, to='main.multiplechoice'),
        ),
    ]