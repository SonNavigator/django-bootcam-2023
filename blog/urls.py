from django.urls import path
from .views import home, post_detail, contact, search


urlpatterns = [
    # path(URL-name, function, ref-name)
    path('', home, name="home"),
    path('blog/<int:post_id>', post_detail, name="post_detail"),
    path('contact', contact, name="contact"),
    path('search', search, name="search")
]

