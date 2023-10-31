from django.urls import path, include
from .views import ShortenUrl, redirecttoURL, URLROSTER


urlpatterns = [
    path('', ShortenUrl),
    path('<slug:key>/', redirecttoURL),
    path('urlRoster', URLROSTER),

]
