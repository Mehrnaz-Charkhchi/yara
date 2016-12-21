from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Purchase
from .serializers import PurchaseSerializer


class PurchaseDetailView(APIView):
    def get(self, request, pk):
        try:
            purchase = Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            purchase = Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        try:
            purchase = Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PurchaseSerializer(purchase, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseView(APIView):
    def post(self, request, format=None):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
