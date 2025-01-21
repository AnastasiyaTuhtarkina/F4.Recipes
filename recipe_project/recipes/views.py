from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


@api_view(['GET'])
def category_view(request):
    if request.method == 'GET':
        dishes = Category.objects.filter(categoryType=request.query_params['category'])
        serializer = CategorySerializer(dishes, many=True)
        return Response(serializer.data)    
