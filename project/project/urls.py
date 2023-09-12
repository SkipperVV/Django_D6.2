from django.contrib import admin
from django.urls import path, include
from simpleapp.views_old1 import ProductsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
    # подключались к главному приложению с префиксом products/
    path('product/', include('simpleapp.urls')),
    path('products/', ProductsList.as_view()),
]
