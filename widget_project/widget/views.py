from rest_framework import generics
from .models import Widget
from .serializers import WidgetSerializer


class WidgetList(generics.ListCreateAPIView):
    """
    API Endpoint that allows Widgets to be Viewed or Created
    """
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

class WidgetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API Endpoint to Retrieve, Update, or Destroy Widget Instances
    """
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer