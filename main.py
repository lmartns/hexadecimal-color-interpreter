def scanner(text: str) -> str:
    return input(text)


def hex_parser(hexColor: str) -> tuple[int, int, int]:
    hexColor = hexColor[1:7]
    p1, p2, p3 = hexColor[:2], hexColor[2:4], hexColor[4:]
    hex1 = int(p1, 16)
    hex2 = int(p2, 16)
    hex3 = int(p3, 16)
    return hex1, hex2, hex3

def hex_color_interpreter():
    hex_color = scanner("Enter your hex color: 0_0 ")
    r, g, b = hex_parser(hex_color)
    print(f"\033[38;2;{r};{g};{b}mYour color :)\033[0m")

hex_color_interpreter()




