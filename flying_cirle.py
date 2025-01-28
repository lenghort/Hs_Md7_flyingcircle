class Circle:
    def __init__(self, radius, x, y): 
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self): 
        print(f"{self.x}, {self.y}")
    
    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y
    
if __name__ == "__main__":
    c = Circle(20,100,100)
    counter = 0
    game_start = True

    window_width = 100
    window_height = 100
    
    move_x = 1
    move_y = 1

    while game_start:
        c.move(move_x,move_y)
        c.draw()
        counter += 1
        
        if c.x > window_width or c.x < 0:
            move_x = -move_x

        if c.y > window_height or c.y < 0:
            move_y = -move_y
        
        if counter >= 1000:
            break