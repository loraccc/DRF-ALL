from django.shortcuts import render,redirect
from rest_framework import generics,serializers
from blog.models import Post,Watchlist,StreamPlatform,Review
from .serializers import WatchlistSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from blog_api.permissions import isAdminOrreadonly   
from django.contrib.auth.models import User



class Reviewdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'    #lookup id
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[IsAuthenticated]

# class Reviewdetail(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     serializer_class = ReviewSerializer

#     def get_queryset(self):
#         # Filter reviews based on the watchlist ID passed in the URL
#         watchlist_id = self.kwargs.get('id')
#         return Review.objects.filter(watchlist_id=watchlist_id)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):

        pk=self.kwargs.get('pk')
        watchlist=Watchlist.objects.get(pk=pk)
        review_user=self.request.user    #Authenticated User
        review_queryset=Review.objects.filter(watchlist=watchlist,review_user=review_user) 
           # first watchlist models ko 
        if review_queryset.exists():
            raise ValidationError('This User Has Already Reviewed ONCE!') 
        
        if watchlist.total_reviews==0:
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(watchlist.avg_rating+serializer.validated_data['rating'])/2

        watchlist.total_reviews=watchlist.total_reviews+1
            
        watchlist.save()

        
        serializer.save(watchlist=watchlist,review_user=review_user)



class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes=[isAdminOrreadonly]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        pk=self.kwargs['pk']
        print("pk:2222222222222", Review.objects.filter(id=pk))
        return Review.objects.filter(id=pk)    #models ko ewatchlist
# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StreamViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

# class StreamViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         Watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(Watchlist)
#         return Response(serializer.data)


class StreamPlatformAV(APIView):
    
    def get(self, request, pk=None):
        if pk is not None:
            try:
                platform = StreamPlatform.objects.get(pk=pk)
                serializer = StreamPlatformSerializer(platform)
                return Response(serializer.data)
            except StreamPlatform.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            platforms = StreamPlatform.objects.all()
            serializer = StreamPlatformSerializer(platforms, many=True,context={'request': request})
            return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchlistAV(APIView):
    # def get(self,request,pk):
    #     if pk is not None:
    #         movie = Movie.objects.filter(pk=pk).first()
    #         if movie:
    #             serializer = MovieSerializer(movie)
    #             return Response(serializer.data)
    #         else:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #     movies=Movie.objects.all()
    #     serializer=MovieSerializer(movies,many=True)
    #     return Response(serializer.data)
    
    def get(self,request,*args, **kwargs):
        if "pk" in kwargs:
            movies=Watchlist.objects.get(id=self.kwargs.get("pk",None))
            serializer=WatchlistSerializer(movies)
        else:
            movies=Watchlist.objects.all()
            serializer=WatchlistSerializer(movies, many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        try:
            platform=StreamPlatformSerializer.get(pk=pk)
            
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    

class FiveStarWatchlistAPIView(APIView):
    def get(self, request):
        # Filter Watchlist objects with 5-star ratings
        watchlists_with_five_stars = Watchlist.objects.filter(stars=5).distinct()
        serializer = WatchlistSerializer(watchlists_with_five_stars, many=True)
        return Response(serializer.data)