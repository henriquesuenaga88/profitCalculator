from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^product/', include('product.urls')),
    url(r'^admin/', admin.site.urls),
]
