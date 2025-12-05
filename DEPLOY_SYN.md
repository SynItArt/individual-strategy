# syn.html 배포 가이드

## 📋 개요
`syn_fixed.html` 파일의 내용을 `corporate-strategy` 저장소의 `syn.html`에 적용하여 배포합니다.

## 🎯 배포 주소
배포 후 다음 URL에서 확인할 수 있습니다:
- `https://synitart.github.io/corporate-strategy/syn.html`
- 또는 `https://synitart.github.io/corporate-strategy/%EF%BD%93%EF%BD%99%EF%BD%8E.html`

## 📝 배포 방법

### 방법 1: GitHub 웹에서 직접 수정 (가장 간단)

1. **GitHub 저장소 접속**
   - `https://github.com/SynItArt/corporate-strategy` 접속
   - `syn.html` 파일 찾기

2. **파일 수정**
   - `syn.html` 파일 클릭
   - 우측 상단의 ✏️ (연필 아이콘) 클릭하여 편집 모드 진입

3. **내용 교체**
   - `syn_fixed.html` 파일의 전체 내용을 복사
   - GitHub 편집기에 전체 붙여넣기 (기존 내용 모두 교체)

4. **커밋 및 푸시**
   - 하단 "Commit changes" 클릭
   - 커밋 메시지 입력: `Add back button to individual-strategy page`
   - "Commit changes" 버튼 클릭

5. **배포 확인**
   - 몇 분 후 `https://synitart.github.io/corporate-strategy/syn.html` 접속하여 확인

### 방법 2: 로컬 Git 사용

1. **저장소 클론** (처음만)
   ```bash
   cd C:\Users\user\Downloads
   git clone https://github.com/SynItArt/corporate-strategy.git
   ```

2. **파일 복사**
   ```bash
   copy "C:\Users\user\Downloads\IndivMaster\owner-strategy\deploy\syn_fixed.html" "C:\Users\user\Downloads\corporate-strategy\syn.html"
   ```

3. **커밋 및 푸시**
   ```bash
   cd corporate-strategy
   git add syn.html
   git commit -m "Add back button to individual-strategy page"
   git push origin main
   ```

## ✅ 주요 변경 사항

1. **뒤로 가기 헤더 추가**
   - `<body>` 태그 바로 다음에 `.back-header` 추가
   - 개인사업자 페이지로 돌아가는 링크 포함

2. **스타일 추가**
   - `position: sticky`로 스크롤 시 상단 고정
   - 반투명 배경과 블러 효과
   - 호버 효과 추가

3. **인쇄 시 숨김 처리**
   - `@media print`에서 `.back-header` 숨김

## 🔍 확인 사항

배포 후 다음을 확인하세요:
- [ ] 뒤로 가기 버튼이 페이지 상단에 표시되는가?
- [ ] 버튼 클릭 시 개인사업자 페이지로 이동하는가?
- [ ] 스크롤 시 버튼이 상단에 고정되는가?
- [ ] 모바일에서도 정상 작동하는가?

## 📞 문제 해결

- **404 에러**: GitHub Pages가 업데이트되는데 몇 분 걸릴 수 있습니다 (최대 10분)
- **변경사항이 안 보임**: 브라우저 캐시를 지우고 새로고침 (Ctrl+F5)
- **링크가 작동 안 함**: URL이 정확한지 확인 (`https://synitart.github.io/individual-strategy/`)

