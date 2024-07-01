from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import WordSerializers
from .models import Word

#import filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
#Pagination import
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12
class WordPaginationListApi(ListAPIView):
    queryset = Word.objects.all().order_by('id')
    serializer_class = WordSerializers
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['wordyordamchi']
    filterset_fields = ['wordturkumi__search']

class WordListApiView(ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['wordyordamchi']
    filterset_fields = ['wordturkumi__search']

class WorsingleListApi(RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializers





# Create your views here.
