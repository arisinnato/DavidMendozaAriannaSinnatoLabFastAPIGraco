from exceptions import Message_Redirection_Exception

class RequiresLoginException(Message_Redirection_Exception):
    def __init__(self, message='Debes haber iniciado sesión para acceder.', path_route='/iniciar_sesion', path_message='Inicia sesión'):
        super().__init__(message, path_route, path_message)

class LoginExpired(Message_Redirection_Exception):
    def __init__(self, message='Tu sesión ha expirado.', path_route='/iniciar_sesion', path_message='Inicia sesión otra vez'):
        super().__init__(message, path_route, path_message)
