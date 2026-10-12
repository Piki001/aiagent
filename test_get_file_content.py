from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print(result)


result2 = get_file_content("calculator", "main.py")
print(f"lorem.txt length: {len(result2)}")
print(f"lorem.txt truncated: {'truncated' in result2}")
print(result2)

result3 = get_file_content("calculator", "pkg/calculator.py")
print(f"lorem.txt length: {len(result3)}")
print(f"lorem.txt truncated: {'truncated' in result3}")
print(result3)


result4 = get_file_content("calculator", "/bin/cat") #(this should return an error string)
if "Error" in result4:
    print(result4)
else:
    print(f"lorem.txt length: {len(result4)}")
    print(f"lorem.txt truncated: {'truncated' in result4}")
    print(result4)


result5 = get_file_content("calculator", "pkg/does_not_exist.py") #(this should return an error string)
if "Error" in result5:
    print(result5)
else:
    print(f"lorem.txt length: {len(result5)}")
    print(f"lorem.txt truncated: {'truncated' in result5}")
    print(result5)
