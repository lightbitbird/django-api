from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest.api.models import Book, Author, Nutrients, FoodStuff, Taxes, Countries, States


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        author = Author(**validated_data)
        author.save()
        return author

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth', 'place']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'price', 'page', 'authors', 'published_at']

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        author_list = []
        for author_data in authors_data:
            author_instance, created = Author.objects.get_or_create(**author_data)
            author_list.append(author_instance)

        book = Book.objects.create(**validated_data)
        book.authors.set(author_list)
        book.save()
        return book


class NutrientsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        nutrients = Nutrients(**validated_data)
        nutrients.save()
        return nutrients

    class Meta:
        model = Nutrients
        fields = ['id', 'carbohydrate', 'protein', 'lipid', 'vitamin', 'calcium', 'iron']


class CountriesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        country = Countries(**validated_data)
        country.save()
        return country

    class Meta:
        model = Countries
        fields = ['id', 'name']


class StatesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        states = States.objects.create(**validated_data)
        return states

    class Meta:
        model = States
        fields = ['id', 'country_id', 'name']


class TaxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxes
        fields = ['id', 'country_id', 'state_id', 'tax']


class FoodStuffSerializer(serializers.ModelSerializer):
    nutrients = NutrientsSerializer()
    taxes = TaxesSerializer()

    def create(self, validated_data):
        nutrients_data = validated_data.pop('nutrients')
        nutrients, created = Nutrients.objects.get_or_create(**nutrients_data)
        taxes_data = validated_data.pop('taxes')
        taxes, created = Taxes.objects.get_or_create(**taxes_data)
        food_stuff = FoodStuff.objects.create(**validated_data, nutrients=nutrients, taxes=taxes)
        return food_stuff

    class Meta:
        model = FoodStuff
        fields = ['id', 'name', 'place', 'nutrients', 'taxes']
