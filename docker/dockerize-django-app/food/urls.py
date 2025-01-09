from django.urls import path
from .views import (
  FoodList,
  FoodDetail,
)

urlpatterns = [
  path('', FoodList.as_view()),
  path('<int:id>/', FoodDetail.as_view())
]