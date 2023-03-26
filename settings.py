from pydantic import BaseModel

class Display(BaseModel):
    WIDTH:int = 1920 //2
    HEIGHT:int = 1000

class Cell(BaseModel):
    SIZE: int = 50
    BORDER_RADIUS: int = SIZE // 5
    WALL_COLOR = "black"
    SPACE_COLOR = "white"
    COLOR_OF_VISITED = "gray"
    READY_TO_VISIT_COLOR = "yellow"
    ROUTE_COLOR = "green"

class Grid(BaseModel):
    WIDTH: int
    HEIGHT: int
    WALL_PERCENT:int = 20

class Settings(BaseModel):
    FPS:int = 20
    display: Display = Display()
    cell: Cell = Cell()
    grid = Grid(**{"WIDTH": display.WIDTH // cell.SIZE, "HEIGHT": display.HEIGHT // cell.SIZE})

settings = Settings()
