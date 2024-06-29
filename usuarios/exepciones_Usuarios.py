from exepciones_David import mensage_para_Redirection_de_Exception

class Requires_el_Login_de_Exception(mensage_para_Redirection_de_Exception):
    def __init__(self, message='iniciado sesión para acceder payaso.', path_route='/iniciar_sesion', path_message='Inicia sesión'):
        super().__init__(message, path_route, path_message)

"""class LoginExpired(mensage_para_Redirection_de_Exception):
    def __init__(self, message='sesion agotada vuelve a logearte.', path_route='/iniciar_sesion', path_message='Inicia sesión otra vez'):
        super().__init__(message, path_route, path_message)"""

class LoginExpired(mensage_para_Redirection_de_Exception):
    def __init__(self, message='sesion agotada vuelve a logearte.', path_route='/iniciar_sesion', path_message='Inicia sesión otra vez'):
        super().__init__(message, path_route, path_message)