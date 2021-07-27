import pytest
from madlib_demo.madlib import read_template, parse_template, merge, write_new_file, copy_image, append_to_file, reverse_arr


def test_read_template_returns_stripped_string():
    actual = read_template("assets/test.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

def test_read_template_returns_stripped_string_2():
    actual = read_template("assets/test2.txt")
    expected = "It is a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

def test_write_new_file_writes_content_to_file():
    expected = " Some Test Content "
    filepath = "assets/test3.txt"
    write_new_file(filepath, expected)
    with open(filepath, 'r') as file:
        actual = file.read()
    assert actual == expected

def test_copy_binary_fnf(): 
    with pytest.raises(FileNotFoundError) as exc:
        copy_image("assets/eww0.jpg", "assets/test2.jpg")
    # assert str(exc.value) == "No such file or directory"

def test_reverse_array_raises_type_error(): 
    with pytest.raises(TypeError) as exc:
        reverse_arr("12345")
    assert str(exc.value) == "input must be a list"

def test_append_to_file(): 
    append_to_file("assets/test4.txt", "This is the test 4 file \n")
    assert True

@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


@pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
