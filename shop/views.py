from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

from shop.models import Item
from shop.serializers import ItemSerializer, PaymentSerializer


class ItemRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        return render(request, 'shop/item_detail.html', {'item': item})

class PaymentRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Item.objects.all()
