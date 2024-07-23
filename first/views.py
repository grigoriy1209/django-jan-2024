from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from first.models import CarModel


class CarListCreateView(APIView):

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        res = [model_to_dict(car) for car in cars]
        return Response(res, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarModel.objects.create(**data)
        car_dict = model_to_dict(car)
        return Response(car_dict, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(car), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        car.brand = data['brand']
        car.year = data['year']
        car.price = data['price']
        car.save()
        return Response(model_to_dict(car), status.HTTP_200_OK)

    # def patch(self, *args, **kwargs):
    #     return Response("Hello patch")

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
