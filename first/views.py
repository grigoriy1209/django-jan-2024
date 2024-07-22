from rest_framework.response import Response
from rest_framework.views import APIView


class Cars(APIView):
    def get(self, *args, **kwargs):
        return Response("Hello get")

    def post(self, *args, **kwargs):
        return Response("Hello post")

    def put(self, *args, **kwargs):
        return Response("Hello put")

    def patch(self, *args, **kwargs):
        return Response("Hello patch")

    def delete(self, *args, **kwargs):
        return Response("Hello delete")
