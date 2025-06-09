from Teamcenter.Soa.Client import RequestListener, ServiceInfo

class AppXRequestListener(RequestListener):
    __namespace__ = "AppXRequestListener"
    def __init__(self):
        pass

    def ServiceRequest(self, info: ServiceInfo):
        # Log or handle the request before sending it to the server
        # For example, logging the service name or operation could be done here
        print(f"Request being sent: Service = {info.Service}, Operation = {info.Operation}")

    def ServiceResponse(self, info: ServiceInfo):
        # Log or handle the response after the server has responded
        # For example, logging the service name or operation could be done here
        print(f"Response received: Service = {info.Service}, Operation = {info.Operation}, ID = {info.Id}")
