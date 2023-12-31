import unittest
from app.services.index_procesor import InvertedIndexProcessor
import os
import shutil


class TestInvertedIndexProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_directory = 'test_dir'
        os.makedirs(cls.test_directory, exist_ok=True)
        with open(os.path.join(cls.test_directory, 'test1.txt'), 'w', encoding='utf-8') as f:
            f.write('Hello world')
        with open(os.path.join(cls.test_directory, 'test2.txt'), 'w', encoding='utf-8') as f:
            f.write('Another test')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_directory)

    def test_initialization(self):
        processor = InvertedIndexProcessor()
        self.assertEqual(processor.directory, processor.directory)

    def test_check_file_exists(self):
        processor = InvertedIndexProcessor()
        test_file_path = os.path.join(self.test_directory, 'test1.txt')
        self.assertTrue(processor.check_file_exists(test_file_path))
        self.assertFalse(processor.check_file_exists('nonexistent.txt'))


if __name__ == '__main__':
    unittest.main()
