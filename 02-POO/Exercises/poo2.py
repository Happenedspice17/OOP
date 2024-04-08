import math
import matplotlib.pyplot as plt

class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self.x_pos = x
        self.y_pos = y

    def set_x(self, x: float) -> None:
        self.x_pos = x
    
    def set_y(self, y: float) -> None:
        self.y_pos = y
    
    def get_x(self) -> float:
        return self.x_pos
    
    def get_y(self) -> float:
        return self.y_pos
    
    def __add__(self, other):
        new_point = Point2D(self.x_pos + other.x_pos, self.y_pos + other.y_pos)
        return new_point

    def __str__(self) -> str:
        return f"({self.x_pos}, {self.y_pos})"


class PlotCosine:
    def __init__(self, num_points: int) -> None:
        self.num_points = num_points
        self.point_list = []
        self.create_points()
    
    def create_points(self) -> None:
        for i in range(self.num_points):
            x = 2 * math.pi * i / self.num_points
            y = math.cos(x)
            self.point_list.append(Point2D(x, y))
    
    def plot_points(self) -> None:
        # Initialize lists for x and y values
        x_values = []
        y_values = []
        # Extract x and y values from each point and append to the respective lists
        for point in self.point_list:
            x_values.append(point.get_x())
            y_values.append(point.get_y())
        # Plot the points
        plt.plot(x_values, y_values)
        plt.show()


class PlotSine(PlotCosine):
    def __super__(self, num_points: int) -> None:
        super().__init__(num_points)
        self.name = "Sine Plot"

    def create_points(self) -> None:
        for i in range(self.num_points):
            x = 2 * math.pi * i / self.num_points
            y = math.sin(x)
            self.point_list.append(Point2D(x, y))

# Create a PlotCosine object with 100 points
cosine_plot = PlotCosine(100)
sine_plot = PlotSine(100)
# Plot the points
cosine_plot.plot_points()
sine_plot.plot_points()

