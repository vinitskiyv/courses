import unittest
from main import hello_world, module_name


class TestHelloWorld(unittest.TestCase):

    def test_print_hello_world(self):
        self.assertIsNone(hello_world(), 'Function must return None')

    def test_module_name(self):
        self.assertEqual(module_name(), '__main__')


if __name__ == '__main__':
    unittest.main()
