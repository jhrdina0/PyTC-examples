import os
import clr

def load_net_all(reference_folder: str) -> None:
    for ref in os.listdir(reference_folder):
        try:
            if ref.endswith(".dll"):
                clr.AddReference(os.path.join(reference_folder, ref))
        except Exception as e:
            pass
            #print(f"{e}")

def load_net(reference: str) -> None:
    try:
        if reference.endswith(".dll"):
            clr.AddReference(reference)
    except Exception as e:
        pass
        #print(f"{e}")