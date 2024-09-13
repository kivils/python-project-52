from django.test import TestCase, override_settings
from ..views import (
    UsersIndexView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView
)
from django.urls import reverse, resolve


@override_settings(
    SECRET_KEY='fake-key'
)
class UsersUrlsTest(TestCase):
    def test_index_url(self):
        url = reverse('users')
        self.assertEqual(resolve(url).func.view_class, UsersIndexView)

    def test_create_url(self):
        url = reverse('user_create')
        self.assertEqual(resolve(url).func.view_class, UserCreateView)

    def test_update_url(self):
        url = reverse('user_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, UserUpdateView)

    def test_delete_url(self):
        url = reverse('user_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, UserDeleteView)
