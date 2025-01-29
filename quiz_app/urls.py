from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, submit_test
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger konfiguratsiyasi
schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version='v1',
        description="API documentation for Quiz, Question, and Answer models.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@quizapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# Routerlarni sozlash
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

urlpatterns = [
    # API endpointlar
    path('api/', include(router.urls)),
    path('api/submit-test/', submit_test, name='submit-test'),
    
    # Swagger va ReDoc hujjatlari
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
