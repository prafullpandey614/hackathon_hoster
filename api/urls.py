from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.APIOverview.as_view()),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('host-hackathon', views.HostHackathonAPIView.as_view(), name='host-hackathon'),
    path('participate-hackathon', views.PartcipantHackathonAPIView.as_view(), name='participate-hackathon'),
    path('submit-solution',views.SubmitYourSolutionAPIView.as_view(),name="submit-solution"),
    path('my-registrations',views.MyRegistrationsAPIView.as_view(),name="registration"),
    path("my-submissions",views.MySubmissionAPIView.as_view(),name="submissions")
    
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)