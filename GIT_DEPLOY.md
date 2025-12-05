# Git 명령어로 배포하기

## 방법 1: GitHub 웹 인터페이스 (간단)

1. **Code 탭으로 이동**
   - 저장소 페이지에서 상단의 `Code` 탭 클릭
   - `Add file` → `Upload files` 버튼이 보입니다

2. **파일 업로드**
   - `deploy` 폴더의 모든 파일과 폴더를 드래그 앤 드롭
   - `Commit changes` 클릭

## 방법 2: Git 명령어 (터미널 사용)

### 처음 배포하는 경우

```bash
# 1. deploy 폴더로 이동
cd owner-strategy/deploy

# 2. Git 저장소 초기화
git init

# 3. 원격 저장소 연결
git remote add origin https://github.com/SynItArt/individual-strategy.git

# 4. 모든 파일 추가
git add .

# 5. 커밋
git commit -m "Initial commit: 개인사업자 재무전략 웹사이트"

# 6. 메인 브랜치로 푸시
git branch -M main
git push -u origin main
```

### 이미 파일이 있는 경우 (강제 업로드)

```bash
# 1. deploy 폴더로 이동
cd owner-strategy/deploy

# 2. Git 저장소 초기화
git init

# 3. 원격 저장소 연결
git remote add origin https://github.com/SynItArt/individual-strategy.git

# 4. 모든 파일 추가
git add .

# 5. 커밋
git commit -m "Deploy: 개인사업자 재무전략 웹사이트"

# 6. 강제 푸시 (기존 파일 덮어쓰기)
git branch -M main
git push -u origin main --force
```

## 방법 3: GitHub Desktop 사용

1. GitHub Desktop 설치 및 로그인
2. `File` → `Clone Repository`
3. `SynItArt/individual-strategy` 선택
4. `deploy` 폴더의 파일들을 복사
5. 커밋 및 푸시

