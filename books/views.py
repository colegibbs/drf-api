from rest_framework import generics
from .models import book
from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = book.objects.all()
  serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = book.objects.all()
  serializer_class = BookSerializer