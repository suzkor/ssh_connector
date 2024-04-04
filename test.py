import readchar
import re
import sys

lines = [
    "dev-abc",
    "dev-def",
    "dev-ghi"
]

def _get_complete_options(text, options):
    return [option for option in options if option.startswith(text)]

def _get_common_prefix(options):
    min_option = min(options, key=len)
    for i in range(len(min_option)):
        if not all(option[i] == min_option[i] for option in options):
            return min_option[:i]
    return min_option

line = ""
pattern = re.compile(r"[a-zA-Z0-9-_.]")
s = ""
preffix = "env? "

while True:
    last_key = s
    s = readchar.readkey()
    if s == '\x1b[A': # up
        print("up")
    elif s == "\x1b[B": # down
        print("down")
    elif s == "\x1b[C": # right
        print("right")
    elif s == "\x1b[D": # left
        print("left")
    elif s == "\t": # tab
        options = _get_complete_options(line, lines)
        if len(options) == 1:
            line = options[0]
        elif len(options) == 0:
            print("\n No options")
        elif len(options) > 1:
            line = _get_common_prefix(options)
            if last_key == "\t":
                print("\n" + "\n".join(options))
        print("\r" + line, end="", flush=True)
    elif s == "\n": # enter
        break
    elif s == "\x7f": # backspace
        if len(line) > 0:
            line = line[:-1]
        sys.stdout.write("\033[2K\033[G")
        sys.stdout.flush()
        print("\r" + line, end="", flush=True)
    elif pattern.match(s):
        line += s
        print("\r" + line, end="", flush=True)

print("\nline: " + line)
