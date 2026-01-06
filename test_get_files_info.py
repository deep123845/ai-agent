from functions.get_files_info import get_files_info


def test(dir):
    print_dir = "current" if dir == "." else dir
    print(f"Result for '{print_dir}' directory:")
    print(get_files_info("calculator", dir))
    print("\n")


test(".")
test("pkg")
test("/bin")
test("../")
