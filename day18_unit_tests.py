import unittest
import day18


class testDay18(unittest.TestCase):
    def test_something(self):
        sfn1 = day18.convert_list_to_snailfish([2, 5])
        self.assertEqual(sfn1.magnitude(), 16)
        sfn1 = day18.convert_list_to_snailfish([10, 10])
        sfn1.split()
        self.assertEqual(sfn1.inorderTraversal(), [[5, 5], 10])
        sfn1.reset()
        sfn1.split()
        self.assertEqual(sfn1.inorderTraversal(), [[5, 5], [5, 5]])


if __name__ == '__main__':
    unittest.main()
