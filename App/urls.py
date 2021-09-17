from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign_up/', views.sign_up, name='sign_up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
