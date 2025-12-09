# GitHub Pages 배포 가이드

## ✅ 자동 배포 설정 완료

GitHub Actions 워크플로우가 설정되어 있어서, `main` 브랜치에 푸시할 때마다 자동으로 GitHub Pages에 배포됩니다.

## 🔧 GitHub Pages 활성화 방법

### 1단계: 저장소 Settings 접속
1. GitHub 저장소 페이지로 이동: `https://github.com/SynItArt/individual-strategy`
2. 상단 메뉴에서 **Settings** 클릭
3. 왼쪽 사이드바에서 **Pages** 클릭

### 2단계: Pages 설정
1. **Source** 섹션에서:
   - **Deploy from a branch** 선택
   - **Branch**: `main` 선택
   - **Folder**: `/ (root)` 선택
   - **Save** 클릭

2. 또는 **GitHub Actions**를 사용하도록 설정:
   - **Source** 섹션에서 **GitHub Actions** 선택
   - 이미 `.github/workflows/deploy.yml` 파일이 설정되어 있으므로 자동으로 작동합니다.

### 3단계: 배포 확인
- 몇 분 후 다음 URL에서 확인:
  - `https://synitart.github.io/individual-strategy/`
  - `https://synitart.github.io/individual-strategy/index.html`
  - `https://synitart.github.io/individual-strategy/consultation_checklist.html`
  - `https://synitart.github.io/individual-strategy/consultation_booking.html`
  - `https://synitart.github.io/individual-strategy/customer_status.html`

## 📋 배포 상태 확인

### GitHub Actions에서 확인
1. 저장소 페이지에서 **Actions** 탭 클릭
2. **Deploy to GitHub Pages** 워크플로우 확인
3. 초록색 체크 표시가 나타나면 배포 완료

### 배포 로그 확인
- Actions 탭에서 각 워크플로우 실행을 클릭하여 상세 로그 확인 가능

## 🚀 수동 배포 (필요시)

일반적으로는 자동 배포가 작동하지만, 수동으로 배포하려면:

```bash
# 1. 변경사항 커밋
git add .
git commit -m "Update website"

# 2. GitHub에 푸시
git push origin main

# 3. GitHub Actions가 자동으로 배포 시작
```

## 🔍 문제 해결

### 배포가 안 되는 경우
1. **Settings > Pages**에서 Source가 올바르게 설정되었는지 확인
2. **Actions** 탭에서 워크플로우 실행 상태 확인
3. 에러 메시지가 있으면 로그 확인

### 변경사항이 반영되지 않는 경우
1. 브라우저 캐시 삭제 (Ctrl+F5)
2. GitHub Pages 배포 완료까지 몇 분 대기 (최대 10분)
3. Actions 탭에서 배포 상태 확인

### 404 에러가 발생하는 경우
1. 파일 경로가 올바른지 확인
2. `index.html` 파일이 루트 디렉토리에 있는지 확인
3. GitHub Pages 설정에서 Source 경로 확인

## 📝 주요 파일 경로

배포 후 다음 URL에서 접근 가능:

- 메인 페이지: `https://synitart.github.io/individual-strategy/`
- 체크리스트: `https://synitart.github.io/individual-strategy/consultation_checklist.html`
- 상담 예약: `https://synitart.github.io/individual-strategy/consultation_booking.html`
- 고객 상태: `https://synitart.github.io/individual-strategy/customer_status.html`

## ✅ 배포 체크리스트

배포 전 확인사항:
- [ ] 모든 변경사항이 커밋되었는가?
- [ ] `main` 브랜치에 푸시되었는가?
- [ ] GitHub Pages가 활성화되어 있는가?
- [ ] GitHub Actions 워크플로우가 정상 작동하는가?

배포 후 확인사항:
- [ ] 웹사이트가 정상적으로 로드되는가?
- [ ] 모든 링크가 작동하는가?
- [ ] 모바일에서도 정상 작동하는가?
- [ ] 체크리스트 기능이 정상 작동하는가?

---

**마지막 업데이트:** 2025년 12월  
**배포 URL:** https://synitart.github.io/individual-strategy/

