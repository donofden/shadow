import time
import imaplib
import email
import os
import pkgutil

class ControlException(Exception):
    pass

class Command():
    def __init__(self):
        print("------------------------------------------------------")
        print("-                    Commands                        -")
        print("------------------------------------------------------")
        self.commands()

    def commands(self):
        """Try to load all modules found in the modules folder"""
        print("\n")
        print("Loading Modules & Commands...")
        self.modules = []
        path = os.path.join(os.path.dirname(__file__), "modules")
        directory = pkgutil.iter_modules(path=[path])
        for finder, name, ispkg in directory:
            try:
                loader = finder.find_module(name)
                module = loader.load_module(name)
                if hasattr(module, "commandWords") \
                        and hasattr(module, "moduleName") \
                        and hasattr(module, "execute"):
                    self.modules.append(module)
                    for module in self.modules:
                        print("Module '{0}' activate Command - {1}".format(module.moduleName, module.commandWords))
                else:
                    print("[ERROR] The module '{0}' is not in the "
                            "correct format.".format(name))
            except:
                print("[ERROR] The module '" + name + "' has some errors.")
            print("\n")

if __name__ == '__main__':
    Command()
