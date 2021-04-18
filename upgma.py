
def upgma(labels, distance_matrix):
    tree = '('
    # TODO: generate the tree
    tree += ");"
    return tree


# Input table
original_labels = ['A', 'B', 'C', 'D', 'E', 'F']
original_distance_matrix = [
    [0, 2, 4, 6, 6, 8],
    [2, 0, 4, 6, 6, 8],
    [4, 4, 0, 6, 6, 8],
    [6, 6, 6, 0, 4, 8],
    [6, 6, 6, 4, 0, 8],
    [8, 8, 8, 8, 8, 0]
]
final_tree = upgma(original_labels, original_distance_matrix)
print(f"Final tree: {final_tree}")
