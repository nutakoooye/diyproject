from django.test import TestCase
from django.contrib.auth.models import User


from blog.models import Comment, Blogger, Post

class BloggerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Blogger.objects.create(name='test_blogger', bio='Some bio about test blogger')

    def test_name_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_name_max_lenght(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_blogger_str(self):
        blogger = Blogger.objects.get(id=1)
        excepted_object_name = blogger.name
        self.assertEqual(excepted_object_name, str(blogger))

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(blogger.get_absolute_url(), '/blog/blogger/1')


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        user = User.objects.create_user('test_user', 'test@mail.com', 'some1223password')
        user.first_name = 'test'
        user.last_name = 'user'
        user.save()

        Blogger.objects.create(name='test_blogger', bio='Some bio about test blogger')
        blogger = Blogger.objects.get(id=1)
        post = Post.objects.create(
            title = 'My test blog',
            content = 'rtejrg90vponfemds,',
            blogger = blogger,
        )

        Comment.objects.create(
            author = user,
            message = 'Hellov',
            post = post,
        )

    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_object_name(self):
        comment = Comment.objects.get(id=1)
        expected_name = comment.author.first_name + ' ' + comment.author.last_name
        self.assertEqual(expected_name, str(comment))


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Blogger.objects.create(name='test_blogger', bio='Some bio about test blogger')
        blogger = Blogger.objects.get(id=1)
        Post.objects.create(
            title='My test blog',
            content='rtejrg90vponfemds,',
            blogger=blogger,
        )

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_object_name(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, str(post))

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/blog/1/')