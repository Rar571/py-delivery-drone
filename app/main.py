from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords=None) -> None:
        self.name = name
        self.weight = weight
        if coords == None:
            coords = [0, 0]
        self.coords = coords

    def go_forward(self, step=1) -> None:
        self.coords[1] += step

    def go_back(self, step=1) -> None:
        self.coords[1] -= step

    def go_right(self, step=1) -> None:
        self.coords[0] += step

    def go_left(self, step=1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name, weight: int, coords=None) -> None:
        super().__init__(name, weight, coords)
        if coords == None:
            self.coords = [0, 0, 0]

    def go_up(self, step=1) -> None:
        self.coords[2] += step

    def go_down(self, step=1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
            coords=None, current_load=None) -> None:
        super().__init__(name, weight, coords)
        if coords == None:
            coords = [0, 0, 0]
        self.coords = coords
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, robot: Cargo) -> None:
        if self.current_load is None and robot.weight <= self.max_load_weight:
            self.current_load = robot
        pass

    def unhook_load(self) -> None:
        self.current_load = None
