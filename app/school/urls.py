from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from students.views import SwaggerUIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
    path("classes/", include("classes.urls")),
    path(
        "openapi/",
        get_schema_view(
            title="School Backend API Docs",
            description="Simple Documentation for Students API"
        ),
        name="openapi-schema",
    ),
    path("", SwaggerUIView.as_view(), name="swagger-ui")
]
