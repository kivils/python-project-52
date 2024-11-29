from django.test import TestCase, override_settings
from django.urls import reverse, resolve
from ..views import (
    LabelIndexView,
    LabelCreateView,
    LabelDeleteView,
    LabelUpdateView
)


@override_settings(
    SECRET_KEY='fake-key',
)
class LabelUrlsTest(TestCase):
    def test_label_index_url(self):
        url = reverse('labels')
        self.assertEqual(resolve(url).func.view_class, LabelIndexView)

    def test_label_create_url(self):
        url = reverse('labels_create')
        self.assertEqual(resolve(url).func.view_class, LabelCreateView)

    def test_label_update_url(self):
        url = reverse('labels_update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, LabelUpdateView)

    def test_label_delete_url(self):
        url = reverse('labels_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, LabelDeleteView)
