# login.py

def interactive_link_login(username, password):
    # Simulación de autenticación para el protocolo InterActiveLink
    # En un caso real, aquí iría la lógica de comunicación segura
    usuarios_validos = {
        "ia_user": "securepass123",
        "admin": "adminpass"
    }
    if username in usuarios_validos and usuarios_validos[username] == password:
        print("Login exitoso en InterActiveLink.")
        return True
    else:
        print("Credenciales inválidas para InterActiveLink.")
        return False

if __name__ == "__main__":
    user = input("Usuario: ")
    pwd = input("Contraseña: ")
    interactive_link_login(user, pwd)

    print("Prueba de autenticación InterActiveLink completada.")