from django.contrib import admin

# Register your models here.
from blog.models import Post,Category,Watchlist,StreamPlatform,Review

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Watchlist)
admin.site.register(StreamPlatform)

# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('review', 'stars')

# admin.site.register(Review, ReviewAdmin)
admin.site.register(Review)