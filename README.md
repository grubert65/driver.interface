# driver.interface
A small Python module to get a driver object for a specific interface module


## Synopsys

    from driver.interface import get_driver

    object = get_driver(
        module  = "<base module providing the interface>"
        driver  = "<the driver that implements the base module class>",
        class_name = "<the class the object refers to>",
        **driver_params = "<dict of params to pass to the driver>"
        )
