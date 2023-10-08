#! /usr/bin/python3

# Terminal formatting.

# Non-color formats
FMT_RESET            = "\033[00m"
FMT_BOLD             = "\033[01m"
FMT_FAINT            = "\033[02m"
FMT_ITALICS          = "\033[03m"
FMT_UNDERLINE        = "\033[04m"

# Regular colors
FMT_BLACK            = "\033[30m"
FMT_RED              = "\033[31m"
FMT_GREEN            = "\033[32m"
FMT_YELLOW           = "\033[33m"
FMT_BLUE             = "\033[34m"
FMT_MAGENTA          = "\033[35m"
FMT_CYAN             = "\033[36m"
FMT_LIGHT_GRAY       = "\033[37m"

# Light colors
FMT_GRAY             = "\033[90m"
FMT_LIGHT_RED        = "\033[91m"
FMT_LIGHT_GREEN      = "\033[92m"
FMT_LIGHT_YELLOW     = "\033[93m"
FMT_LIGHT_BLUE       = "\033[94m"
FMT_LIGHT_MAGENTA    = "\033[95m"
FMT_LIGHT_CYAN       = "\033[96m"
FMT_WHITE            = "\033[97m"

# Regular color backgrounds
FMT_BLACK_BG         = "\033[40m"
FMT_RED_BG           = "\033[41m"
FMT_GREEN_BG         = "\033[42m"
FMT_YELLOW_BG        = "\033[43m"
FMT_BLUE_BG          = "\033[44m"
FMT_MAGENTA_BG       = "\033[45m"
FMT_CYAN_BG          = "\033[46m"
FMT_LIGHT_GRAY_BG    = "\033[47m"

# Light color backgrounds
FMT_GRAY_BG          = "\033[100m"
FMT_LIGHT_RED_BG     = "\033[101m"
FMT_LIGHT_GREEN_BG   = "\033[102m"
FMT_LIGHT_YELLOW_BG  = "\033[103m"
FMT_LIGHT_BLUE_BG    = "\033[104m"
FMT_LIGHT_MAGENTA_BG = "\033[105m"
FMT_LIGHT_CYAN_BG    = "\033[106m"
FMT_WHITE_BG         = "\033[107m"

def _format(s : str, reset : bool, fmt : str) -> str:
    return fmt + s + (FMT_RESET if reset else "")

# Non-color formats
def bold             (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_BOLD)
def bold             (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_BOLD)
def faint            (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_FAINT)
def italics          (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_ITALICS)
def underline        (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_UNDERLINE)

# Regular colors
def black            (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_BLACK)
def red              (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_RED)
def green            (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_GREEN)
def yellow           (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_YELLOW)
def blue             (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_BLUE)
def magenta          (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_MAGENTA)
def cyan             (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_CYAN)
def light_gray       (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_GRAY)

# Light colors
def gray             (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_GRAY)
def light_red        (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_RED)
def light_green      (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_GREEN)
def light_yellow     (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_YELLOW)
def light_blue       (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_BLUE)
def light_magenta    (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_MAGENTA)
def light_cyan       (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_CYAN)
def white            (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_WHITE)

# Regular color backgrounds
def black_bg         (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_BLACK_BG)
def red_bg           (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_RED_BG)
def green_bg         (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_GREEN_BG)
def yellow_bg        (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_YELLOW_BG)
def blue_bg          (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_BLUE_BG)
def magenta_bg       (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_MAGENTA_BG)
def cyan_bg          (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_CYAN_BG)
def light_gray_bg    (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_GRAY_BG)

# Light color backgrounds
def gray_bg          (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_GRAY_BG)
def light_red_bg     (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_RED_BG)
def light_green_bg   (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_GREEN_BG)
def light_yellow_bg  (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_YELLOW_BG)
def light_blue_bg    (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_BLUE_BG)
def light_magenta_bg (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_MAGENTA_BG)
def light_cyan_bg    (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_LIGHT_CYAN_BG)
def white_bg         (s : str, reset : bool = True) -> str: return _format(s, reset, FMT_WHITE_BG)

# Non-color format aliases
#bd = bold
#ft = faint
ita = italics
und = underline

# Regular color aliases
blk  = black
#red  = red
grn  = green
yel  = yellow
blu  = blue
mag  = magenta
cya  = cyan
lgra = light_gray

# Light color aliases
gra  = gray
lred = light_red
lgrn = light_green
lyel = light_yellow
lblu = light_blue
lmag = light_magenta
lcya = light_cyan
whi  = white

# Regular color background aliases
blk_bg  = black_bg
#red_bg  = red_bg
grn_bg  = green_bg
yel_bg  = yellow_bg
blu_bg  = blue_bg
mag_bg  = magenta_bg
cya_bg  = cyan_bg
lgra_bg = light_gray_bg

# Light color background aliases
gra_bg  = gray_bg
lred_bg = light_red_bg
lgrn_bg = light_green_bg
lyel_bg = light_yellow_bg
lblu_bg = light_blue_bg
lmag_bg = light_magenta_bg
lcya_bg = light_cyan_bg
whi_bg  = white_bg

# Non-color format list
NON_COLOR_FORMATS = [
    bold,
    faint,
    italics,
    underline,
]

# Regular color list
REGULAR_COLOR_FORMATS = [
    black,
    red,
    green,
    yellow,
    blue,
    magenta,
    cyan,
    light_gray,
]

# Light color list
LIGHT_COLOR_FORMATS = [
    gray,
    light_red,
    light_green,
    light_yellow,
    light_blue,
    light_magenta,
    light_cyan,
    white,
]

# Regular color background list
REGULAR_COLOR_BACKGROUND_FORMATS = [
    black_bg,
    red_bg,
    green_bg,
    yellow_bg,
    blue_bg,
    magenta_bg,
    cyan_bg,
    light_gray_bg,
]

# Light color background list
LIGHT_COLOR_BACKGROUND_FORMATS = [
    gray_bg,
    light_red_bg,
    light_green_bg,
    light_yellow_bg,
    light_blue_bg,
    light_magenta_bg,
    light_cyan_bg,
    white_bg,
]

COLOR_FORMATS               = REGULAR_COLOR_FORMATS + LIGHT_COLOR_FORMATS
COLOR_BACKGROUND_FORMATS    = REGULAR_COLOR_BACKGROUND_FORMATS + LIGHT_COLOR_BACKGROUND_FORMATS
ALL_FORMATS                 = NON_COLOR_FORMATS + COLOR_FORMATS + COLOR_BACKGROUND_FORMATS

# Print some formatting samples
def swatch(
        include_row_labels        : bool = True,
        include_column_labels     : bool = True,
        include_non_color_formats : bool = True,
        include_faint_colors      : bool = False,
        ):
    
    print()

    color_labels = [
        "blk", "red", "grn",  "yel",  "blu",  "mag",  "cya",  "lgra",
        "gra", "lred", "lgrn", "lyel", "lblu", "lmag", "lcya", "whi",
    ]

    # Nested function, for re-use purposes
    def print_grid(make_faint : bool = False):

        # Faint function
        ffn = faint if make_faint else lambda s: s

        if include_column_labels:

            # Magic incantation to rotate a list of strings to print vertically
            rotated_letters = zip(*[
                bg.rjust(4)
                for bg in color_labels[1:]])

            # Print the header
            for tup in rotated_letters:
                if include_row_labels:
                    print(" " * 6, end="")
                i = 1
                for c in tup:
                    print(ffn(black(COLOR_FORMATS[i](" {} ".format(c)))), end="")
                    i += 1
                print()

        # Print block
        i = 0
        for fg in COLOR_FORMATS:
            label = color_labels[i]
            s = "{:>5} ".format(label) if include_row_labels else ""
            if label == "black" and include_row_labels:
                # highlight only non-whitespace characters
                s = "".join(gray_bg(c, reset=False)
                        if c != " " else black_bg(c, reset=False) for c in s)
            for bg in COLOR_BACKGROUND_FORMATS[1:]:
                s += bg(" # ", reset=False)
            s = ffn(fg(s))
            print(s)
            i += 1

    print_grid()

    if include_faint_colors:
        print()
        print_grid(make_faint=True)

    if include_non_color_formats:
        print()
        if include_row_labels:
            print(" " * 6, end = "")
        for fmt in NON_COLOR_FORMATS:
            print(fmt(fmt.__name__.ljust(9)), end = "  ")
        print()
    
    print()


