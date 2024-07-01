from django.urls import path
from .views import WordListApiView,WorsingleListApi,WordPaginationListApi


urlpatterns = [
    path('',WordListApiView.as_view()),
    path('<int:pk>',WorsingleListApi.as_view()),
    path('pagination/',WordPaginationListApi.as_view())
]