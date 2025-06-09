from Teamcenter.Soa.Client import CredentialManager
from Teamcenter.Schemas.Soa._2006_03.Exceptions import InvalidCredentialsException, InvalidUserException
from Teamcenter.Soa import SoaConstants
from System.IO import IOException

import typing

# Assuming CredentialManager is an interface, we need to implement all its methods
class AppXCredentialManager(CredentialManager):
    __namespace__ = "AppXCredentialManager"
    def __init__(self):
        # Initialize with default values
        self.name = ""
        self.password = ""
        self.group = ""
        self.role = ""
        self.discriminator = ""

    CredentialType = SoaConstants.CLIENT_CREDENTIAL_TYPE_SSO
    
    def get_CredentialType(self) -> int:
        return SoaConstants.CLIENT_CREDENTIAL_TYPE_STD

    def GetCredentials(self, invalidUser: InvalidUserException) -> list[str]:
        if not self.name:
            return self.PromptForCredentials()
        
        return [self.name, self.password, self.group, self.role, self.discriminator]

    def SetGroupRole(self, group: str, role: str):
        self.group = group
        self.role = role

    def SetUserPassword(self, user: str, password: str, discriminator: str):
        self.name = user
        self.password = password
        self.discriminator = discriminator

    def PromptForCredentials(self):
        try:
            self.name = "user_example"
            self.password = "password_example"
        except IOException as e:
            message = f"Failed to get the name and password.\n{str(e)}"
            print(message)
            raise Exception(message)

        return [self.name, self.password, self.group, self.role, self.discriminator]