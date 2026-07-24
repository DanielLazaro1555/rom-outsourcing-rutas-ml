import unittest

from models import Usuario
from password_reset import assign_temporary_password, generate_temporary_password


class PasswordResetTests(unittest.TestCase):
    def test_generate_temporary_password_has_expected_length(self):
        password = generate_temporary_password(14)

        self.assertEqual(len(password), 14)

    def test_generate_temporary_password_rejects_short_length(self):
        with self.assertRaises(ValueError):
            generate_temporary_password(6)

    def test_assign_temporary_password_updates_user_hash(self):
        usuario = Usuario(email="reset@example.com", rol="promotor")
        usuario.set_password("anterior123")

        temporary_password = assign_temporary_password(usuario, length=12)

        self.assertTrue(usuario.check_password(temporary_password))
        self.assertFalse(usuario.check_password("anterior123"))


if __name__ == "__main__":
    unittest.main()
