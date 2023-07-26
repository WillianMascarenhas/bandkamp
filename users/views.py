from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner

from utils.mixin import CreateModelMixin
from utils.generic_views import CreateAPiView
from rest_framework import generics

from drf_spectacular.utils import extend_schema

# ------- Forma usando o mixin--------

# class UserView(APIView, CreateModelMixin):
#     # é preciso erdar as clas que contem os metodos que irão ser usados
#     serializer_class = UserSerializer
#     # é preciso epecificar o serializer_class com qual serializer será usado  

#     def post(self, request: Request) -> Response:
#         """
#         Registro de usuários
#         """
#         return super().create(request=request)
    # esse super acessa as classes pai e mãe deles, no casa será a "CreateModelMixin" para pegar a função/metodo de create

# -------- Forma usando o generic que eu criei------

# class UserView(generics.CreateAPiView):
#     serializer_class = UserSerializer

# ------- Forma unsando o generic do proprio restframe work ----------

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    # esse generics pode ser usado para varias rotas simultaneamente
    serializer_class = UserSerializer
    queryset = User.objects.all() #É a forma que o generics tem de secomunicar com os campos da model, para fazer as inserções no db

    # @extend_schema(operation_id="", description="Rotas que necessitam de autenticação", serializer_class="Retornanr um usuario")
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

    # Forma de fazer um personalização mais unica para cada rota

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    # def get(self, request: Request, pk: int) -> Response:
    #     """
    #     Obtençao de usuário
    #     """
    #     user = get_object_or_404(User, pk=pk)

    #     self.check_object_permissions(request, user)

    #     serializer = UserSerializer(user)

    #     return Response(serializer.data)

    # def patch(self, request: Request, pk: int) -> Response:
    #     """
    #     Atualização de usuário
    #     """
    #     user = get_object_or_404(User, pk=pk)

    #     self.check_object_permissions(request, user)

    #     serializer = UserSerializer(user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data)

    # def delete(self, request: Request, pk: int) -> Response:
    #     """
    #     Deleçao de usuário
    #     """
    #     user = get_object_or_404(User, pk=pk)

    #     self.check_object_permissions(request, user)

    #     user.delete()

    #     return Response(status=status.HTTP_204_NO_CONTENT)
