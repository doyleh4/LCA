
#include <iostream>
#include <stdlib.h>     /* srand, rand */
#include <vector>       //used for vectors essentially an arraylist
using namespace std;
#define COUNT 1

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
    struct Node* parent;

    Node(int a) {
        data = a;
        left = NULL;
        right = NULL;
        parent = NULL;
    }

    void insert(Node* a) {
        int r = rand() % 2 + 1;             //randomising the creation of tree
        if (r == 1) {
            if (this->left == NULL) {
                this->left = a;
                a->parent = this;
            }
            else {
                this->left->insert(a);
            }
        }
        else {
            if (this->right == NULL) {
                this->right = a;
                a->parent = this;
            }
            else {
                this->right->insert(a);
            }
        }

    }

    void LowestCommonAncestor(Node* a, Node* b) {
        std::vector<int> ancestoryA = { };
        std::vector<int> ancestoryB = { };
        bool ancestoryDiscovered = false;
        struct Node* thisNode = a;
        while (!ancestoryDiscovered) {
            if (thisNode->parent != NULL) {
                ancestoryA.push_back(thisNode->data);
                thisNode = thisNode->parent;
            }
            else {
                ancestoryA.push_back(thisNode->data);
                ancestoryDiscovered = true;
            }
        }
        thisNode = b;
        ancestoryDiscovered = false;
        while (!ancestoryDiscovered) {
            if (thisNode->parent != NULL) {
                ancestoryB.push_back(thisNode->data);
                thisNode = thisNode->parent;
            }
            else {
                ancestoryB.push_back(thisNode->data);
                ancestoryDiscovered = true;
            }
        }

        for (int i : ancestoryA) {
            for (int j : ancestoryB) {
                if (i == j) {
                    cout << "The LCA between " << a->data << " and " << b->data << " is " << i;
                    return;
                }
            }
        }
    }
};

void printTree(Node* root, int space) { //got from https://www.tutorialspoint.com/print-binary-tree-in-2-dimensions-in-cplusplus
    if (root == NULL)
        return;
    space += COUNT;
    printTree(root->right, space);
    for (int i = COUNT; i < space; i++)
        cout << "\t";
    cout << root->data << "\n";
    printTree(root->left, space);
}

int main() {
    struct Node* root = new Node(1);
    struct Node* a = new Node(2);
    struct Node* b = new Node(3);
    struct Node* c = new Node(4);
    struct Node* d = new Node(5);
    struct Node* e = new Node(6);
    struct Node* f = new Node(7);
    struct Node* g = new Node(8);
    struct Node* h = new Node(9);
    struct Node* i = new Node(10);
    struct Node* j = new Node(11);
    struct Node* k = new Node(12);
    struct Node* l = new Node(13);
    struct Node* m = new Node(14);
    struct Node* n = new Node(15);
    struct Node* o = new Node(16);
    root->insert(a);
    root->insert(b);
    root->insert(c);
    root->insert(d);
    root->insert(e);
    root->insert(f);
    root->insert(g);
    root->insert(h);
    root->insert(i);
    root->insert(j);
    root->insert(k);
    root->insert(l);
    root->insert(m);
    root->insert(n);
    root->insert(o);



    printTree(root, 0);
    root->LowestCommonAncestor(k, l);
}