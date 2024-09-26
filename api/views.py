from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from functools import wraps
from django.db import transaction
from django.shortcuts import render

@api_view(['POST'])
@transaction.atomic 
def import_order(request):
    # Parse data
    serializer = OrderSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=400)

    # Save order to the database
    order = serializer.save()

    # Return success response with total_price
    return Response({
        "message": "Order imported successfully",
        "order_id": order.id,
        "total_price": order.total_price
    }, status=201)