from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone
from django.core.validators import  MaxValueValidator,MinValueValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='published')

    options=(
    ('draft','Draft'),
    ('published','Published'),

)

    category= models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    title=models.CharField(max_length=100)
    excerpt=models.TextField(null=True)
    content=models.TextField()
    slug=models.SlugField(max_length=100,unique_for_date='published')
    published=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status=models.CharField(max_length=100,choices=options,default='published')

    objects=models.Manager()    #DEFAULT MANAGER
    postobjects=PostObjects()   #CUSTOM MANAGER 

    class Meta:
        ordering = ('-published',)

        def __str__(self) :
            return self.title
        
class StreamPlatform(models.Model):
    name=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    website=models.URLField(max_length=100)

    def __str__(self):
        return self.name
    
class Watchlist(models.Model):
    title=models.CharField(max_length=100)
    storyline=models.CharField(max_length=100)
    stars=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    platform= models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    avg_rating=models.FloatField(default=0)
    total_reviews=models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    active=models.BooleanField(default=True)
    watchlist=models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name='reviews')
    description=models.CharField(max_length=200,null=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.rating)+" | "+ self.watchlist.title

