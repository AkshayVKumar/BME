# Generated by Django 2.2 on 2020-12-12 21:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_no', models.IntegerField()),
                ('building_no', models.IntegerField(blank=True)),
                ('street', models.TextField()),
                ('area', models.TextField()),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter Only Numerics', regex='[0-9]{6}')])),
            ],
        ),
        migrations.CreateModel(
            name='Bank_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_Name', models.CharField(help_text='Please Enter The Complete Name', max_length=100)),
                ('Account_no', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Enter Only Numerics in Account Number', regex='\\d{9,20}')])),
                ('ifsc', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Please Enter The Alphabets in Uppercase', regex='[A-Z]{4}\\d{7}')])),
                ('branch', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_no', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Please Specify the Proper 12 Digit Number', regex='\\d{12}')])),
                ('PAN_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Provide Proper PAN Number', regex='\\w{10}')])),
                ('voterid_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Provide Proper VoterID Number', regex='\\w{10}')])),
                ('passport_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Provide Proper Passport Number', regex='\\w{9}')])),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('sal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('acc_details', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.Bank_Details')),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.Address_Details')),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.Departments')),
                ('doc', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.Documents')),
                ('job_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.Job')),
            ],
        ),
    ]
