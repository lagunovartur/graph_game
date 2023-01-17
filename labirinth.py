import enum
from random import random
from typing import Set, Dict

from general import Frame
from settings import settings
from grid import Grid, GridRow, Cell
from collections import deque

class LabirinthCell(Cell):

    WALL_COLOR  = settings.cell.WALL_COLOR
    SPACE_COLOR = settings.cell.SPACE_COLOR
    READY_TO_VISIT_COLOR = settings.cell.READY_TO_VISIT_COLOR
    COLOR_OF_VISITED = settings.cell.COLOR_OF_VISITED
    ROUTE_COLOR = settings.cell.ROUTE_COLOR


    def __init__(self, left: int, top: int):
        super().__init__(left, top)
        self._is_wall:bool = False
        self._is_visited:bool = False
        self._is_ready_to_visit: bool = False
        self._is_route:bool = False

    @property
    def is_route(self):
        return self._is_route

    @is_route.setter
    def is_route(self, value:bool):
        self.background_color = LabirinthCell.ROUTE_COLOR if value else LabirinthCell.COLOR_OF_VISITED
        self._is_route = value


    @property
    def is_visited(self):
        return self._is_visited

    @is_visited.setter
    def is_visited(self, value: bool):
        if value:
            self.background_color = LabirinthCell.COLOR_OF_VISITED
        self._is_visited = value

    @property
    def is_ready_to_visit(self):
        return self._is_ready_to_visit

    @is_ready_to_visit.setter
    def is_ready_to_visit(self, value: bool):
        self.background_color = LabirinthCell.READY_TO_VISIT_COLOR if value else LabirinthCell.COLOR_OF_VISITED
        self._is_ready_to_visit = value

    @property
    def is_wall(self):
        return self._is_wall

    @is_wall.setter
    def is_wall(self, value:bool):
        self.background_color = LabirinthCell.WALL_COLOR if value else LabirinthCell.SPACE_COLOR
        self._is_wall = value

class LabirinthGridRow(GridRow):

    def __init__(self, top: int):
        super().__init__(top, LabirinthCell)


class LabirinthGrid(Grid):

    WALL_PERCENT:int = settings.grid.WALL_PERCENT

    def __init__(self):
        super().__init__(LabirinthGridRow)
        self._edges: Dict[LabirinthCell, Set[LabirinthCell]] = dict()
        self.set_random_walls(LabirinthGrid.WALL_PERCENT)
        self.update_edges()

        self[0][0].is_visited = True
        self._queue: deque[LabirinthCell] = deque([self[0][0]])
        self._route: Dict[LabirinthCell, LabirinthCell | None] = {self[0][0]:None}
        self._current_route: set[LabirinthCell] = set()
        self._route_generator = self.route_generator()

    def set_random_walls(self, wall_percent:float):
        for top in range(len(self)):
            for left in range(len(self[top])):
                cell = self[top][left]
                cell.is_wall = random() < wall_percent / 100


    def get_neighbors(self, cell: LabirinthCell) -> Set[LabirinthCell]:

        check_neigbor = lambda top, left: (0 <= top < len(self)) \
           and (0 <= left < len(self[top])) and (not self[top][left].is_wall)

        ways = (-1,0), (0,-1), (1,0), (0,1)

        return  {
            self[cell.top + dtop][cell.left + dleft] \
                for dleft, dtop in ways if check_neigbor(cell.top + dtop, cell.left + dleft)
        }

    def update_edges(self):
        for top, row in enumerate(self):
            for left, cell in enumerate(row):
                if not cell.is_wall:
                    self._edges[cell] = self._edges.get(cell,set()).union(self.get_neighbors(cell))

    def route_generator(self):

        while self._queue:

            cur_vertex = self._queue.popleft()
            neighbors = self._edges[cur_vertex]

            cur_vertex.is_ready_to_visit = False

            for neighbor in neighbors:
                if not neighbor.is_visited:

                    self._queue.append(neighbor)
                    self._route[neighbor] = cur_vertex

                    neighbor.is_visited = True
                    neighbor.is_ready_to_visit = True

            yield cur_vertex

    def clear_previous_route(self):
        while self._current_route:
            cell = self._current_route.pop()
            if cell:
                cell.is_route = False

    def update_current_route(self, vertex:LabirinthCell):

        path_segment = vertex
        while path_segment:
            path_segment.is_route = True
            self._current_route.add(path_segment)
            path_segment = self._route[path_segment]

    def draw(self):

        super().draw()

        self.clear_previous_route()
        try:
            next_vertex = self._route_generator.__next__()
        except StopIteration:
            pass
        self.update_current_route(next_vertex)

class LabirinthFrame(Frame):

    SPACE_COLOR = settings.cell.SPACE_COLOR

    def __init__(self):
        self._grid = LabirinthGrid()


    @property
    def grid(self)->LabirinthGrid:
        return self._grid

    def display(self):
        self.grid.draw()






