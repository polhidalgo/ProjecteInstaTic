from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)