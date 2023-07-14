from django.contrib import admin
from django.urls import path,include
from asosiy.views import *
from userapp.views import *
from statsapp.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, \
    SpectacularRedocView, \
    SpectacularSwaggerView

router = DefaultRouter()
router.register("mijozlar",MijozModelViewset)
router.register("mahsulotlar",MahsulotModelViewset)
router.register("ombor",OmborModelViewset)
router.register("statistikalar",StatistikaModelViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('apiview_docs/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name = "schema")),
    path('redoc/', SpectacularRedocView.as_view(url_name = "schema")),
    path('token_olish/',  TokenObtainPairView.as_view()),
    path('token_yangilash/',  TokenRefreshView.as_view()),
]
