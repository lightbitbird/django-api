"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest.api import views

authorView = views.AuthorView.as_view()
taxesView = views.TaxesView.as_view()
nutrientsView = views.NutrientsView.as_view()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'authors', views.AuthorView, basename='authors')
router.register(r'books', views.BookViewSet)
router.register(r'states', views.StatesViewSet)
router.register(r'countries', views.CountriesViewSet)
router.register(r'food_stuff', views.FoodStuffViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/authors/', authorView),
    path('api/nutrients/', nutrientsView),
    path('api/taxes/', taxesView),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

