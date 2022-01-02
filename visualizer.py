import pygame
import random
pygame.init()


class DrawInformation:
    # init different color for GUI appearance 
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    # defines the total number of pixels we want to have as a padding from the left and right side of the windows
    SIDE_PAD = 100
    
    # defines the padding we have from the top to have space to display the controls
    TOP_PAD = 150
    

    # width and height define the GUI-window dimensions and lst is the starting list which will be sorted
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        # init the GUI with given dimensions
        self.window = pygame.display.set_mode((width, height))
        # window caption
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        # set randomly generated list
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        # we need the max and min value in order to adjust the graphical representation (height, width) of the bars which represent the numbers
        self.min_val = min(lst)
        self.max_val = max(lst)

        # calculate the width of the bars
        self.bar_width = round((self.width - self.SIDE_PAD) / len(lst))
        # calculate the height of an individual bar
        self.bar_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        # calculate the starting point (from the left) on the horizontal x-axes
        self.start_x = self.SIDE_PAD // 2


def generate_starting_list(length, min_val, max_val):
    lst = []

    for _ in range(length):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    run = True
    # pygame Clock do manage loop speed
    clock = pygame.time.Clock()

    # information for the list
    length = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(length, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    # "infinte" loop to handle all the events (rest the visualizer, changing sorting order, ...)
    while(run):
        clock.tick(60)

        pygame.display.update()

        # handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    pygame.quit()

if __name__ == "__main__":
    main()
