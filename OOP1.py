import pygame

class Laptop():
    def __init__(self, brand, CPU, RAM, storage, price, owner):
        self.brand = brand
        self.CPU = CPU
        self.RAM = RAM
        self.storage = storage
        self.price = price
        self.owner = owner
        self.image = pygame.image.load("img/laptop.jpg")

    # Object / Clone methods
    def output_specs(self):
        print(self.brand, self.CPU, self.RAM, self.storage, self.price)
        print("A property of " + self.owner)

    def render_image(self, surface):
        surface.blit(self.image, (0, 0))



# Create a clone
kisho_laptop = Laptop("Apple", "M1", 16, 512, 2200, "Kavin Kisho")
kingsley_laptop = Laptop("LG", "AMD-Ryzen", 32, 1000, 3600, "Kingsley Tan")


kisho_laptop.output_specs()
kingsley_laptop.output_specs()

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


############### MAIN GAME LOOP ####################
run = True
while run:
    clock.tick(FPS)

    kisho_laptop.render_image(screen)

    # Event handler to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Update display window in every frame
    pygame.display.update()


pygame.quit()