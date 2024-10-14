from math import ceil
import sys
import re

X = 95
Y = 10
CHARSET = ["╭", "─", "╮", "│", " ", "│", "╰", "─", "╯"]

DG = "\033[2;38m"	# Dark Gray
BO = "\033[1m"		# Bold
IT = "\033[3m"		# Italic
UN = "\033[4m"		# Underline
NC = "\033[0m"		# No Color (Reset)

def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

def generate_box(x, y, offset_x=0, offset_y=0, text=""):
	lines = text.splitlines()
	print("\n" * ceil(offset_y / 2), end="")
	print(" " * ceil(offset_x / 2), end="")
	print(CHARSET[0], end="")
	for _ in range(x - 2 - offset_x):
		print(CHARSET[1], end="")
	print(CHARSET[2], end=" " * int(offset_x // 2) + "\n")

	for line in range(y - 2 - ceil(offset_y / 2)):
		print(CHARSET[4] * ceil(offset_x / 2), end="")
		print(CHARSET[3], end="")
		if (line < len(lines)):
			# move cusror to the middle of the box
			sys.stdout.write("\033[{}C".format(ceil((x - 2 - offset_x - len(escape_ansi(lines[line]))) / 2)))
			print(lines[line], end="")
		sys.stdout.write("\r\033[{0}C".format(x - 1 - offset_x // 2))
		print(CHARSET[5], end=CHARSET[4] * int(offset_x // 2) + "\n")

	print(" " * ceil(offset_x / 2), end="")
	print(CHARSET[6], end="")
	for _ in range(x - 2 - offset_x):
		print(CHARSET[7], end="")
	print(CHARSET[8], end=" " * int(offset_x // 2))
	print("\n" * int(offset_y // 2 - 1))

TEXT = f"""tel.{DG}: (+33)7 82 18 26 03{NC}
email{DG}: {UN}justincollon@gmail.com{NC}
github{DG}: {UN}https://github.com/error7404{NC}
wakatime{DG}: {UN}https://wakatime.com/@error7404{NC}
localisation{DG}: {IT}73370 Le Bourget-du-Lac, France{NC}
"""

print("[38;5;76m❯[39m [32mcat[39m [4mcontact.txt[0m")
# generate_box(X, Y, offset_x=46, offset_y=0, text=TEXT)
generate_box(X, Y, offset_x=0, offset_y=0, text=TEXT)