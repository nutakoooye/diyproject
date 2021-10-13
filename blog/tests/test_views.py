from django.test import TestCase

from blog.models import Post, Blogger
from django.urls import reverse

class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_posts = 13
        for post_num in range(1, number_of_posts+1):
            Blogger.objects.create(name=f'test_blogger{post_num}', bio=f'Some bio about test blogger {post_num}')
            blogger = Blogger.objects.get(id=post_num)
            Post.objects.create(
                title = f'post {post_num}',
                content = f'content post {post_num}',
                blogger = blogger
            )

    def test_view_url_exist_at_desired_location(self):
        resp = self.client.get('/blog/blogs/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('all-blogs'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('all-blogs'))

        self.assertTemplateUsed(resp, 'blog/post_list.html')

    def test_pagination_is_five(self):
        resp = self.client.get(reverse('all-blogs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated']==True)
        self.assertTrue(len(resp.context['post_list'])==5)

    def test_list_all_posts(self):
        resp = self.client.get(reverse('all-blogs')+'?page=3')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['post_list']) == 3)