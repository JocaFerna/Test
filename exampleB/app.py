from event_bus import event_bus
from listeners.listener_a import ListenerA
from listeners.listener_b import ListenerB

def main():
    listener_a = ListenerA()
    listener_b = ListenerB()

    event_bus.subscribe("event_type_1", listener_a)
    event_bus.subscribe("event_type_1", listener_b)

    # Emitting an event
    event_bus.emit("event_type_1", "Event Data")

if __name__ == "__main__":
    main()