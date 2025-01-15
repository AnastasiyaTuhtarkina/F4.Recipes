from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_swagger.renderers import OpenAPIRenderer
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Recipe API",
        default_version='v1',
        description="API для работы с рецептами",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@recipes.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipes.urls')),  # Подключение маршрутов приложения recipes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Документация Swagger
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
]