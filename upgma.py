# Global variables

subtree_list = {}


# Class definitions

class Subtree:
    def __init__(self, a, b, distance):
        self.a = a
        self.b = b
        distance_a = 0
        distance_b = 0
        if a in subtree_list:
            self.a = subtree_list[a]
            distance_a = subtree_list[a].middle
        if b in subtree_list:
            self.b = subtree_list[b]
            distance_b = subtree_list[b].middle
        self.middle = distance / 2
        self.distance_a = self.middle - distance_a
        self.distance_b = self.middle - distance_b

    def __str__(self):
        return f"({self.a}:{self.distance_a},{self.b}:{self.distance_b})"


# Function definitions

def lowest_distance(distance_matrix):
    num_rows = len(distance_matrix)
    num_columns = len(distance_matrix[0])

    min_distance = float("inf")
    min_distance_row = -1
    min_distance_column = -1

    for row in range(num_rows):
        for column in range(num_columns):
            if 0 < distance_matrix[row][column] < min_distance:
                min_distance = distance_matrix[row][column]
                min_distance_row = row
                min_distance_column = column

    return min_distance, min_distance_row, min_distance_column


def generate_new_subtree(a, b, distance):
    new_subtree = Subtree(a, b, distance)
    new_id = f"{a}{b}"
    subtree_list[new_id] = new_subtree


def recalculate_matrix(distance_matrix, row_index, column_index):
    num_rows = len(distance_matrix)

    distance_list = []
    for i in range(num_rows):
        if i == row_index:
            distance_list.append(0)
            continue
        if i == column_index:
            continue
        new_distance = (distance_matrix[row_index][i] + distance_matrix[column_index][i]) / 2
        distance_list.append(new_distance)

    # Remove the row for the second index
    del distance_matrix[column_index]

    # Remove the column for the second index
    for i in range(num_rows - 1):
        del distance_matrix[i][column_index]

    # Use the distance list to update the first index row with the new distances
    for i in range(num_rows - 1):
        distance_matrix[i][row_index] = distance_list[i]

    # Use the distance list to update the first index column with the new distances
    for i in range(num_rows - 1):
        distance_matrix[row_index][i] = distance_list[i]


def join_labels(label_list, row, column):
    new_label = f"{label_list[row]}{label_list[column]}"

    label_list[row] = new_label
    del label_list[column]


def convert_subtree_to_newick_format(final_subtree):
    tree = str(final_subtree) + ';'
    return tree


def upgma(labels, distance_matrix):
    while len(labels) > 1:
        # Find lowest distance
        distance, row, column = lowest_distance(distance_matrix)

        # Labels
        if column < row:
            row, column = column, row

        a = labels[row]
        b = labels[column]

        # Generates the new subtree
        generate_new_subtree(a, b, distance)

        # Recalculate the distance matrix
        recalculate_matrix(distance_matrix, row, column)

        # Join the labels on the list
        join_labels(labels, row, column)

    return convert_subtree_to_newick_format(list(subtree_list.items())[-1][1])


# Input table
original_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
original_distance_matrix = [
    [0.0000000, 2.2266620, 3.3353841, 3.0926941, 1.8896296, 4.9589915, 4.3943885, 5.4122139],
    [2.2266620, 0.0000000, 1.1567076, 0.9140176, 1.3807486, 4.4501105, 3.8855074, 4.9033329],
    [3.3353841, 1.1567076, 0.0000000, 1.8198296, 2.4894707, 5.5588327, 4.9942296, 6.0120551],
    [3.0926941, 0.9140176, 1.8198296, 0.0000000, 2.2467807, 5.3161427, 4.7515396, 5.7693651],
    [1.8896296, 1.3807486, 2.4894707, 2.2467807, 0.0000000, 3.3471233, 2.7825202, 3.8003457],
    [4.9589915, 4.4501105, 5.5588327, 5.3161427, 3.3471233, 0.0000000, 1.1966232, 2.2144487],
    [4.3943885, 3.8855074, 4.9942296, 4.7515396, 2.7825202, 1.1966232, 0.0000000, 1.2176200],
    [5.4122139, 4.9033329, 6.0120551, 5.7693651, 3.8003457, 2.2144487, 1.2176200, 0.0000000]
]
final_tree = upgma(original_labels, original_distance_matrix)
print(f"Final tree: {final_tree}")
