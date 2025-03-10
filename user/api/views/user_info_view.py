from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from user.api.serializers import UserProfileSerializer
from user.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED


class AuthenticatedUserInfoView(GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserProfileSerializer
    authentication_classes = [
        BasicAuthentication
    ]
    lookup_field = None

    def get(self, request, *args, **kwargs):
        if (user := request.user) and request.user.is_authenticated:
            queryset = UserProfile.objects.filter(user=user).first()
            serialized = UserProfileSerializer(queryset)
            return Response(serialized.data, HTTP_200_OK)
        return Response({}, HTTP_401_UNAUTHORIZED)

