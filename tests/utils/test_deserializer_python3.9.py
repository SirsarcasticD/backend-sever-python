# import unittest
# from typing import Union, List, Dict, Optional
# from dataclasses import dataclass, field
# import json
#
# from webapp.webapp.utils.deserializer import Deserializer, CustomError
#
#
# def convert_to_string(var: int):
#     return str(var)
#
#
# class TestClass:
#     pass
#
#
# @dataclass
# class TestDataClass1:
#     a: int = field(default_factory=convert_to_string)
#
#
# @dataclass
# class TestDataClass2:
#     a: int
#     b: float
#
#
# @dataclass
# class TestDataClass3:
#     a: int
#     b: float
#     c: str
#
#
# @dataclass
# class TestDataClass4:
#     a: int
#     b: float
#     c: str
#     d: bool
#
#
# @dataclass
# class TestDataClass5:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#
#
# @dataclass
# class TestDataClass6:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[int]
#
#
# @dataclass
# class TestDataClass7:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[int]
#     g: dict[str, int]
#
#
# @dataclass
# class TestSubDataClass:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[int]
#     g: dict[str, int]
#
#
# @dataclass
# class TestDataClass8:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[int]
#     g: dict[str, int]
#     h: TestSubDataClass
#
#
# @dataclass
# class TestDataClass9:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[list[int]]
#     g: dict[str, int]
#     h: TestSubDataClass
#
#
# @dataclass
# class TestSubDataClass2:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[list[int]]
#     g: dict[str, dict[str, int]]
#
#
# @dataclass
# class TestDataClass10:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[list[int]]
#     g: dict[str, dict[str, int]]
#     h: TestSubDataClass
#
#
# @dataclass
# class TestDataClass11:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[list[int]]
#     g: dict[str, dict[str, int]]
#     h: TestSubDataClass2
#
#
# @dataclass
# class TestDataClass12:
#     a: int
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: List[list[int]]
#     g: dict[str, Dict[str, int]]
#     h: TestSubDataClass2
#
#
# @dataclass
# class TestDataClass13:
#     a: Union[float, str]
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[list[int]]
#     g: dict[str, dict[str, int]]
#     h: TestSubDataClass2
#
#
# @dataclass
# class TestDataClass14:
#     a: Union[int, str]
#     b: float
#     c: str
#     d: bool
#     e: any
#     f: list[list[int]]
#     g: dict[str, dict[str, int]]
#     h: TestSubDataClass2
#
#
# @dataclass
# class TestDataClass15:
#     a: int = 4
#
#
# @dataclass
# class TestDataClass16:
#     o: dict[int, int]
#
#
# @dataclass
# class TestDataClass17:
#     n: dict[int]
#
#
# class TestDeserializer(unittest.TestCase):
#
#     def test_deserialize_data_valid_input(self):
#
#         with self.subTest(""):
#
#             data = {
#                 "a": 1
#             }
#
#             expected_data = {
#                 "a": "1"
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass1, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass1(**expected_data))
#
#         with self.subTest(""):
#
#             data = {
#                 "a": 1,
#                 "b": 2.2
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass2, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass2(**data))
#
#         with self.subTest(""):
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value"
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass3, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass3(**data))
#
#         with self.subTest(""):
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass4, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass4(**data))
#
#         with self.subTest(""):
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass5, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass5(**data))
#
#         with self.subTest(""):
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [1, 2, 3]
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass6, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass6(**data))
#
#         with self.subTest(""):
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [1, 2, 3],
#                 "g": {"outerkey1": 1, "outerkey2": 2},
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass7, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass7(**data))
#
#         with self.subTest(""):
#
#             subdata = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [1, 2, 3],
#                 "g": {"outerkey1": 1, "outerkey2": 2},
#             }
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [1, 2, 3],
#                 "g": {"outerkey1": 1, "outerkey2": 2},
#                 "h": subdata
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass8, json_decoded)
#             expected_subobject = TestSubDataClass(
#                 a=subdata['a'],
#                 b=subdata['b'],
#                 c=subdata['c'],
#                 d=subdata['d'],
#                 e=subdata['e'],
#                 f=subdata['f'],
#                 g=subdata['g'],
#             )
#             expected_object = TestDataClass8(
#                 a=data['a'],
#                 b=data['b'],
#                 c=data['c'],
#                 d=data['d'],
#                 e=data['e'],
#                 f=data['f'],
#                 g=data['g'],
#                 h=expected_subobject
#             )
#             self.assertEqual(deserialized_object, expected_object)
#
#         with self.subTest(""):
#
#             subdata = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [1, 2, 3],
#                 "g": {"outerkey1": 1, "outerkey2": 2},
#             }
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": 1, "outerkey2": 2},
#                 "h": subdata
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass9, json_decoded)
#             expected_subobject = TestSubDataClass(
#                 a=subdata['a'],
#                 b=subdata['b'],
#                 c=subdata['c'],
#                 d=subdata['d'],
#                 e=subdata['e'],
#                 f=subdata['f'],
#                 g=subdata['g'],
#             )
#             expected_object = TestDataClass9(
#                 a=data['a'],
#                 b=data['b'],
#                 c=data['c'],
#                 d=data['d'],
#                 e=data['e'],
#                 f=data['f'],
#                 g=data['g'],
#                 h=expected_subobject
#             )
#             self.assertEqual(deserialized_object, expected_object)
#
#         with self.subTest(""):
#
#             subdata = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [1, 2, 3],
#                 "g": {"outerkey1": 1, "outerkey2": 2},
#             }
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}},
#                 "h": subdata
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass10, json_decoded)
#             expected_subobject = TestSubDataClass(
#                 a=subdata['a'],
#                 b=subdata['b'],
#                 c=subdata['c'],
#                 d=subdata['d'],
#                 e=subdata['e'],
#                 f=subdata['f'],
#                 g=subdata['g'],
#             )
#             expected_object = TestDataClass10(
#                 a=data['a'],
#                 b=data['b'],
#                 c=data['c'],
#                 d=data['d'],
#                 e=data['e'],
#                 f=data['f'],
#                 g=data['g'],
#                 h=expected_subobject
#             )
#             self.assertEqual(deserialized_object, expected_object)
#
#         with self.subTest(""):
#
#             subdata = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}}
#             }
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}},
#                 "h": subdata
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass11, json_decoded)
#             expected_subobject = TestSubDataClass2(
#                 a=subdata['a'],
#                 b=subdata['b'],
#                 c=subdata['c'],
#                 d=subdata['d'],
#                 e=subdata['e'],
#                 f=subdata['f'],
#                 g=subdata['g'],
#             )
#             expected_object = TestDataClass11(
#                 a=data['a'],
#                 b=data['b'],
#                 c=data['c'],
#                 d=data['d'],
#                 e=data['e'],
#                 f=data['f'],
#                 g=data['g'],
#                 h=expected_subobject
#             )
#             self.assertEqual(deserialized_object, expected_object)
#
#         with self.subTest(""):
#
#             subdata = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}}
#             }
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}},
#                 "h": subdata
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass12, json_decoded)
#             expected_subobject = TestSubDataClass2(
#                 a=subdata['a'],
#                 b=subdata['b'],
#                 c=subdata['c'],
#                 d=subdata['d'],
#                 e=subdata['e'],
#                 f=subdata['f'],
#                 g=subdata['g'],
#             )
#             expected_object = TestDataClass12(
#                 a=data['a'],
#                 b=data['b'],
#                 c=data['c'],
#                 d=data['d'],
#                 e=data['e'],
#                 f=data['f'],
#                 g=data['g'],
#                 h=expected_subobject
#             )
#             self.assertEqual(deserialized_object, expected_object)
#
#     def test_deserialize_data_invalid_input(self):
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#                 data = {
#                     "a": "1"
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass1, json_decoded)
#                 self.assertEqual(deserialized_object, TestDataClass1(**data))
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 data = {
#                     "a": 1,
#                     "b": "2.2"
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass2, json_decoded)
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 data = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": 12345
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass3, json_decoded)
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 data = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": None
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass4, json_decoded)
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 data = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": ["1", 2, 3]
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass6, json_decoded)
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 data = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [1, 2, 3],
#                     "g": {"outerkey1": 1, "outerkey2": "2"},
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass7, json_decoded)
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 subdata = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [1, 2, 3],
#                     "g": {"outerkey1": 1, "outerkey2": "2"},
#                 }
#
#                 data = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [1, 2, 3],
#                     "g": {"outerkey1": 1, "outerkey2": 2},
#                     "h": subdata
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass8, json_decoded)
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 subdata = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [1, 2, 3],
#                     "g": {"outerkey1": 1, "outerkey2": 2},
#                 }
#
#                 data = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [[1, 2, 3], [4, 5, "6"]],
#                     "g": {"outerkey1": 1, "outerkey2": 2},
#                     "h": subdata
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass9, json_decoded)
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 subdata = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [1, 2, 3],
#                     "g": {"outerkey1": 1, "outerkey2": 2},
#                 }
#
#                 data = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [[1, 2, 3], [4, 5, 6]],
#                     "g": {"outerkey1": {"innerkey1": 1},
#                           "outerkey2": {"innerkey2": "2"}},
#                     "h": subdata
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass10, json_decoded)
#
#         with self.subTest(""):
#             with self.assertRaises(TypeError):
#
#                 subdata = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [[1, 2, 3], [4, 5, 6]],
#                     "g": {"outerkey1": {"innerkey1": 1},
#                           "outerkey2": {"innerkey2": 2}}
#                 }
#
#                 data = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [[1, 2, 3], [4, 5, 6]],
#                     "g": {"outerkey1": {"innerkey1": 1},
#                           "outerkey2": {"innerkey2": 2}},
#                     "h": subdata
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass13, json_decoded)
#
#         with self.subTest("No error raised when extra data is there because ignore_extra_data is set to True."):
#
#             subdata = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}}
#             }
#
#             data = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}},
#                 "h": subdata,
#                 "i": "extra_data"
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(
#                 TestDataClass14,
#                 json_decoded,
#                 ignore_extra_data=True
#             )
#
#         with self.subTest("No error raised when extra data is there because ignore_extra_data is set to True."):
#
#             subdata = {
#                 "a": 1,
#                 "b": 2.2,
#                 "c": "value",
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}}
#             }
#
#             data = {
#                 "a": 1,
#                 "b": "2.2",
#                 "c": 9874567,
#                 "d": True,
#                 "e": 123,
#                 "f": [[1, 2, 3], [4, 5, 6]],
#                 "g": {"outerkey1": {"innerkey1": 1},
#                       "outerkey2": {"innerkey2": 2}},
#                 "h": subdata,
#                 "i": "extra_data"
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(
#                 TestDataClass14,
#                 json_decoded,
#                 ignore_extra_data=True,
#                 enforce_types=False
#             )
#
#         with self.subTest("No error raised when extra data is there because ignore_extra_data is set to True."
#                           "No error raised for wrong types."
#                           "Error raised for key being uppercase instead of lowercase."):
#             with self.assertRaises(KeyError):
#                 subdata = {
#                     "a": 1,
#                     "b": 2.2,
#                     "c": "value",
#                     "d": True,
#                     "e": 123,
#                     "f": [[1, 2, 3], [4, 5, 6]],
#                     "g": {"outerkey1": {"innerkey1": 1},
#                           "outerkey2": {"innerkey2": 2}}
#                 }
#
#                 data = {
#                     "a": 1,
#                     "B": "2.2",
#                     "c": 9874567,
#                     "d": True,
#                     "e": 123,
#                     "f": [[1, 2, 3], [4, 5, 6]],
#                     "g": {"outerkey1": {"innerkey1": 1},
#                           "outerkey2": {"innerkey2": 2}},
#                     "h": subdata,
#                     "i": "extra_data"
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(
#                     TestDataClass14,
#                     json_decoded,
#                     ignore_extra_data=True,
#                     enforce_types=False,
#                     case_sensitive=True
#                 )
#
#         with self.subTest(""):
#             data = {
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(
#                 TestDataClass15,
#                 json_decoded,
#                 case_sensitive=False
#             )
#
#     def test_deserialize_data_improper_usage(self):
#
#         with self.subTest("Class is not dataclass"):
#             with self.assertRaises(CustomError):
#                 data = {}
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 Deserializer().deserialize_data(TestClass, json_decoded)
#
#         with self.subTest("The 'n' field data type is dict but only specified one arg type"):
#             with self.assertRaises(CustomError):
#                 data = {
#                     "n": {"key": 1}
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass17, json_decoded)
#
#         with self.subTest("The 'o' field data type is dict but key arg type is not str"):
#             with self.assertRaises(CustomError):
#                 data = {
#                     "o": {"key": 1}
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass16, json_decoded)