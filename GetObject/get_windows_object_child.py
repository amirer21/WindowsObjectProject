import ctypes
from ctypes import wintypes

# Load User32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Define necessary functions and types from User32.dll
GetParent = user32.GetParent
EnumChildWindows = user32.EnumChildWindows
EnumChildWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
GetWindowTextLengthW = user32.GetWindowTextLengthW
GetWindowTextW = user32.GetWindowTextW
GetWindowThreadProcessId = user32.GetWindowThreadProcessId

# Define a helper function to get window title
def get_window_title(hWnd):
    length = GetWindowTextLengthW(hWnd)
    if length > 0:
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowTextW(hWnd, buff, length + 1)
        return buff.value
    return None

# Define a helper function to get process ID
def get_process_id(hWnd):
    pid = wintypes.DWORD()
    GetWindowThreadProcessId(hWnd, ctypes.byref(pid))
    return pid.value

# Define a function to get parent window
def get_parent_window(hWnd):
    parent_hWnd = GetParent(hWnd)
    if parent_hWnd:
        return {
            "Handle": parent_hWnd,
            "Title": get_window_title(parent_hWnd),
            "Process ID": get_process_id(parent_hWnd)
        }
    return None

# Define a callback function to enumerate child windows
def enum_child_windows_proc(hWnd, lParam):
    children.append({
        "Handle": hWnd,
        "Title": get_window_title(hWnd),
        "Process ID": get_process_id(hWnd)
    })
    return True

# Define a function to get child windows
def get_child_windows(hWnd):
    global children
    children = []
    EnumChildWindows(hWnd, EnumChildWindowsProc(enum_child_windows_proc), 0)
    return children

# Define a function to get related windows (parent and children)
def get_related_windows(hWnd):
    parent = get_parent_window(hWnd)
    children = get_child_windows(hWnd)
    
    return {
        "Parent": parent,
        "Children": children
    }

# Example usage with a known window handle
example_hWnd = 526944  # Replace with an actual window handle
related_windows = get_related_windows(example_hWnd)

# Display the related windows
print(f"Window Handle: {example_hWnd}, Title: {get_window_title(example_hWnd)}, Process ID: {get_process_id(example_hWnd)}")
if related_windows["Parent"]:
    print(f"Parent Handle: {related_windows['Parent']['Handle']}, Title: {related_windows['Parent']['Title']}, Process ID: {related_windows['Parent']['Process ID']}")
else:
    print("No parent window found.")
if related_windows["Children"]:
    for child in related_windows["Children"]:
        print(f"Child Handle: {child['Handle']}, Title: {child['Title']}, Process ID: {child['Process ID']}")
else:
    print("No child windows found.")
