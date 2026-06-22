# 1 - read a enter
# 2 - valid enter
# 3 - parse hex > rgb
# 4 - print color in terminal


# import re
#
#
# def scanner(text: str) -> str:
#     return input(text)
#
#
# def hex_valid(regex: str):
#     match = re.search(regex, scanner("Text your hex color: "))
#     if match:
#         print("Hex is valid")
#     else:
#         print("Hex is not valid")
#


def hex_parser(hexColor: str):
    pass


hex_string = "#ffffff"
result = int(hex_string, 16)
print(result)
