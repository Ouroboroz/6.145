def tree_max(tree):
    max = tree["value"]
    for child in tree["children"]:
        if max < tree_max(child):
            max = tree_max(child)
    return max
