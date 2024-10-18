import unittest
from layers.presentation_layer import PresentationLayer

class TestLayeredArchitecture(unittest.TestCase):
    def test_presentation_layer(self):
        presentation = PresentationLayer()
        presentation.run()  # Should print processed data

if __name__ == "__main__":
    unittest.main()