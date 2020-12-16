from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
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
                return Response({'message': 'Wrong format file'}, status.HTTP_404_NOT_FOUND)
            try:
                file_data = Deal.upload_data(file)
            except:
                return Response({'message': 'Error import csv'}, status.HTTP_404_NOT_FOUND)
            data = Deal.data_processing(start_date=file_data[0]['date'], end_date=file_data[len(file_data)-1]['date'])
            serializer = InfoSerializer(data, many=True)
            return Response({'response': serializer.data}, status.HTTP_200_OK)
        else:
            return Response({'message': 'File missing'}, status.HTTP_404_NOT_FOUND)






