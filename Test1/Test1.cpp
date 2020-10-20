#include "pch.h"
#include "CppUnitTest.h"
#include "../LCA/LCA.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace Test1
{
	TEST_CLASS(Test1)
	{
	public:
		
		TEST_METHOD(Testconstructor)
		{
			Node* root = new Node(0);
			Assert::AreEqual(root->data , 0);
			Assert::IsNull(root->left);
			Assert::IsNull(root->right);
		}

		TEST_METHOD(TestInsert) {
			//Test normal insert
			Node* root = new Node(0);
			Node* a = new Node(1);
			root->insert(a, "left");
			Node* b = new Node(2);
			root->insert(b, "right");
			Assert::AreEqual(root->left->data, 1);
			Assert::AreEqual(root->right->data, 2);
			//Test error control
			Node* c = new Node(5);
			root->insert(c, "left");
			Assert::AreNotEqual(root->left->data, 5);
			root->insert(c, "right");
			Assert::AreNotEqual(root->right->data, 5);
			root->insert(c, "xx");
			Assert::AreNotEqual(root->left->data, 5);
			Assert::AreNotEqual(root->right->data, 5);
		}

		TEST_METHOD(TestBuild) {
			//Test proper building of a tree 
			Node* root = new Node(0);
			Node* a = new Node(1);
			Node* b = new Node(2);
			Node* c = new Node(3);
			Node* d = new Node(4);
			Node* e = new Node(5);
			Node* f = new Node(6);

			root->insert(a, "left");
			root->insert(b, "right");
			a->insert(c, "left");
			a->insert(d, "right");
			b->insert(e, "right");
			d->insert(f, "left");

			Assert::AreEqual(root->left->data, 1);
			Assert::AreEqual(root->right->data, 2);
			Assert::AreEqual(root->left->left->data, 3);
			Assert::AreEqual(root->right->right->data, 5);
			Assert::AreEqual(root->left->right->data, 4);
			Assert::AreEqual(root->left->right->left->data, 6);
		}

		TEST_METHOD(TestRandomInsert) {
			//Havent thought of a way to do this yet
			Assert::IsTrue(true);
		}

		TEST_METHOD(TestLCA) {
			//Test if the LCA is right, uising the same tree as above
			Assert::IsTrue(true);
			Node* root = new Node(0);
			Node* a = new Node(1);
			Node* b = new Node(2);
			Node* c = new Node(3);
			Node* d = new Node(4);
			Node* e = new Node(5);
			Node* f = new Node(6);

			root->insert(a, "left");
			root->insert(b, "right");
			a->insert(c, "left");
			a->insert(d, "right");
			b->insert(e, "right");
			d->insert(f, "left");

			Assert::AreEqual(root->LowestCommonAncestor(e, f), 0); 
			Assert::AreEqual(root->LowestCommonAncestor(d, c), 1);
			Assert::AreEqual(root->LowestCommonAncestor(d, a), 1);
		}
	};
}
