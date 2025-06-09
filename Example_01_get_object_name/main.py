from importManager import load_net_all
load_net_all(r"C:\soa_client\net\libs") # load all .NET dlls from folder using pythonnet

from clientX.Session import Session     # clientX module converted from C# Siemens example to native python

from Teamcenter.Services.Strong.Core import DataManagementService

def get_object_name(dm_service: DataManagementService, uid: str) -> str:
    sd = dm_service.LoadObjects([uid])
    if not sd.sizeOfPlainObjects():
        print("Failed to load ModelObject using UID")
        return ""

    mdo = sd.GetPlainObject(0)
    dmService.GetProperties([mdo], ["object_name"])

    object_name = mdo.GetProperty("object_name")
    return str(object_name.StringValue)

if __name__ == "__main__":
    session = Session("http://10.1.2.48:7001/tc")
    session.login("infodba", "infodba", "dba", "DBA", "en_US", "SoaAppX")

    dmService = DataManagementService.getService(session.get_connection())

    object_uid = "AkNAAIBdJXe22A"
    object_name = get_object_name(dmService, object_uid)

    print(f"UID: {object_uid} object_name: {object_name}")