class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if not self.props:
            return ""

        html_props = ""
        for prop in self.props:
            attribute = " " + prop + "=" + self.props[prop]
            html_props += attribute
        
        return html_props
        


    def __repr__(self):
        return f"HTMLNode: Tag = {self.tag}, Value = {self.value}, Children = {self.children}, Props = {self.props}"

class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes require a value")
        elif self.tag:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        return f"{self.value}"

class ParentNode(HTMLNode):

    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided")
        if not self.children:
            raise ValueError("No children provided, this would cause an empty branch")

        html_text = f"<{self.tag}>"
        for child in children:
            html_text += child.to_html()
        
        html_text += f"</{self.tag}>"
        return html_text

