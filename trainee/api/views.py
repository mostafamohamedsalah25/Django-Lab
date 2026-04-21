from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from trainee.models import Trainee
from .serializers import TraineeSerializer



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])  # يتطلب تسجيل دخول حتى للعرض
def trainee_list_api(request):
    trainees = Trainee.objects.all()
    serializer = TraineeSerializer(trainees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def trainee_detail_api(request, pk):
    try:
        trainee = Trainee.objects.get(pk=pk)
    except Trainee.DoesNotExist:
        return Response({'error': 'Trainee not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TraineeSerializer(trainee)
    return Response(serializer.data)



class TraineeCreateAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({'message': 'Ready to create! Please submit a POST request with trainee data.'})
    def post(self, request, format=None):
        serializer = TraineeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TraineeUpdateAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response({'error': 'Trainee not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TraineeSerializer(trainee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response({'error': 'Trainee not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TraineeSerializer(trainee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TraineeDeleteAPI(generics.DestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer