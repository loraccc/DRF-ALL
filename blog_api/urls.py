from django.urls import path,include
from .views import  (WatchlistAV,StreamPlatformAV
                     ,FiveStarWatchlistAPIView,ReviewList
                     ,Reviewdetail,ReviewCreate,StreamViewSet)
from rest_framework.routers import DefaultRouter
from .serializers import (WatchlistSerializer,
                          StreamPlatformSerializer,
                          ReviewSerializer)
app_name = 'blog_api'

router = DefaultRouter()
router.register('stream', StreamViewSet, basename='streamplatform')
urlpatterns = router.urls
urlpatterns = [
    path('review/<int:id>/', Reviewdetail.as_view(), name='Review-detail'),
    path('<int:pk>/review/', ReviewList.as_view(), name='Review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='Review-create'),
    # path('review/', ReviewList.as_view(), name='ReviewList'),
    # path('review/<int:id>/', Reviewdetail.as_view(), name='Review-detail'),


    # path('<int:pk>/',PostSerializer,name='detailcreate'),
    # path('list/',PostList.as_view(),name='listcreate'),
    path('',WatchlistAV.as_view(),name='movielist'),
    path('<int:pk>/',WatchlistAV.as_view(),name='moviedetail'),


    # path('stream/',StreamPlatformAV.as_view(),name='stream'),
    # path('stream/<int:pk>/',StreamPlatformAV.as_view(),name='stream-detail'),

    path('',include (router.urls)),


    #To get all 5 stars
    path('watchlist/five/', FiveStarWatchlistAPIView.as_view(), name='five-star-watchlist'),
    ]