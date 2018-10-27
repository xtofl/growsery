import json

from entities import Unit

class JsonStore:
    def __init__(self):
        self.units = {}
    
    def store_unit(self, unit):
        return json.dumps({
            "label": unit.label,
            "conversions": {
                u: {
                    "constant": function(0),
                    "factor": (function(1)-function(0))}
                for u, function in unit.conversions.items() }})
 
    def restore_unit(self, stored):
        s = json.loads(stored)
        def function_from(c, f):
            return lambda x: x*f + c
        return Unit(
            label=s["label"],
            conversions={
                Unit(k): function_from(v["constant"], v["factor"])
                for k, v in s["conversions"].items()
            })

    def store(self, what):
        return self.store_unit(what)
    
    def restore(self, stored):
        return self.restore_unit(stored)