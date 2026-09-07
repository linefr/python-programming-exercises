# exercise 07: Is the TV on or off?
class Television:
    def __init__(self,turn,min_channel,max_channel,channel = 2):
        self.on = turn
        self.channel = channel
        self.min_channel = min_channel
        self.max_channel = max_channel

    def change_to_up(self):
        if self.on:
            if self.channel  <  self.max_channel:
                self.channel += 1
            else:
                self.channel = self.min_channel
            return self.channel

    def change_to_down(self):
        if self.on:
            if self.channel  >  self.min_channel:
                self.channel -= 1
            else:
                self.channel = self.max_channel
            return self.channel
        
while True:
    turn_on_or_off = input("Is the TV on or off?")
    if turn_on_or_off == "on".lower():
        turn_on_or_off = True
        break
    elif turn_on_or_off == "off".lower():
        turn_on_or_off = False
        break
    else:
        continue

tv = Television(turn_on_or_off,1,10)

if tv.on:
    for x in range(0,100):
        up = tv.change_to_up()
        print(up)

    for x in range(0,10):
        down = tv.change_to_down()
        print(down)

print(tv.channel)

