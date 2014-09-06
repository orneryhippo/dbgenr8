#test the message class
__author__ = 'jesse'

import unittest,message


class MyTestCase(unittest.TestCase):
    def test_existence(self):
        msg=message.Message()

    def test_msg_text(self):
        msg=message.Message("Hello")
        self.assertEqual('Hello',msg.text)
    def test_msg_kwargs(self):
        msg=message.Message("Hello",k='v',v='k')
        self.assertEqual('Hello',msg.text)
        self.assertEqual({'k':'v','v':'k'},msg.entries)



if __name__ == '__main__':
    unittest.main()
