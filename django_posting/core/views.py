from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from core.serializers import SignupSerializer


class SignUpView(CreateAPIView):
    serializer_class = SignupSerializer


def post(self, request, *args, **kwargs) -> Response:
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
