from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import CreateUserView, LoginUserView, ManageUserView


class TestURLs(SimpleTestCase):

    def test_create_user_url(self):
        url = reverse("user:create")
        self.assertEqual(resolve(url).func.view_class, CreateUserView)

    def test_login_user_url(self):
        url = reverse("user:get_token")
        self.assertEqual(resolve(url).func.view_class, LoginUserView)

    def test_manage_user_url(self):
        url = reverse("user:manage_user")
        self.assertEqual(resolve(url).func.view_class, ManageUserView)
