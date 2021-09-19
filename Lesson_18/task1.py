import unittest
from Lesson_13.task2 import *


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.lib_obj = Library('test name')
    
    def tearDown(self) -> None:
        pass
    
    def test_new_book(self):
        self.assertIsInstance(self.lib_obj.new_book('Kobzar', 1988, Author('Taras', 'Ukraine', '1814')), Book)
        self.assertNotIsInstance(self.lib_obj.new_book('Kobzar', 1988, Author('Taras', 'Ukraine', '1814')), Author)
        with self.assertRaises(TypeError):
            self.lib_obj.new_book(['Kobzar', ], 1988, Author('Taras', 'Ukraine', '1814'))
            self.lib_obj.new_book('Kobzar', '1988', Author('Taras', 'Ukraine', '1814'))
            self.lib_obj.new_book('Kobzar', 1988, self.lib_obj)
    
    def test_group_by_author(self):
        self.assertIsInstance(self.lib_obj.group_by_author(Author('Taras', 'Ukraine', '1814')), list)
        self.assertNotIsInstance(self.lib_obj.group_by_author(Author('Taras', 'Ukraine', '1814')), str)
        with self.assertRaises(TypeError):
            self.lib_obj.group_by_author(Library)
    
    def test_group_by_year(self):
        self.assertIsInstance(self.lib_obj.group_by_year(1988), list)
        self.assertNotIsInstance(self.lib_obj.group_by_year(1988), str)
        with self.assertRaises(TypeError):
            self.lib_obj.group_by_year('1988')
        
            
    
    