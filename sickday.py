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
                "selected_bg" :  (0x00, 0x99, 0xff),
                "selected_text" :  (0xff, 0xff, 0x00),
        }

        self.fonts =  {
                "title" : pygame.font.Font("Sony_Sketch_EF.ttf", 45),
                "footer" : pygame.font.Font("Sony_Sketch_EF.ttf", 20),
                "default" : pygame.font.Font("Sony_Sketch_EF.ttf", 35),
                "menu" : pygame.font.Font("Sony_Sketch_EF.ttf", 35)
        }
        
        self.title_text = ""
        self.footer_text_left = self.vers_str
        self.footer_text_right = "00:00"

        #self.js = pygame.joystick.Joystick(0)
        #self.js.init()

        self.screen = pygame.display.set_mode((800, 600))

        # figure out how big the viewport is
        sample1 = self.fonts["title"].render(
                "test", True, self.colours["text"])
        sample2 = self.fonts["footer"].render(
                "test", True, self.colours["text"])
        sample3 = self.fonts["menu"].render(
                "test", True, self.colours["text"])

        viewport_poss = pygame.Surface((self.screen.get_rect().w,
                    self.screen.get_rect().h - sample1.get_rect().h -
                    sample2.get_rect().h))

        self.n_menu_items = viewport_poss.get_rect().h / sample3.get_rect().h

        self.viewport = pygame.Surface((self.screen.get_rect().w, self.n_menu_items *
            sample3.get_rect().h))

        self.viewport_pos = (0, sample1.get_rect().h + ((viewport_poss.get_rect().h -
                self.viewport.get_rect().h) / 2))

        self.selected_menu_item = 0

    def update_gui(self):

        self.footer_text_right = time.strftime("%a, %d %b %Y %H:%M",
                time.gmtime())
        self.title_text = "test"

        # start drawing
        self.screen.fill(self.colours["bg"])
        self.viewport.fill(self.colours["bg"])

        # render header and footer
        title = self.fonts["title"].render(
                self.title_text, True, self.colours["text"])
        footer_left = self.fonts["footer"].render(
                self.footer_text_left, True, self.colours["text"])
        footer_right = self.fonts["footer"].render(
                self.footer_text_right, True, self.colours["text"])

        self.screen.blit(self.viewport, self.viewport_pos)

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

        self.render_menu()

        pygame.display.flip()

    def render_menu(self):

        items_txt = ["test123", "lalalalalala", "kjhfdkjhfkdsj", "a", "b", "c", "d", "e"];
        items_txt1 = ["test123", "lalalalalala", "kjhfdkjhfkdsj", "a", "b", "c", "d", "e"];
        items_txt.extend(items_txt1)

        items = []
        for i in range(len(items_txt)):
            if i == self.selected_menu_item:
                items.append(self.fonts["title"].render(
                    items_txt[i], True, self.colours["selected_text"]))
            else:
                items.append(self.fonts["title"].render(
                    items_txt[i], True, self.colours["text"]))

        start_item = 0 # XXX scrolling
        for i in range(start_item, len(items)):

            if (self.selected_menu_item == i):
                r = pygame.Rect((0, i * items[i].get_rect().h),
                        (self.screen.get_rect().w, items[i].get_rect().h))
                pygame.draw.rect(self.viewport, self.colours["selected_bg"], r)

            y = self.viewport_pos[1] + (i * items[i].get_rect().h)
            self.screen.blit(items[i], (0, y))

            if (len(items) - start_item - 1) == self.n_menu_items:
                break

    def handle_events(self):
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif e.key == pygame.K_DOWN:
                        self.selected_menu_item = self.selected_menu_item + 1
                    elif e.key == pygame.K_UP:
                        self.selected_menu_item = self.selected_menu_item - 1

    def run(self):

        while True:
            self.handle_events()
            self.update_gui()

if __name__ == "__main__":
    gui = SickGUI()
    gui.run()
