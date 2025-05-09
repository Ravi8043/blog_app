from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from .models import Blog

# Create your tests here.
class PostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testmail@gmail.com'
        )

        self.blog = Blog.objects.create(
            title='Test Blog',
            content='this is a test blog content'
        )
    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(), '/post/1/')
    def test_string_representation(self):
        self.assertEqual(self.blog.title, 'Test Blog')

    def test_blog_content(self):
        self.assertEqual(self.blog.content, 'this is a test blog content')
    def test_blog_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')
        self.assertTemplateUsed(response, 'home.html')
    def test_blog_detail_view(self):   
        response = self.client.get(reverse('post_detail', args='1'))
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'this is a test blog content')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):  # new
        response = self.client.post(reverse('post_new'), {
        'title': 'New title',
        'content': 'New text',
    })
        self.assertEqual(response.status_code, 302)  # Assuming redirect after creation
    # Optionally, follow the redirect and check content
    # follow_response = self.client.get(self.blog.get_absolute_url())
    # self.assertContains(follow_response, 'New title')
    # self.assertContains(follow_response, 'New text')
    def test_post_edit_view(self):
        response = self.client.post(reverse('post_edit', args='1'),{
            'title':'updated title',
            'content':'updated content',
            
        })
        self.assertEqual(response.status_code, 302)
    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200) 