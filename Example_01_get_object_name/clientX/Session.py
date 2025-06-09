
from Teamcenter.Soa.Client import Connection
from Teamcenter.Soa.Client.Model.Strong import User
from Teamcenter.Schemas.Soa._2006_03.Exceptions import InvalidCredentialsException
from Teamcenter.Services.Strong.Core import SessionService

from clientX.AppXPartialErrorListener import AppXPartialErrorListener
from clientX.AppXCredentialManager import AppXCredentialManager
from clientX.AppXExceptionHandler import AppXExceptionHandler
from clientX.AppXModelEventListener import AppXModelEventListener
from clientX.AppXRequestListener import AppXRequestListener

class Session:
    PartialErrors = AppXPartialErrorListener()
    connection: Connection
    credentialManager: AppXCredentialManager
    
    def __init__(self, host: str):
        # Initialize the credential manager
        self.credentialManager = AppXCredentialManager()
        
        # Set protocol and environment name for connection
        proto: str = ""
        envNameTccs: str = ""
        
        if host.startswith("http"):
            proto = "HTTP"
        elif host.startswith("tccs"):
            proto = "TCCS"
            envNameTccs = host.split('/', 1)[1]  # Extract environment name
        
        # Create the connection object
        self.connection = Connection(host, None, self.credentialManager, "REST", proto, False)
        
        if proto == "TCCS":
            self.connection.SetOption(Connection.TCCS_ENV_NAME, envNameTccs)
        
        # Set exception handler
        self.connection.ExceptionHandler = AppXExceptionHandler()

        # Add listeners
        self.connection.ModelManager.AddPartialErrorListener(self.PartialErrors)
        self.connection.ModelManager.AddModelEventListener(AppXModelEventListener())
        Connection.AddRequestListener(AppXRequestListener())  # Placeholder
        
    def get_connection(self) -> Connection:
        return self.connection
    
    def login(self, username: str, password: str, group: str = "", role: str = "", locale: str = "", discriminator: str = "SoaAppX") -> None | User:
        # Get the service stub for session
        sessionService = SessionService.getService(self.connection)
        
        try:
            # Attempt login
            resp = sessionService.Login(username, password, group, role, locale, discriminator)
            return resp.User
        except InvalidCredentialsException as ex:
            print(f"Login attempt to Teamcenter failed due to invalid credentials: {ex.Message}")
        except Exception as ex:
            print(f"System exception: {ex.Message}")
        return None
    
    def logout(self):
        sessionService = SessionService.getService(self.connection)
        try:
            sessionService.Logout()
        except Exception:
            pass