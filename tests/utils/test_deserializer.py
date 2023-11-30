# import unittest
# from webapp.webapp.utils.deserializer import Deserializer
# from dataclasses import dataclass
# import json
#
#
# @dataclass
# class TestDataClass:
#     a: str
#     b: int
#     c: str
#     d: int
#     e: str
#     f: str
#
#     def __post_init__(self):
#         self.test_a_validation()
#
#     def test_a_validation(self):
#         self.a = "test"
#
#
# @dataclass
# class TestDataClass3:
#     h: int
#
#
# @dataclass
# class TestSubDataClass2:
#     b: list[int]
#     c: list[int]
#
#
# @dataclass
# class TestDataClass2:
#     a: TestSubDataClass2
#
#
# class TestClass:
#     pass
#
#
# @dataclass
# class TestDataClass4:
#     h: list[int]
#     k: list[list[str]]
#
#
# @dataclass
# class TestDataClass5:
#     j: list[TestDataClass3]
#     l: list[list[TestDataClass3]]
#
#
# @dataclass
# class TestDataClass6:
#     m: any
#
#
# @dataclass
# class TestDataClass7:
#     n: dict[int]
#
#
# @dataclass
# class TestDataClass8:
#     o: dict[int, int]
#
#
# @dataclass
# class TestDataClass9:
#     p: dict[str, int]
#
#
# @dataclass
# class TestDataClass10:
#     q: list[dict[str, int]]
#
#
# @dataclass
# class TestDataClass11:
#     r: dict[int, str]
#
#
# class TestDeserializer(unittest.TestCase):
#
#     def test_deserialize_data(self):
#
#         with self.subTest("Data missing 'a' field"):
#             with self.assertRaises(KeyError):
#                 data = {
#                     "b": 1,
#                     "c": "value1",
#                     "d": 2,
#                     "e": "value2",
#                     "f": "value3",
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 Deserializer().deserialize_data(TestDataClass, json_decoded)
#
#         with self.subTest("The 'a' field data type is wrong"):
#             with self.assertRaises(TypeError):
#                 data = {
#                     "a": 0,
#                     "b": 1,
#                     "c": "value1",
#                     "d": 2,
#                     "e": "value2",
#                     "f": "value3",
#                 }
#
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 Deserializer().deserialize_data(TestDataClass, json_decoded)
#
#         with self.subTest("The 'a' field data type is nested and wrong"):
#             with self.assertRaises(TypeError):
#                 data = {
#                     "a": {"b": [1, 2, 3],
#                           "c": [4, 5, "6"]
#                           }
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 Deserializer().deserialize_data(TestDataClass2, json_decoded)
#
#         with self.subTest("The 'a' field data type is nested and correct"):
#             data = {
#                 "a": {"b": [1, 2, 3],
#                       "c": [4, 5, 6]
#                       }
#             }
#
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass2, json_decoded)
#             self.assertEqual(deserialized_object.a, TestSubDataClass2(b=[1, 2, 3], c=[4, 5, 6]))
#
#         with self.subTest("The 'a' field data type is nested and has extra data"):
#             with self.assertRaises(KeyError):
#                 data = {
#                     "a": {"b": [1, 2, 3],
#                           "c": [4, 5, 6],
#                           "d": [7, 8, 9]
#                           }
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass2, json_decoded)
#
#         with self.subTest("The 'a' field data type is nested and is missing data"):
#             with self.assertRaises(KeyError):
#                 data = {
#                     "a": {"b": [1, 2, 3]
#                           }
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass2, json_decoded)
#
#         with self.subTest("The 'a' field data type is nested and has wrong type but is dataclass"):
#             with self.assertRaises(TypeError):
#                 data = {
#                     "a": {"b": [1, 2, 3],
#                           "c": TestDataClass3(h=4)
#                           }
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass2, json_decoded)
#
#         with self.subTest("The a field data type is nested and has wrong type and is not dataclass"):
#             with self.assertRaises(TypeError):
#                 data = {
#                     "a": {"b": [1, 2, 3],
#                           "c": TestClass()
#                           }
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass2, json_decoded)
#
#         with self.subTest("The 'p' field data type is dict and is correct"):
#             data = {
#                 "p": {"key": 1}
#             }
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass9, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass9(**data))
#
#         with self.subTest("The 'q' field data type is list of dict and is correct"):
#             data = {
#                 "q": [{"key": 1, "key2": 2}, {"key3": 3, "key4": 4}]
#             }
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass10, json_decoded)
#             self.assertEqual(deserialized_object, TestDataClass10(**data))
#
#         with self.subTest("The 'q' field data type is list of dict and one value type is incorrect"):
#             with self.assertRaises(TypeError):
#                 data = {
#                     "q": [{"key": 1, "key2": 2}, {"key3": 3, "key4": "4"}]
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass10, json_decoded)
#                 self.assertEqual(deserialized_object, TestDataClass10(**data))
#
#         with self.subTest("There is extra data"):
#             with self.assertRaises(KeyError):
#                 data = {
#                     "a": "value0",
#                     "b": 1,
#                     "c": "value1",
#                     "d": 2,
#                     "e": "value2",
#                     "f": "value3",
#                     "g": 4
#                 }
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 Deserializer().deserialize_data(TestDataClass, json_decoded)
#
#         with self.subTest("Check __post_init()__ validator runs"):
#             data = {
#                 "a": "value0",
#                 "b": 1,
#                 "c": "value1",
#                 "d": 2,
#                 "e": "value2",
#                 "f": "value3",
#             }
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass, json_decoded)
#
#             self.assertEqual(deserialized_object.a, "test")
#
#         with self.subTest("The h field data type is list of int and k is list[list[str]]"):
#             data = {"h": [1, 2, 3],
#                     "k": [["4", "5", "6"],
#                           ["7", "8", "9"]]}
#             json_object = json.dumps(data)
#             json_decoded = json.loads(json_object)
#             deserialized_object = Deserializer().deserialize_data(TestDataClass4, json_decoded)
#
#         with self.subTest("The h field data type is list of int and k is list[list[str]] but bad input"):
#             with self.assertRaises(TypeError):
#                 data = {"h": [1, 2, 3],
#                         "k": [["4", "5", "6"],
#                               ["7", "8", "9"],
#                               0,
#                               ]}
#                 json_object = json.dumps(data)
#                 json_decoded = json.loads(json_object)
#                 deserialized_object = Deserializer().deserialize_data(TestDataClass4, json_decoded)
