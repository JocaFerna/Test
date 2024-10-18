from layers.data_access_layer import DataAccessLayer

class BusinessLayer:
    def __init__(self):
        self.data_access = DataAccessLayer()

    def process_data(self):
        raw_data = self.data_access.get_data()
        processed_data = raw_data.upper()  # Example of processing
        return processed_data