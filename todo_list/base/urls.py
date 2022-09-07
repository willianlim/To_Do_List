from nturl2path import url2pathname
from django.urls import path
from .views import TaskList


urlpatterns = [
	path('', TaskList.as_view(), name='tasks'),
]
