import ctypes
from ctypes import wintypes

# Load User32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Define necessary functions and types from User32.dll
GetWindowRect = user32.GetWindowRect
GetClassNameW = user32.GetClassNameW
GetWindowLongW = user32.GetWindowLongW
GetWindowThreadProcessId = user32.GetWindowThreadProcessId

# Constants for GetWindowLong
GWL_STYLE = -16
GWL_EXSTYLE = -20

# Define RECT structure
class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]

# Define a helper function to get window title
def get_window_title(hWnd):
    length = user32.GetWindowTextLengthW(hWnd)
    if length > 0:
        buff = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hWnd, buff, length + 1)
        return buff.value
    return None

# Define a helper function to get window class name
def get_class_name(hWnd):
    buff = ctypes.create_unicode_buffer(256)
    user32.GetClassNameW(hWnd, buff, 256)
    return buff.value

# Define a helper function to get window rectangle
def get_window_rect(hWnd):
    rect = RECT()
    if GetWindowRect(hWnd, ctypes.byref(rect)):
        return (rect.left, rect.top, rect.right, rect.bottom)
    return None

# Define a helper function to get window styles
def get_window_styles(hWnd):
    style = GetWindowLongW(hWnd, GWL_STYLE)
    ex_style = GetWindowLongW(hWnd, GWL_EXSTYLE)
    return style, ex_style

# Define a function to get window properties
def get_window_properties(hWnd):
    title = get_window_title(hWnd)
    class_name = get_class_name(hWnd)
    rect = get_window_rect(hWnd)
    styles = get_window_styles(hWnd)
    pid = wintypes.DWORD()
    GetWindowThreadProcessId(hWnd, ctypes.byref(pid))
    
    return {
        "Title": title,
        "Class Name": class_name,
        "Rectangle": rect,
        "Styles": styles,
        "Process ID": pid.value
    }

# Example usage with a known window handle
example_hWnd = 526944  # Replace with an actual window handle
properties = get_window_properties(example_hWnd)

# Display the window properties
for prop, value in properties.items():
    print(f"{prop}: {value}")
