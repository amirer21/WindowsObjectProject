import pyautogui
import tkinter as tk  # GUI 창 생성
from pywinauto import Desktop, findwindows 
import psutil  # 프로세스 정보

class MouseCoordinatesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Coordinates")
        self.label = tk.Label(root, text="", font=("Helvetica", 12), bg="white", padx=5, pady=2)
        self.label.pack()
        self.update_label()  # 라벨 업데이트를 시작

    def get_cursor_window_info(self):
        x, y = pyautogui.position()  # 마우스 커서의 현재 위치를 가져옴
        try:
            # 마우스 위치에 있는 윈도우 객체를 찾기
            window_handle = findwindows.find_window(handle=pyautogui.getWindowsAt(x, y)[0]._hWnd)
            if window_handle:
                window = Desktop(backend="uia").window(handle=window_handle)  # 해당 핸들로 윈도우 객체를 얻음
                window_title = window.window_text()  # 윈도우의 제목을 가져옴
                window_process_id = window.process_id()  # 윈도우의 프로세스 ID를 가져옴
                window_process_name = psutil.Process(window_process_id).name()  # 프로세스 이름을 가져옴
                return x, y, window_handle, window_title, window_process_id, window_process_name
            else:
                return x, y, None, None, None, None
        except Exception as e:
            return x, y, None, None, None, None

    def update_label(self):
        x, y, window_handle, window_title, window_process_id, window_process_name = self.get_cursor_window_info()
        offset = 20  # 오프셋을 정의하여 마우스 커서와 GUI 창이 겹치지 않도록 함
        
        if window_handle:
            # 라벨을 업데이트하여 커서 위치와 윈도우 정보를 표시
            self.label.config(text=f"X: {x}, Y: {y}\nHandle: {window_handle}\nTitle: {window_title}\nPID: {window_process_id}\nProcess: {window_process_name}")
            print(f"X: {x}, Y: {y}\nHandle: {window_handle}\nTitle: {window_title}\nPID: {window_process_id}\nProcess: {window_process_name}")
        else:
            self.label.config(text=f"X: {x}, Y: {y}\nNo window found")
            print(f"X: {x}, Y: {y}\nNo window found")

        # GUI 창의 위치를 마우스 커서 위치로 업데이트
        self.root.geometry(f"+{x+offset}+{y+offset}")
        update_interval = 100  # 0.1초마다 위치를 업데이트
        self.root.after(update_interval, self.update_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseCoordinatesApp(root)
    root.overrideredirect(True)  # 윈도우 장식을 제거
    root.attributes("-topmost", True)  # 창을 항상 위에 표시
    root.wm_attributes("-transparentcolor", "white")  # 창 배경을 투명하게 설정
    root.configure(bg="white")  # 배경색을 흰색으로 설정
    root.mainloop()  # GUI 루프를 시작
