from rest_framework.viewsets import ModelViewSet
from .models import PersonnelInfo
from .serializers import PersonnelInfoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PersonnelInfoViewSet(ModelViewSet):
    queryset = PersonnelInfo.objects.all()
    serializer_class = PersonnelInfoSerializer

    @action(detail=False, methods=["get"])
    def sort_name(self, request):
        queryset = self.get_queryset().order_by("name")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
       
