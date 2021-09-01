"""
TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
exists in the list, or "No" - in the other case.
"""


class TVController:
    """ TV controller class"""
    def __init__(self, channels: list) -> None:
        self.CHANNELS = channels
        self.current_channel = 0
    
    def is_exist(self, n: int or str) -> str:
        if type(n) is str:
            result = "Yes" if n in self.CHANNELS else "No"
        elif type(n) is int and n > 0:
            result = "Yes" if n in range(1, len(self.CHANNELS)+1) else "No"
        else:
            result = 'No'
        return result
        
    def first_channel(self):
        self.current_channel = 0
        return self.current_channel_display()
    
    def last_channel(self):
        self.current_channel = len(self.CHANNELS)-1
        return self.current_channel_display()
    
    def turn_channel(self, n):
        if self.is_exist(n) == 'Yes':
            self.current_channel = n - 1
            return self.current_channel_display()
        else:
            return 'Channel not found.'
    
    def next_channel(self):
        if self.current_channel == len(self.CHANNELS)-1:
            self.current_channel = 0
        else:
            self.current_channel += 1
        return self.current_channel_display()
    
    def previous_channel(self):
        if self.current_channel == 0:
            self.current_channel = len(self.CHANNELS)-1
        else:
            self.current_channel -= 1
        return self.current_channel_display()
        
    def current_channel_display(self):
        return self.CHANNELS[self.current_channel]
    
   
CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)
print(controller.first_channel())               # "BBC"
print(controller.last_channel())                # "TV1000"
print(controller.turn_channel(1))               # "BBC"
print(controller.next_channel())                # "Discovery"
print(controller.previous_channel())            # "BBC"
print(controller.current_channel_display())     # "BBC"
print(controller.is_exist(4))                   # "No"
print(controller.is_exist("BBC"))               # "Yes"
