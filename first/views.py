from django.db.models import Q
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    CreateModelMixin

from first.filter import car_filter
from first.models import CarModel
from first.serializers import CarSerializer



# class CarListCreateView(GenericAPIView):
#
#     def get(self, *args, **kwargs):
#         # queryset = CarModel.objects.filter(brand__in=['oka','lada'], year__gte=2023) #логіне і
#         # queryset = CarModel.objects.filter(Q(brand__in=['oka','lada']) | Q(year__gte=2023)).order_by('-price').reverse()#сортуваня + зворотній
#         # queryset = CarModel.objects.filter(Q(brand__in=['oka','lada']) | Q (year__gte=2039)).exclude(brand='lada') #або
#         # queryset = CarModel.objects.filter(Q(brand__in=['oka','lada']) | Q(price=2000)).values('id', 'brand')
#         # queryset = CarModel.objects.all()[:2]#pagination
#         queryset = CarModel.objects.all()
#         # res = [model_to_dict(car) for car in cars]
#         serializer = CarSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = CarSerializer(car, data)  # отримуємо
#         serializer.is_valid(raise_exception=True)  # перевіряємо
#         serializer.save()  # додаємо
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = CarSerializer(car, data, partial=True)  # отримуємо частково дані
#         serializer.is_valid(raise_exception=True)  # перевіряємо
#         serializer.save()  # додаємо
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         #     car.delete()
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get_queryset(self):
#         return car_filter(self.request.query_params)
#
#     # def get_serializer(self, *args, **kwargs):
#     #     return super().get_serializer(*args, **kwargs)
#     #
#     # def get_object(self):
#     #     return super().get_object()
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     # def perform_update(self, serializer):
#     #     super().perform_update(serializer)
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()





