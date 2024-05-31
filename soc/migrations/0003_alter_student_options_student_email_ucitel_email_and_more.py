# Generated by Django 4.2.13 on 2024-05-31 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0002_trieda_student_heslo_student_odbor_ucitel_heslo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['priezvisko'], 'verbose_name': 'Študent', 'verbose_name_plural': 'Študenti'},
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ucitel',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=20)),
                ('konzultant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soc.ucitel')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soc.student')),
            ],
        ),
    ]