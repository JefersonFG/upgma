from upgma import upgma


def test_upgma():
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
    generated_tree = upgma(original_labels, original_distance_matrix)
    expected_tree = "(((D:2,E:2):1,((A:1,B:1):1,C:2):1):1,F:4);"
    print(f"Generated tree: {generated_tree}")
    print(f"Expected tree: {expected_tree}")
    assert(generated_tree == expected_tree)
