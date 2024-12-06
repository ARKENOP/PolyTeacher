"""
URL configuration for polyteacher project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from translator.views import index
from translator.views import FrenchSpanishTranslationViewSet
from translator.views import FrenchEnglishTranslationViewSet
from translator.views import AllTranslation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Polyteacher API",
        default_version='v1',
        description="API for Polyteacher project",
        terms_of_service="https://www.Polyteacher.com/",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/all_translation', AllTranslation.as_view()),
]
