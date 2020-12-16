from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import FileUploadParser

from .serializers import InfoSerializer, UploadSerializer
from .models import Deal


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        data = Deal.data_processing()
        serializer = InfoSerializer(data, many=True)
        return Response(serializer.data)

    def create(self, request):
        file = request.FILES.get('deals')
        if file:
            if file.name.split('.')[1] != 'csv':
                return Response({'message': 'Wrong wormat file'}, status.HTTP_404_NOT_FOUND)
            Deal.import_csv(file)
            data = Deal.data_processing()
            serializer = InfoSerializer(data, many=True)
            return Response({'response': serializer.data}, status.HTTP_200_OK)
        else:
            return Response({'message': 'File missing'}, status.HTTP_404_NOT_FOUND)






