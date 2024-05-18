
# Release Notes for WindowsObjectProject

## v1.0.0 - Initial Release

### New Features

- **GetObject 폴더**:
  - `get_windows_all.py`: 모든 윈도우 객체를 가져오는 기능 추가
  - `get_windows_current.py`: 현재 활성화된 윈도우 객체를 가져오는 기능 추가
  - `get_windows_current_isvisible.py`: 현재 보이는 윈도우 객체를 가져오는 기능 추가
  - `get_windows_object.py`: 특정 윈도우 객체를 가져오는 기능 추가
  - `get_windows_object_child.py`: 자식 윈도우 객체를 가져오는 기능 추가

- **MouseControl 폴더**:
  - `mouse_cursor.py`: 마우스 커서의 좌표를 실시간으로 나타내는 기능 추가
  - `mouse_cursor_windowobj.py`: 마우스 커서 위치의 윈도우 객체를 클릭시 가져오는 기능 추가
  - `mouse_cursor_windowobj_nonclick.py`: 마우스 커서 위치의 윈도우 객체를 클릭하지 않아도 실시간으로 가져와 출력하는 기능 추가
  - `mouse_cursor_windowobj_print.py`: 마우스 커서 위치의 윈도우 객체를 클릭시 가져와 출력하는 기능 추가

### Improvements

- 초기 버전 출시로 기본적인 윈도우 객체 탐지 및 마우스 커서 좌표 표시 기능 제공.

### Bug Fixes

- 초기 버전에서는 보고된 버그가 없습니다.
