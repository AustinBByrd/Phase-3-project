import time

def clear_lines(num_lines):
    for _ in range(num_lines):
        print("\033[F\033[K", end="")


# First drawing
drawing1 = [
    "        _____",
    "     _.'_____`._",
    "   .'.-'  12 `-.`.",
    "  /,' 11      1 `.\\",
    " // 10      /   2 \\",
    ";;         /       ::",
    "|| 9  ----O      3 ||",
    "::                 ;;",
    " \\\\ 8           4 //",
    "  \`. 7       5 ,'/",
    "   '.`-.__6__.-'.",
    "      -._____.-"
]

for line in drawing1:
    print(line)

time.sleep(1)  # Wait for 2 seconds

# Clearing specific lines
clear_lines(5)
clear_lines(6)
clear_lines(7)
clear_lines(8)
clear_lines(9)

# Second drawing
drawing2 = [
    "        _____",
    "     _.'_____`._",
    "   .'.-'  12 `-.`.",
    "  /,' 11      1 `.\\",
    " // 10          2 \\",
    ";;                 ::",
    "|| 9  ----O------3 ||",
    "::                 ;;",
    " \\\\ 8           4 //",
    "  \`. 7       5 ,'/",
    "   '.`-.__6__.-'.",
    "      -._____.-"
]

# Move cursor to the top
print("\033[12F")

for line in drawing2:
    print(line)
