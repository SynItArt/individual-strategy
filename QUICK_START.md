# 빠른 배포 가이드

## 🚀 가장 쉬운 방법

### 1단계: Code 탭으로 이동
- GitHub 저장소 페이지에서 상단의 **`Code`** 탭을 클릭하세요
- Settings가 아닌 **Code** 탭에 있어야 합니다

### 2단계: 파일 업로드
1. **`Add file`** 버튼 클릭
2. **`Upload files`** 선택
3. `deploy` 폴더의 모든 파일과 폴더를 드래그 앤 드롭
4. 하단의 **`Commit changes`** 클릭

### 3단계: GitHub Pages 활성화
1. **`Settings`** 탭 클릭
2. 왼쪽 메뉴에서 **`Pages`** 클릭
3. Source: **`main`** 브랜치, **`/ (root)`** 선택
4. **`Save`** 클릭

### 4단계: 확인
몇 분 후 다음 URL에서 접속:
```
https://synitart.github.io/individual-strategy/
```

---

## ⚠️ Code 탭이 비어있는 경우

저장소가 비어있으면 자동으로 파일 업로드 안내가 표시됩니다.
- "uploading an existing file" 링크 클릭
- 또는 `deploy.bat` 파일 실행 (Windows)

---

## 📁 배포할 파일 위치

모든 파일은 `owner-strategy/deploy/` 폴더에 있습니다.

