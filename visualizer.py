import pygame
import random
pygame.init()


class DrawInformation:
    # init different color for GUI appearance 
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    # Gradients: Stores the different colors for the bars, representing the numbers, to make a single number representation more clear
    GRADIENT = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

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


def draw(draw_info):
    # clear the screen
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    # draw list
    draw_list(draw_info)

    # update the screen and show everything, which has been drawn before
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst
    # iterate over the vale and index of the items in list 
    for i, val in enumerate(lst):

        # calculate x value of the bar (bottom left corner)
        x = draw_info.start_x + i * draw_info.bar_width
        # calculate the y value of the bar (from top hand corner to bottom left hand corner)
        y = draw_info.height - (val - draw_info.min_val) * draw_info.bar_height
        
        # determine the color of the bar (grey -> light grey -> dark grey -> grey -> ...)
        color = draw_info.GRADIENT[i % 3]

        # we can use the height, because everything over the max. height is "underneath" the screen and will just be cut off
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.bar_width, draw_info.height))


def generate_starting_list(length, min_val, max_val):
    lst = []
    # calculate the random numbers for the list and insert them into the list
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

        draw(draw_info)

        # handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    pygame.quit()

if __name__ == "__main__":
    main()
