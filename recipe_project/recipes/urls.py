from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
        path('', include(router.urls)),
        path('openapi', get_schema_view(
        title="Recipes",
        description="SF HW-04",
    ), name='openapi-schema'),
        path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
        path('categories/', CategoryList.as_view(), name='category-list'),
        path('recipes/', RecipeList.as_view(), name='recipe-list'),
        path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]