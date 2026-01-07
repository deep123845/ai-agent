from functions.get_file_content import get_file_content


def test(file):
    print(f"Content for {file}:")
    print(get_file_content("calculator", file))
    print("\n")


test("lorem.txt")
test("main.py")
test("pkg/calculator.py")
test("/bin/cat")
test("pkg/does_not_exist.py")
