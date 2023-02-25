from django.urls import path
from .views import home


urlpatterns = [
    # path(URL-name, function)
    path('', home)
]
