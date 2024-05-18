# WindowsObjectProject

WindowsObjectProject는 윈도우 시스템에서 다양한 윈도우 객체를 가져오고 마우스 커서와 연동하여 객체 정보를 출력하는 파이썬 프로젝트입니다. 이 프로젝트는 윈도우 객체의 정보를 쉽게 가져오고, 이를 시각적으로 확인할 수 있도록 도와줍니다.

## 폴더 구조

### GetObject 폴더

- `get_windows_all.py`: 모든 윈도우 객체 가져오기
- `get_windows_current.py`: 현재 객체 가져오기
- `get_windows_current_isvisible.py`: 현재 보이는 객체 가져오기
- `get_windows_object.py`: 특정 객체 가져오기
- `get_windows_object_child.py`: 자식 객체 가져오기

### MouseControl 폴더

- `mouse_cursor.py`: 커서 좌표 나타내기
- `mouse_cursor_windowobj.py`: 커서 위치의 윈도우 객체 가져오기 (클릭시)
- `mouse_cursor_windowobj_nonclick.py`: 커서 위치의 윈도우 객체 가져오기 및 출력 (클릭하지 않아도)
- `mouse_cursor_windowobj_print.py`: 커서 위치의 윈도우 객체 가져오기 및 출력 (클릭시)

## 설치 방법

1. 이 저장소를 클론합니다.

   ```bash
   git clone https://github.com/amirer21/WindowsObjectProject.git
   cd WindowsObjectProject
   ```

필요한 패키지를 설치합니다.

> pip install -r requirements.txt

## 사용 방법

1. GetObject 스크립트 사용

### get_windows_all.py 실행

> python GetObject/get_windows_all.py

이 스크립트는 시스템의 모든 윈도우 객체를 출력합니다.

### get_windows_current.py 실행

> python GetObject/get_windows_current.py

이 스크립트는 현재 활성화된 윈도우 객체를 출력합니다.

2. MouseControl 스크립트 사용

### mouse_cursor.py 실행

> python MouseControl/mouse_cursor.py

이 스크립트는 마우스 커서의 좌표를 실시간으로 표시합니다.

### mouse_cursor_windowobj_nonclick.py 실행

> python MouseControl/mouse_cursor_windowobj_nonclick.py

이 스크립트는 마우스 커서 위치의 윈도우 객체 정보를 실시간으로 표시합니다.

## 기여 방법

- 이 저장소를 포크합니다.

- 새 브랜치를 생성합니다. (git checkout -b feature/your-feature)

- 변경 사항을 커밋합니다. (git commit -am 'Add some feature')

- 브랜치에 푸시합니다. (git push origin feature/your-feature)

- 풀 리퀘스트를 생성합니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.