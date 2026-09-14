# exercise 06: I brought up this question because I found it different from the others.
class Television:
    def __init__(self,min_channel,max_channel,channel = 2):
        self.on = True
        self.channel = channel
        self.min_channel = min_channel
        self.max_channel = max_channel

    def change_to_up(self):
        if self.channel  <  self.max_channel:
            self.channel += 1
        else:
            self.channel = self.min_channel
        return self.channel

    def change_to_down(self):
        if self.channel  >  self.min_channel:
            self.channel -= 1
        else:
            self.channel = self.max_channel
        return self.channel
        

tv = Television(1,10)


for x in range(0,100):
    up = tv.change_to_up()
    print(up)


for x in range(0,100):
    down = tv.change_to_down()
    print(down)




print(tv.channel)

