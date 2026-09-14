# exercise 03
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

    def change_to_down(self):
        if self.channel  >  self.min_channel:
            self.channel -= 1
        else:
            self.channel = self.max_channel
        

tv = Television(1,100)


for x in range(0,1000):
    tv.change_to_up()
    print(tv.channel)

for x in range(0,1000):
    tv.change_to_down()
    print(tv.channel)



print(tv.channel)

