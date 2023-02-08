from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
   # path('portfolio-details', views.portfolio_details, name='portfolio-details'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #to manage rendering images/files from db