from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from blog.models import Post ,Category

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category=Category.objects.create(name='django')   #creating a category
        test_user1=User.objects.create_user(      #creating a user
            username="test_user1", password="12345")
        test_post=Post.objects.create(category_id=1,title='Post Title',excerpt='excerpt',content='Post Content',slug='post-title',author_id=1,status='published')


    def test_blog_content(self):
        post=Post.postobjects.get(id=1)
        cat=Category.objects.get(id=1)
        author=f'{post.author}'
        title=f'{post.title}'
        excerpt=f'{post.excerpt}'
        content=f'{post.content}'
        status=f'{post.status}'
        self.assertEqual(author,'test_user1')
        # self.assertEqual(title,'Post Title')
        self.assertEqual(content,'Post Content')
        self.assertEqual(status,'published')
        # self.assertEqual(str(post),'Post Title')
        
