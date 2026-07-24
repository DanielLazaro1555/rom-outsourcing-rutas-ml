import secrets


PASSWORD_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789"


def generate_temporary_password(length=12):
    if length < 8:
        raise ValueError("La contraseña temporal debe tener al menos 8 caracteres.")
    return "".join(secrets.choice(PASSWORD_ALPHABET) for _ in range(length))


def assign_temporary_password(usuario, length=12):
    temporary_password = generate_temporary_password(length=length)
    usuario.set_password(temporary_password)
    return temporary_password
