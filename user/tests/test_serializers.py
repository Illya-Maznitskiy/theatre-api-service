from django.test import TestCase
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from user.serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="testuser", password="password"
        )
        self.serializer = UserSerializer(instance=self.user)

    def test_serializer_valid_data(self):
        data = {
            "username": "newuser",
            "password": "newpassword",
            "first_name": "New",
            "last_name": "User",
            "email": "newuser@example.com",
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, "newuser")
        self.assertTrue(user.check_password("newpassword"))

    def test_serializer_update(self):
        data = {"username": "updateduser", "password": "newpassword"}
        serializer = UserSerializer(
            instance=self.user, data=data, partial=True
        )
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertEqual(updated_user.username, "updateduser")
        self.assertTrue(updated_user.check_password("newpassword"))

    def test_serializer_invalid_password(self):
        data = {"username": "invaliduser", "password": "123"}
        serializer = UserSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
