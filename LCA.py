import random

class Node: #used https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm as a template
    def __init__(self,data):    #to create a new tree essentially this is the very first node
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insertRandom(self, data): #if you do not specify left or right node will be inserted randomly
        if self.data:
            n = random.randint(1,2) #using a random int to add the data to the tree radnomly
            if n == 1:
                if self.left is None:
                    self.left = data
                    data.parent = self
                else: self.left.insertRandom(data)
            else:
                if self.right is None:
                    self.right = data
                    data.parent = self
                else: self.right.insertRandom(data)
        else:
            self.data = self

    def insert(self, child, x): #x is left or right child
        if x == "left":
            if self.left is None:
                self.left = child
                child.parent = self
            #else:
                 #print("Node could not be added as there is already a left child")
        elif x == "right":
            if self.right is None:
                self.right = child
                child.parent = self
            #else:
                 #print("Node could not be added as there is already a right child")
        #else: print("Parameter not regognised")


    def display(self): #got display from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python used to check if LCA answer is right
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def LowestCommonAncestor(self, a, b): 
        
        ancestoryA = []
        ancestoryB = []
        ancestoryDiscovered = False
        thisNode = a
        while ancestoryDiscovered is not True:
            if thisNode.parent is not None:
                ancestoryA.append(thisNode.data)
                thisNode = thisNode.parent
            else:
                ancestoryA.append(thisNode.data)
                ancestoryDiscovered = True
        thisNode = b
        ancestoryDiscovered = False
        while ancestoryDiscovered is not True:
            if thisNode.parent is not None:
                ancestoryB.append(thisNode.data)
                thisNode = thisNode.parent
            else:
                ancestoryB.append(thisNode.data)
                ancestoryDiscovered = True
        for i in ancestoryA:
            for h in ancestoryB:
                if i == h:
                    #print ("The LCA between " + str(a.data) + " and " + str(b.data) + " is " + str(i))
                    return int(i)

