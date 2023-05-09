from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.OverviewAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('host-hackathon', views.HostHackathonAPIView.as_view(), name='host-hackathon'),
    # path('login', views.LoginAPIView.as_view(), name='login'),
    
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)