from Teamcenter.Soa.Client.Model import ModelEventListener, ModelObject
from Teamcenter.Soa.Exceptions import NotLoadedException

class AppXModelEventListener(ModelEventListener):
    __namespace__ = "AppXModelEventListener"
    def __init__(self):
        pass

    def LocalObjectChange(self, changedObjs: list[ModelObject]):
        if len(changedObjs) == 0:
            return

        for obj in changedObjs:
            uid = obj.Uid
            obj_type = obj.GetType().Name
            name = ""
            
            if obj_type == "WorkspaceObject":
                try:
                    # Simulating the "object_string" property fetching
                    name = obj.GetProperty("object_string").StringValue
                except NotLoadedException:
                    # Ignore NotLoadedException
                    pass

            # You could log or process the object change information here
            print(f"Object changed: UID = {uid}, Type = {obj_type}, Name = {name}")

    def LocalObjectDelete(self, deletedUids: list[str]):
        if len(deletedUids) == 0:
            return

        for uid in deletedUids:
            print(f"Object deleted: UID = {uid}")
