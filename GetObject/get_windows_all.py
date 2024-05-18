import ctypes
from ctypes import wintypes
import collections

# Load User32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Define necessary functions from User32.dll
GetTopWindow = user32.GetTopWindow
GetTopWindow.argtypes = [wintypes.HWND]
GetTopWindow.restype = wintypes.HWND

GetWindow = user32.GetWindow
GetWindow.argtypes = [wintypes.HWND, wintypes.UINT]
GetWindow.restype = wintypes.HWND

GetWindowThreadProcessId = user32.GetWindowThreadProcessId
GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
GetWindowThreadProcessId.restype = wintypes.DWORD

GW_HWNDNEXT = 2  # Define constant for getting the next window

# Define a function to get the top-level windows
def sort_windows_top_to_bottom():
    sorted_windows = []
    hWnd = GetTopWindow(None)
    while hWnd:
        sorted_windows.append(hWnd)
        hWnd = GetWindow(hWnd, GW_HWNDNEXT)
    return sorted_windows

# Define a helper function to get window titles
def get_window_title(hWnd):
    length = user32.GetWindowTextLengthW(hWnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hWnd, buff, length + 1)
    return buff.value

# Define a helper function to get process ID
def get_process_id(hWnd):
    pid = wintypes.DWORD()
    GetWindowThreadProcessId(hWnd, ctypes.byref(pid))
    return pid.value

# Get the sorted windows
sorted_windows = sort_windows_top_to_bottom()

# Display the sorted window handles, their titles, and process IDs
for hWnd in sorted_windows:
    print(f"Window Handle: {hWnd}, Title: {get_window_title(hWnd)}, Process ID: {get_process_id(hWnd)}")

# Get the main window (the first one in the sorted list, if available)
main_window = sorted_windows[0] if sorted_windows else None
if main_window:
    print(f"Main Window Handle: {main_window}, Title: {get_window_title(main_window)}, Process ID: {get_process_id(main_window)}")
else:
    print("No main window found.")
