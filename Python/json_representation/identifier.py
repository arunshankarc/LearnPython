"""
Example on how to build json objects
Read this to make python object json serializable -
https://pynative.com/make-python-class-json-serializable/

how to validate json with schema -
https://pynative.com/python-json-validation/
"""
from typing import List
from json import JSONEncoder
import json


class Identifier:
    def __init__(self, type_data: str, value: str):
        self._type = type_data
        self._value = value
        self._validation_output = True

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, new_type: str):
        self._type = new_type

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._value = new_value

    # Add your validations here
    def run_validations(self):
        if isinstance(self._value, str) and isinstance(self._type, str):
            self._validation_output = True
            return True
        self._validation_output = False
        return False

    def to_dict(self) -> dict:
        return {'type': self._type, '@value': self._value, 'validations': self._validation_output}

    def __repr__(self):
        return f"{self._type} : {self._value}"

    def __eq__(self, other):
        if isinstance(other, Identifier):
            return (self._type == other._type and self._value == other._value)
        return False


class RrCoreMatch:
    def __init__(self, identifier: List[Identifier]):
        self._identifier = identifier

    @property
    def identifier(self) -> List[Identifier]:
        return self._identifier

    @identifier.setter
    def identifier(self, new_identifier: List[Identifier]):
        self._identifier = new_identifier

    def to_dict(self) -> dict:
        return {'identifier': self._identifier}

    def __repr__(self):
        return f"{self._identifier}"

    def __eq__(self, other):
        if isinstance(other, RrCoreMatch):
            return (self._identifier == other._identifier)
        return False


class PostProcessingOutput:
    def __init__(self, json_id, reference, rr_core_match_value):
        self._id = json_id
        self._reference = reference
        self._rr_core_match = rr_core_match_value

    @property
    def json_id(self):
        return self._id

    @json_id.setter
    def json_id(self, new_id):
        self._id = new_id

    @property
    def reference(self):
        return self.reference

    @reference.setter
    def reference(self, new_reference):
        self.reference = new_reference

    @property
    def rr_core_match(self):
        return self.rr_core_match

    @rr_core_match.setter
    def rr_core_match(self, new_rr_core_match):
        self.rr_core_match = new_rr_core_match

    def to_dict(self) -> dict:
        return {"@id": f"{self._id}", "reference": f"{self._reference}",
        "rr_core_match": [self._rr_core_match]}

    def __repr__(self):
        return f"@id = {self._id}, reference={self._reference}, rr_core_match={self._rr_core_match}"


class PostProcessingEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


identifier1 = Identifier("EID", "84913598979")
identifier2 = Identifier("parityId", "53674561602")
identifier3 = Identifier("EID", 1234)
print(identifier3.run_validations())
print(PostProcessingEncoder().encode(identifier3.to_dict()))
rr_core_match = RrCoreMatch([identifier1.to_dict(), identifier2.to_dict()])
post_processing_output = PostProcessingOutput("123", "</reference>", rr_core_match.to_dict())
print(post_processing_output)
print(PostProcessingEncoder().encode(post_processing_output.to_dict()))
process_output = json.dumps(post_processing_output.to_dict(), cls=PostProcessingEncoder)
print(process_output)
with open("output.json", 'a', encoding='utf-8') as fd:
    json.dump(post_processing_output.to_dict(), fd)
