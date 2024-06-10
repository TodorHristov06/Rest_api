from django.shortcuts import render
from rest_framework import generics
from .models import Computer
from .serializers import ComputerSerializer

class ComputerList(generics.ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def get_queryset(self):
        queryset = Computer.objects.all()
        processor = self.request.query_params.get('processor')
        gpu = self.request.query_params.get('gpu')
        motherboard = self.request.query_params.get('motherboard')
        ram = self.request.query_params.get('ram')
        if processor:
            queryset = queryset.filter(processor__icontains=processor)
        if gpu:
            queryset = queryset.filter(gpu__icontains=gpu)
        if motherboard:
            queryset = queryset.filter(motherboard__icontains=motherboard)
        if ram:
            queryset = queryset.filter(ram__icontains=ram)
        return queryset
# Create your views here.
