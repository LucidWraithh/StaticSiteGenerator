from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

def main():
    node = HTMLNode("Look at me I am a tag", 64, None, {"href": "https://www.google.com", "target": "_blank"})
    leaf = LeafNode("This is a value, normal text will go here", "p")
    leaf2 = LeafNode("This is a test with props added", "q", {"href": "https://google.com"})
    pnode = ParentNode( [
        LeafNode("Bold text", "b"),
        LeafNode("Normal text", None),
        LeafNode("italic text", "i"),
        LeafNode("Normal text", None),
    ],
    "p"
    )  

    print(node)
    print(node.props_to_html())
    print(leaf.to_html())
    print(leaf2.to_html())
    print(pnode)



main()
