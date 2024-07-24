from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from first.models import CarModel
from first.serializers import CarSerializer


class CarListCreateView(GenericAPIView):

    def get(self, *args, **kwargs):
        queryset = CarModel.objects.filter(brand__in=['oka','lada'], year__gte=2023)
        # res = [model_to_dict(car) for car in cars]
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(GenericAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        # try:
        #     car = CarModel.objects.get(pk=pk)
        # except CarModel.DoesNotExist:
        #     return Response("not found", status.HTTP_404_NOT_FOUND)
        car = self.get_object()
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        # pk = kwargs['pk']
        data = self.request.data
        # try:
        #     car = CarModel.objects.get(pk=pk)
        # except CarModel.DoesNotExist:
        #     return Response("not found", status.HTTP_404_NOT_FOUND)
        car = self.get_object()
        serializer = CarSerializer(car, data)  # отримуємо
        serializer.is_valid(raise_exception=True)  # перевіряємо
        serializer.save()  # додаємо
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        # pk = kwargs['pk']
        data = self.request.data
        # try:
        #     car = CarModel.objects.get(pk=pk)
        # except CarModel.DoesNotExist:
        #     return Response("not found", status.HTTP_404_NOT_FOUND)
        car = self.get_object()
        serializer = CarSerializer(car, data, partial=True)  # отримуємо частково дані
        serializer.is_valid(raise_exception=True)  # перевіряємо
        serializer.save()  # додаємо
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        # pk = kwargs['pk']
        # data = self.request.data
        # try:
        #     car = CarModel.objects.get(pk=pk)
        #     car.delete()
        # except CarModel.DoesNotExist:
        #     return Response("not found", status.HTTP_404_NOT_FOUND)
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
