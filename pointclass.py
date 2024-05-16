from Player_Class import Player, Point_List

class point(Player):
    def __init__(self,x,y,num):
        Player.__init__(self,x,y)
        Point_List.append(self)
        self.num = num
        self.count = 0
    def act(self):
        if self.count == 5:
            Point_List.remove(self)
        self.count += 1
