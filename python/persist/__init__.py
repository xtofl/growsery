class JsonStore:
    def __init__(self):
        self.value = None
    
    def store(self, what):
        self.value = what
        return ""
    
    def restore(self, stored):
        return self.value