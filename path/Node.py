from .Colors import colors

TOTAL_NUM_OF_ROWS = 40
TOTAL_NUM_OF_COLUMNS = 40


class Node:
    def __init__(self, row, column, node_width, color=colors["WHITE"]):
        self.neighbors_nodes = []
        self.row = row
        self.col = column
        self.color = color
        self.x = row * node_width
        self.y = column * node_width

    def is_visited_node(self):
        """Return true if the node is visited already """
        return self.color == colors["BLUE"]

    def is_not_visited_node(self):
        """Return true if the node is not visited yet """
        return self.color == colors["GREY"]

    def is_end_node(self):
        """Return true if the node is the end node"""
        return self.color == colors["PURPLE"]

    def is_start_node(self):
        """Return true if the node is the start node"""
        return self.color == colors["TEAL"]

    def is_barrier_node(self):
        """Return true if the node is a barrier node"""
        return self.color == colors["BLACK"]

    def set_color(self, color):
        """Set the color """
        self.color = colors[color]

    def get_pos(self):
        return self.row, self.col

    def can_move_down(self, grid):
        """Return true if the down neighbor is empty"""
        return self.row < TOTAL_NUM_OF_ROWS - 1 and not grid[self.row + 1][self.col].is_barrier_node()

    def get_down_node(self, grid):
        return grid[self.row + 1][self.col]

    def can_move_up(self, grid):
        """Return true if the up neighbor is empty"""
        return self.row > 0 and not grid[self.row - 1][self.col].is_barrier_node()

    def get_up_node(self, grid):
        return grid[self.row - 1][self.col]

    def can_move_right(self, grid):
        """Return true if the right neighbor is empty"""
        return self.col < TOTAL_NUM_OF_ROWS - 1 and not grid[self.row][self.col + 1].is_barrier_node()

    def get_right_node(self, grid):
        return grid[self.row][self.col + 1]

    def can_move_left(self, grid):
        """Return true if the left neighbor is empty"""
        return self.col > 0 and not grid[self.row][self.col - 1].is_barrier_node()

    def get_left_node(self, grid):
        return grid[self.row][self.col - 1]

    def update_neighbors(self, grid):
        self.neighbors_nodes = []

        if self.can_move_down(grid):
            self.neighbors_nodes.append(self.get_down_node(grid))

        if self.can_move_up(grid):
            self.neighbors_nodes.append(self.get_up_node(grid))

        if self.can_move_right(grid):
            self.neighbors_nodes.append(self.get_right_node(grid))

        if self.can_move_left(grid):
            self.neighbors_nodes.append(self.get_left_node(grid))
