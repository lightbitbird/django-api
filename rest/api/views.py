from datetime import datetime

from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import views
from rest.api.models import Book, Author, FoodStuff, Nutrients, Taxes, Countries, States
from rest.api.serializers import UserSerializer, GroupSerializer, AuthorSerializer, BookSerializer, NutrientsSerializer, \
    FoodStuffSerializer, TaxesSerializer, CountriesSerializer, StatesSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AuthorView(views.APIView):
    """
    API endpoint that allows authors to be viewed or edited.
    """

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """Return a list of all authors"""
        authors = [(author.id, author.name, author.birth, author.place) for author in Author.objects.all()]
        return Response(authors)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


# class CountriesView(views.APIView):
#     """
#     API endpoint that allows countries to be viewed or edited.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Countries.objects.get(pk=pk)
#         except Countries.DoesNotExist:
#             raise Http404
#
#     def get(self, request, format=None):
#         """Return a list of all countries"""
#         country_list = [(countries.id, countries.name) for countries in Countries.objects.all()]
#         return Response(country_list)
#
#     def post(self, request):
#         serializer = CountriesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, format=None):
#         countries = self.get_object(pk)
#         serializer = CountriesSerializer(countries, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StatesView(views.APIView):
#     """
#     API endpoint that allows states to be viewed or edited.
#     """
#
#     def get_object(self, pk):
#         try:
#             return States.objects.get(pk=pk)
#         except States.DoesNotExist:
#             raise Http404
#
#     def get(self, request, format=None):
#         """Return a list of all states"""
#         state_list = [(states.id, states.name) for states in States.objects.all()]
#         return Response(state_list)
#
#     def post(self, request):
#         serializer = StatesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, format=None):
#         states = self.get_object(pk)
#         serializer = StatesSerializer(states, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows states to be viewed or edited.
    """
    queryset = States.objects.all().order_by('id')
    serializer_class = StatesSerializer


class CountriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows countries to be viewed or edited.
    """
    queryset = Countries.objects.all().order_by('id')
    serializer_class = CountriesSerializer


class NutrientsView(views.APIView):
    """
    API endpoint that allows nutrients to be viewed or edited.
    """

    def get_object(self, pk):
        try:
            return Nutrients.objects.get(pk=pk)
        except Nutrients.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """Return a list of all authors"""
        nutrients_list = [(nutrients.id, nutrients.carbohydrate, nutrients.protein, nutrients.lipid, nutrients.vitamin,
                           nutrients.calcium, nutrients.iron) for nutrients in Nutrients.objects.all()]
        return Response(nutrients_list)

    def post(self, request):
        serializer = NutrientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        nutrients = self.get_object(pk)
        serializer = NutrientsSerializer(nutrients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxesView(views.APIView):
    """
    API endpoint that allows taxes to be viewed or edited.
    """

    def get_object(self, pk):
        try:
            return Taxes.objects.get(pk=pk)
        except Taxes.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """Return a list of all taxes"""
        taxes_list = [(taxes.id, taxes.country_id, taxes.state_id, taxes.tax) for taxes in Taxes.objects.all()]
        return Response(taxes_list)

    def post(self, request):
        serializer = TaxesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        taxes = self.get_object(pk)
        serializer = NutrientsSerializer(taxes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodStuffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows food_stuff to be viewed or edited.
    """
    queryset = FoodStuff.objects.all().order_by('id')
    serializer_class = FoodStuffSerializer
