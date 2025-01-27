from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'base'
# url patterns
urlpatterns = [
    path('', base, name='base'),
    path('service/<slug:service_id>/', service, name='service'),
    path('payment', payment, name='payment'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
