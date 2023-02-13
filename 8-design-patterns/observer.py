# Observer pattern aka PubSub pattern
# Widely used beyond just OOP, also in distributed systems

class YoutubeChannel:
    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = []
    
    def subscribe(self, sub):
        self.subscribers.append(sub)