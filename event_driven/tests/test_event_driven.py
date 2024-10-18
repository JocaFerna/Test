import unittest
from event_bus import event_bus
from listeners.listener_a import ListenerA

class TestEventDriven(unittest.TestCase):
    def test_event_emission(self):
        listener_a = ListenerA()
        event_bus.subscribe("event_test", listener_a)
        event_bus.emit("event_test", "Test Data")

if __name__ == "__main__":
    unittest.main()