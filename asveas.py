class person:
    def __init__(self,a="yoyo",b="12"):
        self._name=a
        self.age=b
    def get_name(self):
        return _name
    def set_name(self,a):
        self._name=a
        return
    def shoinfo(self):
        print("name:",self._name)
        print("age:",self.age)
