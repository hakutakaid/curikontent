import sys
import logging
import importlib
from pathlib import Path

def load_module(plugin_name):
    path = Path(f"B/module/{plugin_name}.py")
    name = "B.module.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["B.module." + plugin_name] = load
    print("Sukses Ngentod! " + plugin_name)
