from django.db import models


# Create your models here.


# Author model
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)


# Book model
class Book(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    page = models.IntegerField()
    published_at = models.DateField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(Author, null=True, through='BookWrittenByAuthor')

    class Meta:
        ordering = ('published_at', 'id')


class BookWrittenByAuthor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)


class Taxes(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    state_id = models.IntegerField()
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class States(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100)


class Nutrients(models.Model):
    id = models.AutoField(primary_key=True)
    carbohydrate = models.DecimalField(max_digits=7, decimal_places=1)
    protein = models.DecimalField(max_digits=7, decimal_places=1)
    lipid = models.DecimalField(max_digits=7, decimal_places=1)
    vitamin = models.DecimalField(max_digits=7, decimal_places=1)
    calcium = models.DecimalField(max_digits=7, decimal_places=1)
    iron = models.DecimalField(max_digits=7, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class FoodStuff(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=100, blank=True, null=True)
    nutrients = models.ForeignKey(Nutrients, related_name='nutrients', null=True, on_delete=models.CASCADE)
    taxes = models.ForeignKey(Taxes, related_name='taxes', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
