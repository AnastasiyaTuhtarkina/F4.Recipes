from rest_framework import viewsets, generics
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
       queryset = Category.objects.all()
       serializer_class = CategorySerializer

class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
       queryset = Recipe.objects.all()
       serializer_class = RecipeSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
