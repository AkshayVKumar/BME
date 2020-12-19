from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators

# Create your models here.
class Bank_Details(models.Model):
    Bank_Name=models.CharField(max_length=100,blank=False,help_text="Please Enter The Complete Name")
    Account_no=models.CharField(blank=False,unique=True,max_length=20,validators=[validators.RegexValidator(regex='\d{9,20}',message="Enter Only Numerics in Account Number")])
    ifsc=models.CharField(max_length=11,blank=False,validators=[validators.RegexValidator(regex='[A-Z]{4}\d{7}',message="Please Enter The Alphabets in Uppercase")])
    branch=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"{self.Bank_Name} {self.ifsc}"


class Address_Details(models.Model):
    door_no=models.IntegerField(blank=False)
    building_no=models.IntegerField(blank=True)
    street=models.TextField(blank=False)
    area=models.TextField(blank=False)
    district=models.CharField(blank=False,max_length=100)
    state=models.CharField(blank=False,max_length=100)
    country=models.CharField(blank=False,max_length=100)
    pincode=models.CharField(blank=False,max_length=6,validators=[validators.RegexValidator(regex='[0-9]{6}',message="Enter Only Numerics")])
    def __str__(self):
        return f"Address : {self.id}"


class Job(models.Model):
    job_title=models.CharField(max_length=100)

    def __str__(self):
        return self.job_title

class Documents(models.Model):
    aadhar_no=models.CharField(max_length=12,validators=[validators.RegexValidator(regex='\d{12}',message="Please Specify the Proper 12 Digit Number")])
    PAN_no=models.CharField(max_length=10,validators=[validators.RegexValidator(regex='\w{10}',message="Provide Proper PAN Number")])
    voterid_no=models.CharField(max_length=10,validators=[validators.RegexValidator(regex='\w{10}',message="Provide Proper VoterID Number")])
    passport_no=models.CharField(max_length=10,validators=[validators.RegexValidator(regex='\w{9}',message="Provide Proper Passport Number")])
    def __str__(self):
        return self.aadhar_no
    
class Departments(models.Model):
    dept_name=models.CharField(max_length=100)
    manager_id=models.CharField(max_length=8,null=True)#models.ForeignKey(Employee,null=True,on_delete=models.SET_NULL,blank=True)
    loc=models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20,blank=True,null=True)
    last_name=models.CharField(max_length=20,blank=True,null=True)
    job_id=models.ForeignKey(Job,null=True,on_delete=models.SET_NULL)
    acc_details=models.OneToOneField(Bank_Details,null=True,on_delete=models.SET_NULL)
    address=models.OneToOneField(Address_Details,null=True,on_delete=models.SET_NULL)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    gender=models.CharField(max_length=100,choices=(('Male','Male'),('Female','Female')))
    dept=models.ForeignKey(Departments,null=True,on_delete=models.SET_NULL)
    doc=models.OneToOneField(Documents,null=True,on_delete=models.SET_NULL)


    @property
    def eid(self):
        return "BME%05d" % self.id

    def __str__(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name
    
    


