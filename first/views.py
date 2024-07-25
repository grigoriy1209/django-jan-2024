from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


from first.filter import car_filter
from first.models import CarModel
from first.serializers import CarSerializer

from first.models import CarModel


class CarListCreateView(GenericAPIView):

    def get(self, *args, **kwargs):
        queryset = CarModel.objects.filter.order_by('price')
        queryset = CarModel.objects.filter.order_by('-price')
        queryset = CarModel.objects.filter.order_by('-brand')
        queryset = CarModel.objects.filter.order_by('brand')
        queryset = CarModel.objects.filter.order_by('year')
        queryset = CarModel.objects.filter.order_by('-year')

        queryset = CarModel.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
