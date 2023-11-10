from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Relatives
from .serializers import RelativeSerializer


class RelativesView(APIView):
    def get(self, request):
        user_id = request.user.pk
        relatives = Relatives.objects.filter(user=user_id)
        serialize_data = RelativeSerializer(relatives, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)