from typing import Optional

import pygame as pg

from general import Frame, Singleton
from settings import settings

from pydantic import BaseModel

class Game(metaclass=Singleton):

    def __init__(self):
        pg.init()

        window_size = (settings.display.WIDTH, settings.display.HEIGHT)

        self._fps = settings.FPS
        self._is_running:bool = False
        self._screen = pg.display.set_mode(window_size)
        self._clock = pg.time.Clock()
        self._current_frame: Optional[Frame] = None
        self._keys = {pg.K_PAUSE:False}

    @property
    def keys(self):
        return self._keys

    @property
    def fps(self):
        return self._fps

    @property
    def clock(self):
        return self._clock

    @property
    def is_running(self):
        return self._is_running


    @property
    def screen(self):
        return self._screen

    @property
    def current_frame(self):
        return self._current_frame

    @current_frame.setter
    def current_frame(self, value:Frame):
        self._current_frame = value

    def start(self):
        if not self.current_frame:
            raise "Current frame is not set"

        self._is_running = True
        self._loop()

    def stop(self):
        self._is_running = False


    def _loop(self):

        while self.is_running:

            self.clock.tick(self.fps)
            pg.display.flip()
            self._check_events()

            if not self.keys[pg.K_PAUSE]:
                self.current_frame.display()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.stop()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_PAUSE:
                   self._keys[pg.K_PAUSE] = not self._keys[pg.K_PAUSE]














