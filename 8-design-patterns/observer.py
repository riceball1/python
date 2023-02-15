# Observer pattern aka PubSub pattern
# Widely used beyond just OOP, also in distributed systems
# e.g. uploading a video on Youtube notifies subscribers to be notified of the new video

class YoutubeChannel:
    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = []
    
    # adds new new subscriber
    def subscribe(self, sub):
        self.subscribers.append(sub)

    # sends notification
    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)

# define a subscriber interface, which can be done with an abstract class or an interface

from abc import ABC, abstractmethod

class YoutubeSuscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass

# different users may implemement notification differently

class YoutubeUser(YoutubeSuscriber):
    def __init__(self, name) -> None:
        self.name = name
    
    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel}: {event}")

# create a Youtube channel
channel = YoutubeChannel("neetcode")

# add subscribers
channel.subscribe(YoutubeUser("sub1"))
channel.subscribe(YoutubeUser("sub2"))
channel.subscribe(YoutubeUser("sub3"))

# then call notify once and all subscribers will receive notification
channel.notify("A new video released")

# User sub1 received notification from neetcode: A new video released
# User sub2 received notification from neetcode: A new video released
# User sub3 received notification from neetcode: A new video released