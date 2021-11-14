from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        test_category = Category.objects.create(name='Django')
        test_user = User.objects.create_user(
            username='test_user', password='test_password')
        test_post = Post.objects.create(category_id=1, title='Post title', excerpt='Post excerpt', content='Post content', slug='post-title', author_id='1', status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user')
        self.assertEqual(title, 'Post title')
        self.assertEqual(content, 'Post content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Post title')
        self.assertEqual(str(cat), 'Django')
