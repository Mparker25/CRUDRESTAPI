from django.urls import path
from widget import views

urlpatterns = [
    path('widgets/', views.WidgetList.as_view()),
    path('widgets/<int:pk>/', views.WidgetDetail.as_view()),
]