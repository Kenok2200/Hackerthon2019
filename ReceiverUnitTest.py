import unittest

from Receiver import Receiver


class ReceiverUnitTest(unittest.TestCase):

    def test_receiver_getter(self):
        foo = Receiver()
        self.assertEqual(foo.get_signal(), 0)

    def test_receiver_setter(self):
        foo = Receiver()
        foo.set_signal(1)
        self.assertEqual(foo.get_signal(), 1)

    def main(self):
        self.test_receiver_getter()
        self.test_receiver_setter()


if __name__ == '__main__':
    unittest.main()
