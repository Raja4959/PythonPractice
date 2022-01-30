# def print_string(String):
#     print(String)
#     l = String.split()
#     for a in l:
#         print(a)
#     for a in String:
#         print(a, end=" ")
#     print()
#     for a in String:
#         print(a,'-',ord(a))


# print_string("Hello.... World....!%@")
# print(chr(40))

from pathlib import Path
print("File Name = ",__file__)
Dir = Path(__file__).resolve().parent
print("Parent Directory = ", Dir)

file_path = Path.joinpath(Dir,__file__)
print("File path = ",file_path)