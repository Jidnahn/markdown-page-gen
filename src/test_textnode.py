import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        node3 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node4 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node6 = TextNode("This is a text node", TextType.ITALIC, "https://www.google.com")
        self.assertNotEqual(node5, node6)
        
        
if __name__ == "__main__":
    unittest.main()
        