class RulesException(Exception):
    pass

class CoordinateException(RulesException):
    pass 

class BorderException(RulesException):
    pass 

class OverlapException(RulesException):
    pass 

class NeighbourException(RulesException):
    pass 

class NotImplementedException(RulesException):
    pass