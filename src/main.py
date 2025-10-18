from textnode import TextNode, TextType

print("Hello World")

def main():
    """
    Main entry point for the module.

    Creates a TextNode with the text "Hello, World!", using TextType.PLAIN and the URL
    "https://boot.dev", then prints the resulting node to standard output.

    This function takes no arguments and returns None.

    Side effects:
    - Prints the TextNode representation to stdout.

    Raises:
    - NameError: If TextNode or TextType are not defined in the current scope.
    """
    node = TextNode(text="Hello, World!", text_type=TextType.PLAIN, url="https://boot.dev")
    print(node)

if __name__ == "__main__":
    main()
