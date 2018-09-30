from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=200)


class Dept(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Department'


class Employee(models.Model):
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    salary = models.IntegerField()
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    sales_rep = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField()
    date_shipped = models.DateTimeField()
    total = models.IntegerField()
