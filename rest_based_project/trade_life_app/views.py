from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
from rest_framework .views import APIView
from .models import Trade
from .serializers import TradeSerializer
from rest_framework.response import Response
import json
# class BaseViewSet(ModelViewSet):
#     def get_queryset(self):
#         return self.model.objects.all()
#
#
# class TradeAPIView(BaseViewSet):
#         serializer_class = TradeSerializer
#         model = Trade


class TradeAPIView(APIView):
    def get(self, request, format=None):
        trades = Trade.objects.all()
        serializer = TradeSerializer(trades, many=True)
        # str_output = json.dumps(serializer.data)
        # print('Output Data : ' + str_output)
        return Response(serializer.data)
