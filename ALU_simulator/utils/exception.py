class InvalidInput(Exception):
    def __init__(self, classname = None):
        super().__init__()
        self.error = True
        self.classname = self.__class__.__name__ if classname == None else classname
        self.error_message = classname + ": Invalid input"
  
        
class InvalidOperation(Exception):
    def __init__(self, classname = None):
        super().__init__()
        self.error = True
        self.classname = self.__class__.__name__ if classname == None else classname
        self.error_message = classname + ": Invalid operation"
    
        
class InvalidType(Exception):
    def __init__(self, classname = None):
        super().__init__()
        self.error = True
        self.classname = self.__class__.__name__ if classname == None else classname
        self.error_message = classname + ": Invalid Type"