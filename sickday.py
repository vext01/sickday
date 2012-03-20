#!/usr/bin/env python

import sys, pygame, os
import time

class SickGUI:
    def __init__(self):

        pygame.init()
        pygame.font.init()
        pygame.joystick.init()

        self.vers = "0.1"
        self.vers_str = ("SickDay-%s" % self.vers)

        self.colours = {
                "bg" : (0x00, 0x00, 0x00),
                "text" :  (0x00, 0x99, 0xff),
                "lines" :  (0x00, 0x99, 0xff),
        }

        self.fonts =  {
                "title" : pygame.font.Font("Sony_Sketch_EF.ttf", 45),
                "footer" : pygame.font.Font("Sony_Sketch_EF.ttf", 20),
                "default" : pygame.font.Font("Sony_Sketch_EF.ttf", 35)
        }
        
        self.title_text = ""
        self.footer_text_left = self.vers_str
        self.footer_text_right = "00:00"

        #self.js = pygame.joystick.Joystick(0)
        #self.js.init()

        self.screen = pygame.display.set_mode((800, 600))

    def update_gui(self):

        self.footer_text_right = time.strftime("%a, %d %b %Y %H:%M",
                time.gmtime())
        self.title_text = "test"

        # start drawing
        self.screen.fill(self.colours["bg"])

        # render header and footer
        title = self.fonts["title"].render(
                self.title_text, True, self.colours["text"])
        footer_left = self.fonts["footer"].render(
                self.footer_text_left, True, self.colours["text"])
        footer_right = self.fonts["footer"].render(
                self.footer_text_right, True, self.colours["text"])

        # top and bottom lines are always static
        pygame.draw.line(self.screen, self.colours["lines"],
                (0, title.get_rect().h),
                (self.screen.get_rect().w, title.get_rect().h))
        pygame.draw.line(self.screen, self.colours["lines"],
                (0, self.screen.get_rect().h - footer_left.get_rect().h),
                (self.screen.get_rect().w, self.screen.get_rect().h -
                    footer_left.get_rect().h))

        self.screen.blit(title, (0,0))
        self.screen.blit(footer_left, (0, self.screen.get_rect().h -
            footer_left.get_rect().h))
        self.screen.blit(footer_right,(self.screen.get_rect().w -
            footer_right.get_rect().w, self.screen.get_rect().h -
            footer_right.get_rect().h))

        pygame.display.flip()


    def build_menu(self):
        items = ["test123", "lalalalalala", "kjhfdkjhfkdsj"];

    def handle_events(self):
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()

    def run(self):

        while True:

            self.handle_events()
            self.update_gui()

if __name__ == "__main__":
    gui = SickGUI()
    gui.run()