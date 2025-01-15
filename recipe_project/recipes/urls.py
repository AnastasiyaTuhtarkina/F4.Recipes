from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, RecipeViewSet, CategoryList, RecipeList, RecipeDetail

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
       path('', include(router.urls)),
        path('categories/', CategoryList.as_view(), name='category-list'),
        path('recipes/', RecipeList.as_view(), name='recipe-list'),
        path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]