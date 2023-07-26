from rest_framework.views import APIView, Request, Response
from utils.mixin import CreateModelMixin

class GenericAPIView(APIView):
    queryset = None
    serializer_class = None
    lookup_field = "pk"
    # field e passaodn quanod é precios retronar um item pelo id, é possivel mudar essa variavel para qualquer valor, basta a igualdade

class CreateAPiView(GenericAPIView, CreateModelMixin):
        def post(self, request: Request) -> Response:
            return super().create(request=request)