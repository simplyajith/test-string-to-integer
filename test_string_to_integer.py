import pytest


def string_to_int(value):
	try:
		return int(value)
	except ValueError as err:
		print(err)
		return False
	except TypeError as err:
		print(err)
		return False


@pytest.mark.parametrize("test_input,expected", [("1", 1), ("1000", 1000), ("+888", 888), ("-1", -1), ("-9999", -9999),
												 ("2147483647", 2147483647), ("-2147483647", -2147483647), ("0", 0),
												 (True, 1)])
def test_valid_data(test_input, expected):
	assert expected == string_to_int(test_input)


@pytest.mark.parametrize("data", ["", "999.5", "3/4", "abc", "abc946", "$%^", "--667", "++-6567",
								  None, (), {}, [], (1, 1), [55, ], {56: 77},"0b100","0xABC"])
def test_invalid_data(data):
	assert string_to_int(data) is False


def test_no_input():
	assert 0 == int()


@pytest.mark.parametrize("data", [1000, 5000, 10000])
def test_stress_valid_input(data):
	def generate_number(value):
		x = 1
		while x < value:
			yield str(x)
			x += 1
	
	input_string = ""
	for val in generate_number(data):
		input_string += val
	
	assert string_to_int(input_string) is not False
