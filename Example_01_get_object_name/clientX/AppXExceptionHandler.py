from Teamcenter.Soa.Client import ExceptionHandler
from Teamcenter.Schemas.Soa._2006_03.Exceptions import InternalServerException, ConnectionException, ProtocolException
import Teamcenter.Schemas.Soa._2006_03.Exceptions
import Teamcenter.Soa.Exceptions

# The AppXExceptionHandler class implementing ExceptionHandler
class AppXExceptionHandler(ExceptionHandler):
    __namespace__ = "AppXExceptionHandler"
    def __init__(self):
        pass

    def HandleException(self, ise: Teamcenter.Schemas.Soa._2006_03.Exceptions.InternalServerException) -> None:
        print("\n*****")
        print(f"Exception caught in AppXExceptionHandler.handle_internal_server_exception(InternalServerException): {str(ise)}")
    
        if isinstance(ise, ConnectionException):
            print(f"The server returned a connection error.\n{ise.Message}")
        elif isinstance(ise, ProtocolException):
            print(f"The server returned a protocol error.\n{ise.Message}")
        else:
            print(f"The server returned an internal server error.\n{ise.Message}")

        return None