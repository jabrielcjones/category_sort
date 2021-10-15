import sys
import os
import yaml

sys.path.append(os.path.abspath(os.path.join('..', 'main')))

from category_sort import sort_categories_for_insert, _create_category_graph


with open('sample_inputs.yml', 'r') as stream:
    try:
        sample_inputs = yaml.safe_load(stream)

    except yaml.YAMLError as err:
        print(err)
        exit()

class TestCreateCategoryGraph:

    def test_one(self):
        input_json = sample_inputs['1']['input']
        expected_result = sample_inputs['1']['graph']

        assert _create_category_graph(input_json) == expected_result

    def test_two(self):
        input_json = sample_inputs['2']['input']
        expected_result = sample_inputs['2']['graph']

        assert _create_category_graph(input_json) == expected_result

    def test_three(self):
        input_json = sample_inputs['3']['input']
        expected_result = sample_inputs['3']['graph']

        assert _create_category_graph(input_json) == expected_result

    def test_four(self):
        input_json = sample_inputs['4']['input']
        expected_result = sample_inputs['4']['graph']

        assert _create_category_graph(input_json) == expected_result

    def test_five(self):
        input_json = sample_inputs['5']['input']
        expected_result = sample_inputs['5']['graph']

        assert _create_category_graph(input_json) == expected_result

    def test_six(self):
        input_json = sample_inputs['6']['input']
        expected_result = sample_inputs['6']['graph']

        assert _create_category_graph(input_json) == expected_result

    def test_seven(self):
        input_json = sample_inputs['7']['input']
        expected_result = sample_inputs['7']['graph']

        assert _create_category_graph(input_json) == expected_result

    def test_eight(self):
        input_json = sample_inputs['8']['input']
        expected_result = sample_inputs['8']['graph']

        assert _create_category_graph(input_json) == expected_result


class TestSortCategories:

    def test_one(self):
        input_json = sample_inputs['1']['input']
        expected_result = sample_inputs['1']['output']

        assert sort_categories_for_insert(input_json) == expected_result

    def test_two(self):
        input_json = sample_inputs['2']['input']
        expected_result = sample_inputs['2']['output']

        assert sort_categories_for_insert(input_json) == expected_result

    def test_three(self):
        input_json = sample_inputs['3']['input']
        expected_result = sample_inputs['3']['output']

        assert sort_categories_for_insert(input_json) == expected_result

    def test_four(self):
        input_json = sample_inputs['4']['input']
        expected_result = sample_inputs['4']['output']

        assert sort_categories_for_insert(input_json) == expected_result

    def test_five(self):
        input_json = sample_inputs['5']['input']
        expected_result = sample_inputs['5']['output']

        assert sort_categories_for_insert(input_json) == expected_result

    def test_six(self):
        input_json = sample_inputs['6']['input']
        expected_result = sample_inputs['6']['output']

        assert sort_categories_for_insert(input_json) == expected_result

    def test_seven(self):
        input_json = sample_inputs['7']['input']
        expected_result = sample_inputs['7']['output']

        assert sort_categories_for_insert(input_json) == expected_result

    def test_eight(self):
        input_json = sample_inputs['8']['input']
        expected_result = sample_inputs['8']['output']

        assert sort_categories_for_insert(input_json) == expected_result
