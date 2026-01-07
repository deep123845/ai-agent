from functions.run_python_file import run_python_file


def test(file, args=None):
    print(f"Attempting to run file {file}:")
    print(run_python_file("calculator", file, args))
    print("\n")


test("main.py")
test("main.py", ["3 + 5"])
test("tests.py")
test("../main.py")
test("nonexistent.py")
test("lorem.txt")
