from django.conf.urls import url
from user_app import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'user_app'

urlpatterns = [
    url(r'register_user/^$',views.register_user, name='register_user'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)