from django.shortcuts import get_object_or_404, render

from .models import Item

# Create your views here.

def detail(request,pk):
    print(Item.objects.all()[0].pk==pk)
    item = get_object_or_404(Item, pk=pk)

    related_items = Item.objects.filter(Category=item.Category, is_sold=False).exclude(pk=pk)[:3]
    return render(request, 'item/detail.html',{'item':item,'related_items':related_items})

