import unittest
import day18


class testDay18(unittest.TestCase):
    def test_something(self):
        sfn = day18.convert_list_to_snailfish([2, 5])
        self.assertEqual(sfn.magnitude(), 16)

        sfn = day18.convert_list_to_snailfish([10, 10])
        sfn.reset()
        sfn.split()

        self.assertEqual(sfn.inorderTraversal(), [[5, 5], 10])
        sfn.reset()
        sfn.split()
        self.assertEqual(sfn.inorderTraversal(), [[5, 5], [5, 5]])

        sfn = day18.convert_list_to_snailfish([[[[[9,8],1],2],3],4])
        sfn.reset()
        sfn.explode()
        self.assertEqual(sfn.inorderTraversal(),[[[[0, 9], 2], 3], 4])
        self.assertEqual(sfn.magnitude(), 548)




if __name__ == '__main__':
    unittest.main()
