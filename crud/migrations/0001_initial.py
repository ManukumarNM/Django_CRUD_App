# Generated by Django 3.2.4 on 2021-06-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=255)),
                ('std_email', models.EmailField(max_length=254)),
                ('std_address', models.TextField()),
                ('std_course', models.CharField(choices=[('0', 'Choose'), ('1', 'MCA'), ('2', 'MBA'), ('3', 'MTECH'), ('4', 'BCA'), ('5', 'BBA'), ('6', 'BE')], default='0', max_length=7)),
                ('std_semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=8)),
                ('std_mobile', models.IntegerField()),
            ],
        ),
    ]
