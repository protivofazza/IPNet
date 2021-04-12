from rest_framework.views import APIView, Response

from .models import Users as UsersModel
from .serializers import UsersSerializers


class Users(APIView):

    def get(self, request):
        print('TEST!')
        user = UsersModel.objects.filter(agg_id='005602173').first()
        serializer = UsersSerializers(user).data
        response = {
            'data': serializer
        }
        return Response(response)
