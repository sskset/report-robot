import unittest
from verify_code import *


class TestVerifyCode(unittest.TestCase):

    def test_get_string_from_image(self):
        text = VerifyCode.get_text_from_image_file('../images/code.gif')
        print(text)
        self.assertEqual(text, 'YJGV')


if __name__ == '__main__':
    unittest.main()
