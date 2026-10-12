from django.db import models

# Create your models here.


class LoginTable(models.Model):
    Login_identifier = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    user_type = models.CharField(max_length=20, null=True, blank=True)

class ShopTable(models.Model):
    shop_name = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=30, name=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    Date_joined = models.DateField(auto_now_add=True)
    Login_id = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)

class StaffTable(models.Models):
    Staff_code = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blanl=True)
    Designation = models.CharField(max_length=20, null=True, blank=True)
    assigned_counter = models.IntegerField(null=True, blank=True)
    LOgin_id = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)

class Product_Table(models.Models):
        product_name = models.CharField(max_length=20, null=True, blank=True)
        Brand = models.CharField(max_length=20, null=True, blank=True)
        Quantity = models.IntegerField(null=True, blank=True)
        Expiry_Date = models.DateField(auto_now_add=True)
        Manufacturing_Date = models.DateField(auto_now_add=True)
        Category = models.CharField(max_length=20, null=True, blank=True)
        Supplier_Name = models.CharField(max_length=20, null=True, blank=True)
        Supplier_email = models.CharField(max_length=20, null=True, blank=True)
        Supplier_Phone = models.CharField(max_length=20, null=True, blank=True)
        Barcode = models.IntegerField(null=True, blank=True)
        Purchase_Price = models.IntegerField(null=True, blank=True)
        Selling_Price = models.IntegerField(null=True, blank=True)
        Unit = models.IntegerField(null=True, blank=True)
        Description = models.CharField(max_length=20, null=True, blank=True)
        Discount = models.CharField(max_length=20, null=True, blank=True)
        Offers = models.CharField(max_length=20, null=True, blank=True)

class  CustomerTable(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    Address = models.CharField(max_length=20, null=True, blank=True)
    Created_At = models.DateField(auto_now_add=True)

class StockTable(models.Models):
    phone = models.IntegerField(null=True, blank=True)
    Product_id = models.ForeignKey(Product_Table, on_delete=models.CASCADE, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Las_Updated = models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=20, null=True, blank=True)

class DiscountTable(models.Models):
     






















