from rest_framework import serializers
from blog.models import (Post,
                         Watchlist,
                         StreamPlatform,
                         Review)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','title','author','excerpt','content','status')


        
class ReviewSerializer(serializers.ModelSerializer):
    # watchlist = WatchlistSerializer(many=True)  # Include WatchlistSerializer for nested representation
    review_user= serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = ['id', 'stars', 'watchlist']
        # fields = '__all__'
        exclude=('watchlist',)
        
class WatchlistSerializer(serializers.ModelSerializer):
    # len_name=serializers.SerializerMethodField()
    reviews=ReviewSerializer(many=True,read_only=True)

    class Meta:
        model=Watchlist
        fields='__all__'
        # fields=['name','desc','active']
        # exclude=['active']
    # def get_len_name(self,object):
    #     return len(object.name)

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchlistSerializer(many=True,read_only=True)                                 #Everydetails
    review=ReviewSerializer(read_only=True)
    # watchlist=serializers.StringRelatedField(many=True,read_only=True)                  # Name
    # watchlist=serializers.PrimaryKeyRelatedField(many=True,read_only=True)             #for number ac to id
    # tracks = serializers.HyperlinkedRelatedField(                                     # for site address
    #     many=True,
    #     read_only=True,
    #     view_name='movielist'
    # )
    class Meta:
        model=StreamPlatform
        fields='__all__'
    def validate_name(self, value):  #validating a name 
        if len(value.strip()) < 2:
            raise serializers.ValidationError('Title length must be at least 2 characters.')
        return value

