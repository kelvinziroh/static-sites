import unittest

from generate import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """# Hello

This is a test to see if the title will extracted _successfully_!

**Goodbye** World!
"""
        title = extract_title(md)
        self.assertEqual(title, "Hello")


if __name__ == "__main__":
    unittest.main()
