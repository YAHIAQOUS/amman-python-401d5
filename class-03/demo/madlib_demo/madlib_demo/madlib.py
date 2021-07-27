
def read_template(filepath: str) -> str:
    """ Reads a template from the filepath and returns the stripped content as a string """
    # open the file, using the open() function and passing the filepath as the parameter, and the 'r' parameter, which indicates that we're reading the file
    with open(filepath, 'r') as file:
        # read the file content and assign it to a variable, using the readlines() method
        file_content = file.read()
    return file_content.strip()

def parse_template():
    pass

def merge(): 
    pass

def write_new_file(filepath: str, content: str):
    """ Writes a new file to the filepath with the content """
    # open the file, using the open() function and passing the filepath as the parameter, and the 'w' parameter, which indicates that we're writing to the file
    with open(filepath, 'w') as potato:
        # write the content to the file, using the write() method
        potato.write(content)

# binary, base 2 - number system with two digits 0, 1 => 10
# decimal, base 10 - number system with ten digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 => 10
# hexadecimal, base 16 - number system with sixteen digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f => 10 

# All files are techincally represented in binary, but we can open them in text mode, which makes it easier to read and write to the file
# Opening a file in text mode, it looks for specific characters (\n, \t, \r) and interprets them as newlines, tabs, and carriage returns

def copy_image(src_path: str, dest_path:str):
    """ Copies an image file from one path to the other"""
    # open src file in binary mode
    with open(src_path, 'rb') as src_file:
        # read the file content and assign it to a variable, using the read() method
        src_content = src_file.read()
        # write contents to dest_path
        with open(dest_path, 'wb') as dest_file:
            dest_file.write(src_content)

def append_to_file(filepath: str, content: str):
    """ Writes a new file to the filepath with the content """
    # open the file, using the open() function and passing the filepath as the parameter, and the 'w' parameter, which indicates that we're writing to the file
    with open(filepath, 'a') as potato:
        # write the content to the file, using the write() method
        potato.write(content)

def reverse_arr(arr):
    if type(arr) != list:
        raise TypeError('input must be a list')
    return arr[::-1]