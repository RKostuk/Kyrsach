import unittest
from app.services.index_procesor import InvertedIndexProcessor  # Замініть your_module на назву вашого модуля
import os
import shutil
from collections import defaultdict


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
        processor = InvertedIndexProcessor(self.test_directory)
        self.assertEqual(processor.directory, self.test_directory)

    def test_check_file_exists(self):
        processor = InvertedIndexProcessor(self.test_directory)
        self.assertTrue(processor.check_file_exists(os.path.join(self.test_directory, 'test1.txt')))
        self.assertFalse(processor.check_file_exists('nonexistent.txt'))


if __name__ == '__main__':
    unittest.main()
