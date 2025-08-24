
from django.contrib import admin
from django.urls import path
from home.views import *
from project1.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('recipe/', recipe, name="recipe"),
    path('update-recipe/<id>/', update_recipe, name="update-recipe"),
    path('delete-recipe/<id>/', delete_recipe, name="delete-recipe"),
    path('contact-page/', contact, name="contact"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page")
    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
