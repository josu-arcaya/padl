# testing
import unittest
import logging

from lint.utils import Padl

class TestOptimizer(unittest.TestCase):

    def setUp(self):
        pipeline_location = 'lint/test/resources/pipeline.yaml'
        with open(pipeline_location, 'r') as input_data_file:
            self.input_pipeline = input_data_file.read()

    def test_padl(self):
        isValid = Padl(self.input_pipeline).validate()

    def test_obj(self):
        Padl(self.input_pipeline).file2obj()


if __name__ == '__main__':
    unittest.main()
