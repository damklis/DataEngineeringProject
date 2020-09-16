from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

    email = "testemail@test.com"
    email_upper = "testemail@TESTUPPER.COM"
    password = "testpassword"

    def test_create_user_check_email(self):
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )
        self.assertEqual(user.email, self.email)

    def test_create_user_check_password(self):
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )
        self.assertTrue(user.check_password(self.password))
    
    def test_user_email_normalized(self):
        user = get_user_model().objects.create_user(
            email=self.email_upper,
            password=self.password
        )
        self.assertEqual(user.email, self.email_upper.lower())

    def test_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password=self.password
            )

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email=self.email,
            password=self.password
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
