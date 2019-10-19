from django.conf.urls import url
from django.contrib import admin
from WishListApp1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'insert',views.WishListview),
    url(r'^delete',views.delete)
]
