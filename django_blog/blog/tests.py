from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass123')
        self.user2 = User.objects.create_user(username='u2', password='pass123')
        self.post = Post.objects.create(title='p1', content='c1', author=self.user)

    def test_create_comment_requires_login(self):
        client = Client()
        url = reverse('comment-create', kwargs={'pk': self.post.pk})
        resp = client.post(url, {'content': 'hello'})
        # should redirect to login because we required login
        self.assertIn(resp.status_code, (302, 401, 302))

        client.login(username='u1', password='pass123')
        resp2 = client.post(url, {'content': 'hello'}, follow=True)
        self.assertEqual(resp2.status_code, 200)
        self.assertTrue(Comment.objects.filter(content='hello', post=self.post).exists())

    def test_edit_delete_only_author(self):
        c = Comment.objects.create(post=self.post, author=self.user, content='x')
        # user2 should not be able to edit/delete
        client = Client()
        client.login(username='u2', password='pass123')
        edit_url = reverse('comment-update', kwargs={'pk': c.pk})
        delete_url = reverse('comment-delete', kwargs={'pk': c.pk})
        resp_edit = client.get(edit_url)
        resp_delete = client.post(delete_url)
        self.assertIn(resp_edit.status_code, (302, 403))
        self.assertIn(resp_delete.status_code, (302, 403))
        # author can edit/delete
        client.login(username='u1', password='pass123')
        resp_ok = client.post(edit_url, {'content': 'edited'}, follow=True)
        self.assertEqual(resp_ok.status_code, 200)
        c.refresh_from_db()
        self.assertEqual(c.content, 'edited')
        resp_del = client.post(delete_url, follow=True)
        self.assertEqual(resp_del.status_code, 200)
        self.assertFalse(Comment.objects.filter(pk=c.pk).exists())

