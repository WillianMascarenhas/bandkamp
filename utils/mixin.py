# mixin e uma teoria de POO e ela é uma classe que passa metodos para outras classes

from rest_framework.views import Request, Response, status

class CreateModelMixin:
    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)