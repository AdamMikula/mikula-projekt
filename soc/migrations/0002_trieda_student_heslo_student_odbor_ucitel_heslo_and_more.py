# Generated by Django 4.2.13 on 2024-05-31 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trieda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Trieda',
                'verbose_name_plural': 'Triedy',
                'ordering': ['nazov'],
            },
        ),
        migrations.AddField(
            model_name='student',
            name='heslo',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='odbor',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ucitel',
            name='heslo',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ucitel',
            name='titul',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='trieda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soc.trieda'),
        ),
    ]
