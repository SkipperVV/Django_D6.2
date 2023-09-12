from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять 
                                             #постраничный вывод
 
from .models import Product
 
# Create your views here.
 
# В отличие от дженериков, которые мы уже знаем, код здесь надо писать самому, 
# переопределяя типы запросов (например гет или пост, вспоминаем реквесты из модуля C5)
class Products(View):
    
    def get(self, request):
        products = Product.objects.order_by('-price')
        p = Paginator(products, 1)  # создаём объект класса пагинатор, передаём ему список наших 
        # товаров и их количество для одной страницы
 
        products = p.get_page(request.GET.get('page', 1))  # берём номер страницы из get-запроса. 
        # Если ничего не передали, будем показывать первую страницу.        
        # # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами
        
        data = {
            'products': products,
        }
        return render(request, 'product.html', data)