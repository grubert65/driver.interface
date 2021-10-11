import importlib

def get_driver(
        driver: str,
        module: str,
        class_name: str,
        **driver_params):
    """
    Imports the driver module and returns a driver obj
    Each driver has to implement the same class
    """
    mod_name = f"{module}.{driver}" if driver else module
    mod = importlib.__import__(mod_name, fromlist=(class_name))
    type = getattr(mod, class_name)
    return type(**driver_params)

