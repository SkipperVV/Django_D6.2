from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
# импортируем уже знакомый generic
from .filters import ProductFilter  
 
from .models import Product

 
# Create your views here.
 
class Product(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1 # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['filter']= ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context