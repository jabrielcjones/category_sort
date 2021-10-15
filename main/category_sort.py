#!/usr/bin/env python

def sort_categories_for_insert(input_json):

    visited = set()
    proper_json_output = []

    category_graph = _create_category_graph(input_json)

    for category in category_graph:
        _sort(category_graph, category, visited, proper_json_output)

    return proper_json_output


def _create_category_graph(input_json):
    category_graph = {}

    for category in input_json:
        category_graph[category['id']] = []

        if category['parent_id']:
            category_graph[category['id']].append(category['parent_id'])

    return category_graph


def _sort(category_graph, current_category, visited, proper_json_output):

    if current_category in visited:
        return

    visited.add(current_category)

    for neighbor in category_graph[current_category]:
        _sort(category_graph, neighbor, visited, proper_json_output)

    proper_json_output.append(current_category)


input_json = [
    {
        'name': 'Watches',
        'id': 74,
        'parent_id': 87
    },
    {
        'name': 'Men',
        'id': 450,
        'parent_id': None
    },
    {
        'name': 'Men',
        'id': 9,
        'parent_id': 87
    },
    {
        'name': 'Men',
        'id': 87,
        'parent_id': 450
    },
    {
        'name': 'Accessories',
        'id': 25,
        'parent_id': 450
    }
]

print(_create_category_graph(input_json))
