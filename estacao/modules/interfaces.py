class IModule(object):
    def __init__(self):
        pass

    def read(self, type_grandeza: str):
        raise Exception("NotImplementedException")

    def start(self):
        raise Exception("NotImplementedException")