# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    user = models.ForeignKey('User', models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    ic = models.CharField(max_length=255, blank=True, null=True)
    dic = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'address'


class Category(models.Model):
    parent = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    position = models.IntegerField()
    enabled = models.IntegerField()
    delivery_days = models.IntegerField()
    installation_enabled = models.IntegerField()
    installation_price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'category'


class Order(models.Model):
    user = models.ForeignKey('User', models.RESTRICT)
    shipping_address = models.ForeignKey(Address, models.RESTRICT, blank=True, null=True)
    billing_address = models.ForeignKey(Address, models.RESTRICT, related_name='order_billing_address_set', blank=True, null=True)
    number = models.CharField(unique=True, max_length=255)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255)
    checkout_state = models.CharField(max_length=255)
    payment_state = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255)
    pohoda_export = models.IntegerField()
    shipping_method = models.CharField(max_length=255)
    shipping_price = models.IntegerField()
    payment_method = models.CharField(max_length=255)
    payment_price = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'order'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey('Product', models.RESTRICT)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()

    class Meta:
        db_table = 'order_item'


class Product(models.Model):
    code = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    enabled = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'product'


class ProductParameters(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    parameter_name = models.CharField(max_length=255)
    parameter_value = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_parameters'
        unique_together = (('product', 'parameter_name'),)


class User(models.Model):
    role = models.IntegerField()
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    gender = models.IntegerField()
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    logged_in = models.IntegerField()
    verified = models.IntegerField()

    class Meta:
        db_table = 'user'
