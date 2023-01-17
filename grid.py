from typing import Optional

from general import Renderable
from settings import settings
import pygame as pg

from game import Game


class Cell(Renderable):

    SIZE:int = settings.cell.SIZE
    BORDER_RADIUS = settings.cell.BORDER_RADIUS

    def __init__(self, left:int, top:int):
        self._game  = Game()
        self._left  = left
        self._top   = top
        self._rect: Optional[pg.Rect]  = None
        self._background_color:pg.Color = pg.Color('darkorange')

    @property
    def background_color(self) -> pg.Color:
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = pg.Color(value)

    @property
    def left(self):
        return self._left

    @property
    def top(self):
        return  self._top

    def draw(self):
        box = self.left * Cell.SIZE, self.top * Cell.SIZE, Cell.SIZE, Cell.SIZE
        self._rect = pg.draw.rect(self._game.screen, self.background_color, box, border_radius=Cell.BORDER_RADIUS)

    def update(self):
        pass

    def __repr__(self):
        return f"{Cell.__name__} ({self.top},{self.left})"

class GridRow(Renderable):

    WIDTH:int  = settings.grid.WIDTH

    def __init__(self, top:int, Cell=Cell):
        self._top = top
        self._items:list[Cell] = [Cell(left, top) for left in range(GridRow.WIDTH)]


    def __getitem__(self, item):
        return self._items[item]

    def update(self):
        pass

    def draw(self):
        for item in self._items:
            item.draw()

    def __len__(self):
        return len(self._items)


class Grid(Renderable):
    HEIGHT: int = settings.grid.HEIGHT

    def __init__(self, Row=GridRow):
        self._items: list[Row] = [Row(top) for top in range(Grid.HEIGHT)]

    def update(self):
        pass

    def draw(self):
        for item in self._items:
            item.draw()

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)
