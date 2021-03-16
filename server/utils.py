"""
Utility Classes and Functions
"""
import json

class ParseRequest(object):
    """Utility Class for parsing the request parameters"""
    def __init__(self, request):
        self.request = request
    
    def parse(self):
        if len(self.request.body) > 0:
            return json.loads(self.request.body.decode())
        else:
            return {}