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


    def test_DAGNode(self):
        root = LCA.DAGNode(1)
        self.assertEqual(root.data, 1)

    def test_DAG_insert(self):
        root = LCA.DAGNode(1)
        a = LCA.DAGNode(2)
        b = LCA.DAGNode(3)
        c = LCA.DAGNode(4)
        d = LCA.DAGNode(5)

        root.insert(a)
        root.insert(b)
        b.insert(c)
        b.insert(d)
        
        if (self.assertEqual(root.data, 1) and self.assertEqual(root.children[0], a) and self.assertEqual(root.children[0], b) and self.assertEqual(a.children, [])
            and self.assertEqual(b.children[0], c) and self.assertEqual(b.children[0], d)):
            print("Test for normal DAG insertion ran succesfully")
        else: print("Test for normal DAG insertion failed")

    #no need to test if a node is already occupied as a parents can have as many children, and a child as many parents
    def test_DAGLCA(self):
        root = LCA.DAGNode(1)
        b = LCA.DAGNode(3)
        c = LCA.DAGNode(4)
        d = LCA.DAGNode(5)
        e = LCA.DAGNode(6)
        f = LCA.DAGNode(7)
        g = LCA.DAGNode(8)
        h = LCA.DAGNode(9)
        z = LCA.DAGNode(99)

        root.insert(b)
        root.insert(c)
        root.insert(d)
        b.insert(g)
        b.insert(e)
        c.insert(f)
        g.insert(h)
        e.insert(h)
        f.insert(h)

        self.assertEqual(h.LCA(b, root), b)         #test 2 nodes that are close to each other
        self.assertEqual(h.LCA(d, root), root)      #test when only the root is common
        self.assertEqual(h.LCA(z, root), None)      #test no common

if __name__ == '__main__':
    unittest.main()