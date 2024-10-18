from layers.business_layer import BusinessLayer

class PresentationLayer:
    def __init__(self):
        self.business_layer = BusinessLayer()

    def run(self):
        data = self.business_layer.process_data()
        print(f"Presentation: {data}")