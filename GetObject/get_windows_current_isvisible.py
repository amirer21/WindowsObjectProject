import ctypes
from ctypes import wintypes

# Load User32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Define necessary functions and types from User32.dll
EnumWindows = user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
IsWindowVisible = user32.IsWindowVisible
IsIconic = user32.IsIconic
GetWindowTextLengthW = user32.GetWindowTextLengthW
GetWindowTextW = user32.GetWindowTextW
GetWindowThreadProcessId = user32.GetWindowThreadProcessId
GetForegroundWindow = user32.GetForegroundWindow

# Define a helper function to get window titles
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

# Callback function for EnumWindows
def enum_windows_proc(hWnd, lParam):
    if IsWindowVisible(hWnd) and get_window_title(hWnd):  # Only consider visible windows with titles
        # Check if the window is the foreground window or is not minimized
        if hWnd == GetForegroundWindow() or not IsIconic(hWnd):
            windows.append((hWnd, get_window_title(hWnd), get_process_id(hWnd)))
    return True

# List to store the window handles, titles, and process IDs
windows = []

# Call EnumWindows with the callback function
EnumWindows(EnumWindowsProc(enum_windows_proc), 0)

# Display the collected window handles, titles, and process IDs
for hWnd, title, pid in windows:
    print(f"Window Handle: {hWnd}, Title: {title}, Process ID: {pid}")
