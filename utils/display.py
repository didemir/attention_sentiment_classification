"""
Simple classes to style output.
"""

class icons:
  # Arrows
  L_ARROW  = u'\u2190'     # ←
  U_ARROW  = u'\u2191'     # ↑
  R_ARROW  = u'\u2192'     # →
  D_ARROW  = u'\u2193'     # ↓
  L_DOUBLE = u'\u21D0'     # ⇐
  R_DOUBLE = u'\u21D2'     # ⇒
  U_DOUBLE = u'\u21D1'     # ⇑
  D_DOUBLE = u'\u21D3'     # ⇓
  L_BOLD   = u'\u2B05'     # ⬅
  R_BOLD   = u'\u2B95'     # ⮕

  # Checks & crosses
  TICK        = u'\u2713'  # ✓
  BOLD_TICK   = u'\u2714'  # ✔
  CROSS       = u'\u2717'  # ✗
  BOLD_CROSS  = u'\u2718'  # ✘

  # Status & indicators
  INFO    = u'\u2139'      # ℹ
  WARNING = u'\u26A0'      # ⚠
  STAR    = u'\u2605'      # ★
  CIRCLE  = u'\u25CF'      # ●
  DIAMOND = u'\u25C6'      # ◆
  SQUARE  = u'\u25A0'      # ■
  FLAG    = u'\U0001F6A9'  # 🚩

  # Math & logic
  INFINITY  = u'\u221E'    # ∞
  SUM       = u'\u2211'    # ∑
  DELTA     = u'\u0394'    # Δ
  APPROX    = u'\u2248'    # ≈
  NOT_EQUAL = u'\u2260'    # ≠
  LEQ       = u'\u2264'    # ≤
  GEQ       = u'\u2265'    # ≥

  # Misc
  BULLET     = u'\u2022'   # •
  COPYRIGHT  = u'\u00A9'   # ©
  DEGREE     = u'\u00B0'   # °
  LIGHTNING  = u'\u26A1'   # ⚡
  HOURGLASS  = u'\u231B'   # ⌛
  CHECKBOARD = u'\u2611'   # ☑



class styles:
  """
  ANSI escape codes to style text.
  """
  # Text styles
  BOLD          = '\033[1m'
  DIM           = '\033[2m' # Faded/dimmed text
  ITALIC        = '\033[3m' 
  UNDERLINE     = '\033[4m'
  REVERSE       = '\033[7m' # Swaps foreground and background color
  STRIKETHROUGH = '\033[9m'
  END           = '\033[0m'

  # Text colors
  RED     = '\033[31m'
  GREEN   = '\033[32m'
  YELLOW  = '\033[33m'
  BLUE    = '\033[34m'
  MAGENTA = '\033[35m'
  CYAN    = '\033[36m'
  WHITE   = '\033[37m'

  # Background colors
  BG_RED     = '\033[41m'
  BG_GREEN   = '\033[42m'
  BG_YELLOW  = '\033[43m'
  BG_BLUE    = '\033[44m'
  BG_MAGENTA = '\033[45m'
  BG_CYAN    = '\033[46m'
  BG_WHITE   = '\033[47m'

