from django.urls import path
from liveagent.views import LineCallbackView

urlpatterns = [
    path('', LineCallbackView.as_view()),
]
