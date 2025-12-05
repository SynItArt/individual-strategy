@echo off
echo ========================================
echo GitHub 배포 스크립트
echo ========================================
echo.

cd /d "%~dp0"

echo [1/5] Git 저장소 초기화...
git init

echo.
echo [2/5] 원격 저장소 연결...
git remote remove origin 2>nul
git remote add origin https://github.com/SynItArt/individual-strategy.git

echo.
echo [3/5] 모든 파일 추가...
git add .

echo.
echo [4/5] 커밋 생성...
git commit -m "Deploy: 개인사업자 재무전략 웹사이트"

echo.
echo [5/5] GitHub에 푸시...
git branch -M main
git push -u origin main --force

echo.
echo ========================================
echo 배포 완료!
echo ========================================
echo.
echo 다음 URL에서 확인하세요:
echo https://synitart.github.io/individual-strategy/
echo.
pause

