from functions.write_file import write_file


def test(file, content):
    print(f"Writing to {file} with {len(content)} chars")
    print(write_file("calculator", file, content))
    print("\n")


test("lorem.txt", "wait, this isn't lorem ipsum")
test("pkg/morelorem.txt", "lorem ipsum dolor sit amet")
test("/tmp/temp.txt", "this should not be allowed")
