from textnode import TextNode, TextType

print("Hello World")

def main():
    """Create a TextNode instance with dummy data and print it."""
    node = TextNode(text="Hello, World!", text_type=TextType.PLAIN, url="https://boot.dev")
    print(node)

if __name__ == "__main__":
    main()
