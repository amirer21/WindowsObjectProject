import pyautogui
import tkinter as tk
from pywinauto import Desktop, findwindows
import psutil

class MouseCoordinatesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Coordinates")
        self.label = tk.Label(root, text="", font=("Helvetica", 12), bg="white", padx=5, pady=2)
        self.label.pack()
        self.update_label()

    def update_label(self):
        x, y = pyautogui.position()
        offset = 20  # 오프셋을 정의하여 마우스 커서와 GUI 창이 겹치지 않도록 함
        
        try:
            # 마우스 위치에 있는 윈도우 객체를 얻습니다.
            window_handle = findwindows.find_element(active_only=True, found_index=0).handle
            window = Desktop(backend="uia").window(handle=window_handle)
            window_title = window.window_text()
            window_process_id = psutil.Process(window.process_id()).name()
            print(f"X: {x}, Y: {y}\nHandle: {window_handle}\nTitle: {window_title}\nPID: {window_process_id}")
            self.label.config(text=f"X: {x}, Y: {y}\nHandle: {window_handle}\nTitle: {window_title}\nPID: {window_process_id}")
        except Exception as e:
            self.label.config(text=f"X: {x}, Y: {y}\nNo active window found")

        self.root.geometry(f"+{x+offset}+{y+offset}")
        update_interval = 100  # 업데이트 간격을 정의하여 0.1초마다 위치를 업데이트
        self.root.after(update_interval, self.update_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseCoordinatesApp(root)
    root.overrideredirect(True)  # Removes window decorations
    root.attributes("-topmost", True)  # Keeps the window on top
    root.wm_attributes("-transparentcolor", "white")  # Makes the window transparent
    root.configure(bg="white")  # Set background color to make the window transparent
    root.mainloop()
