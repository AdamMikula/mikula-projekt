# Generated by Django 5.0 on 2024-06-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0008_alter_tema_konzultant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='heslo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='meno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='odbor',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='priezvisko',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tema',
            name='nazov',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ucitel',
            name='heslo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ucitel',
            name='meno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ucitel',
            name='priezvisko',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ucitel',
            name='titul',
            field=models.CharField(max_length=10),
        ),
    ]
