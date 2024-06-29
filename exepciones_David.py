class mensage_para_Redirection_de_Exception(Exception):
    def __init__ (self, message: str, path_route: str, path_message: str):
        self.message = message
        self.path_route = path_route
        self.path_message = path_message

"""class No_para_artesano_Exception(Message_Redirection_Exception):
    def __init__(self, message='si quiere acceder a esta función debe ser otro tipo de usuario.', path_route='/home', path_message='home.'):
        super().__init__(message, path_route, path_message)"""

class No_para_cliente_Exception(mensage_para_Redirection_de_Exception):
    def __init__(self, message='si desea acceder a esta función debe ser otro tipo de usuario.', path_route='/home', path_message='home.'):
        super().__init__(message, path_route, path_message)

class No_para_artesano_Exception(mensage_para_Redirection_de_Exception):
    def __init__(self, message='si quiere acceder a esta función debe ser otro tipo de usuario.', path_route='/home', path_message='home.'):
        super().__init__(message, path_route, path_message)