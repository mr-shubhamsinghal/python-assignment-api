from django.urls import path
from api_app import views

urlpatterns = [
    path('', views.QuestionSolutionLinks),
    path('getPlantProductionUnit/', views.PlantProduction),
    path('getMachineUtilization/', views.MachineUtilization),
    path('getAverageBelt/', views.AverageBelt)
]
