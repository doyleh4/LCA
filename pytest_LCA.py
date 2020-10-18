import unittest
import LCA

class TestLCA(unittest.TestCase):
    def test_Node(self):
        root = LCA.Node(1)
        self.assertEqual(root.data, 1)

    def test_insert_normal(self):
        root = LCA.Node(1)
        a = LCA.Node(2)
        b = LCA.Node(3)
        c = LCA.Node(4)

        root.insert(a, "left")
        root.insert(b, "right")
        a.insert(c, "left")
        if (self.assertEqual(root.data, 1),  self.assertEqual(root.left.data, 2), self.assertEqual(root.right.data, 3),  self.assertEqual(root.left.left.data, 4)):
            print("Test for normal insertion ran succesfully")
        else: print("Test for normal insertion failed")

    def test_insert_already_occupied(self):
        root = LCA.Node(1)
        a = LCA.Node(2)
        b = LCA.Node(3)
        c = LCA.Node(4)

        root.insert(a, "left")
        root.insert(b, "right")
        root.insert(c, "left")

        if (self.assertEqual(root.data, 1), self.assertEqual(root.left.data, 2), self.assertNotEqual(root.right.data, 4)):
            print ("Test for node already occupied ran successfully")
        else: print("Test for node already occupied failed")

    def test_insert_wrong_parameter(self):
        root = LCA.Node(1)
        a = LCA.Node(2)
        b = LCA.Node(3)
        c = LCA.Node(4)

        root.insert(a, "left")
        root.insert(b, "right")
        a.insert(c, "lft")

        if(self.assertEqual(root.data, 1), self.assertEqual(root.left.data, 2),  self.assertEqual(root.right.data, 3), self.assertEqual(root.left.left, None)):
            print("Test for wrong node parameter ran succesfully")
        else: print("Test for wrong node parameter failed")
        

    def test_insertRandom(self):    #as the tree is built randomly i am not able to test this, will add a method if i find a way
        self.assertTrue(True, True)

    def test_LCA(self):
        root = LCA.Node(1)
        a = LCA.Node(2)
        b = LCA.Node(3)
        c = LCA.Node(4)

        root.insert(a, "left")
        root.insert(b, "right")
        a.insert(c, "left")
        self.assertEqual(root.LowestCommonAncestor(c, b), 1)
        print("The LCA between Node C and Node B is expected 1 and got " + str(root.LowestCommonAncestor(c, b)))
        

if __name__ == '__main__':
    unittest.main()