from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . views import HomeView
from . views import AboutView
from . views import ServicesView
from . views import ContactView
from . views import ProductView
from . import views
# my urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('services', ServicesView.as_view(), name='services'),
    path('contact', ContactView.as_view(), name='contact'),
    path('products', ProductView.as_view(), name='products'),
    path('user_register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)