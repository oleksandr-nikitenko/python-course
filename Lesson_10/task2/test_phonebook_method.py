import os
import unittest
from phonebook_methods import get_json_object, get_field, update, delete


class TestPhonebookMethods(unittest.TestCase):
    
    def setUp(self) -> None:
        self.test_file_path = 'test_phonebook_db.json'
        text = '{"+380630000000": {"first_name": "John", "last_name": "Smithson","full_name": "John Smithson",' \
               '"country": "Ukraine", "city": "NY"}}'
        with open(self.test_file_path, 'w') as file:
            file.write(text + '\n')
    
    def tearDown(self) -> None:
        os.remove(self.test_file_path)
    
    def test_get_object_json_object(self):
        self.assertIsInstance(get_json_object(), dict)
        with self.assertRaises(FileNotFoundError) as d:
            get_json_object('test_phonebook_db1.json')
           
    def test_get_field(self):
        self.assertIsInstance(get_field(get_json_object()), list)
        with self.assertRaises(TypeError):
            get_field(1)
    
    def test_update(self):
        self.assertTrue(update({}, {}, None, self.test_file_path))
        with self.assertRaises(TypeError):
            update('', {}, None, self.test_file_path)
            update({}, '', None, self.test_file_path)
            update('', '', None, self.test_file_path)
    
    def test_delete(self):
        self.assertTrue(delete(get_json_object(self.test_file_path), '+380630000000', self.test_file_path))
        with self.assertRaises(TypeError):
            delete([], '+380630000000', self.test_file_path)
        with self.assertRaises(KeyError):
            delete(get_json_object(self.test_file_path), '1', self.test_file_path)