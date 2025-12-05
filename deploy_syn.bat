@echo off
chcp 65001 >nul
echo ========================================
echo syn.html 배포 스크립트
echo ========================================
echo.

set "CORP_REPO=C:\Users\user\Downloads\corporate-strategy"
set "SYN_FIXED=C:\Users\user\Downloads\IndivMaster\owner-strategy\deploy\syn_fixed.html"
set "SYN_TARGET=%CORP_REPO%\syn.html"

echo [1/4] 저장소 확인...
if not exist "%CORP_REPO%" (
    echo.
    echo ❌ corporate-strategy 저장소를 찾을 수 없습니다.
    echo.
    echo 다음 명령어로 저장소를 클론하세요:
    echo   cd C:\Users\user\Downloads
    echo   git clone https://github.com/SynItArt/corporate-strategy.git
    echo.
    pause
    exit /b 1
)

echo ✅ 저장소 확인 완료: %CORP_REPO%
echo.

echo [2/4] syn_fixed.html 파일 확인...
if not exist "%SYN_FIXED%" (
    echo ❌ syn_fixed.html 파일을 찾을 수 없습니다: %SYN_FIXED%
    pause
    exit /b 1
)

echo ✅ 파일 확인 완료: %SYN_FIXED%
echo.

echo [3/4] syn.html 파일 복사...
copy /Y "%SYN_FIXED%" "%SYN_TARGET%"
if errorlevel 1 (
    echo ❌ 파일 복사 실패
    pause
    exit /b 1
)

echo ✅ 파일 복사 완료: %SYN_TARGET%
echo.

echo [4/4] Git 커밋 및 푸시...
cd /d "%CORP_REPO%"

git add syn.html
if errorlevel 1 (
    echo ⚠️  Git add 실패 (Git이 초기화되지 않았을 수 있습니다)
    echo.
    echo 수동으로 다음 명령어를 실행하세요:
    echo   cd %CORP_REPO%
    echo   git add syn.html
    echo   git commit -m "Add back button to individual-strategy page"
    echo   git push origin main
    echo.
    pause
    exit /b 1
)

git commit -m "Add back button to individual-strategy page"
if errorlevel 1 (
    echo ⚠️  커밋 실패 (변경사항이 없을 수 있습니다)
)

git push origin main
if errorlevel 1 (
    echo ⚠️  푸시 실패
    echo.
    echo 수동으로 다음 명령어를 실행하세요:
    echo   cd %CORP_REPO%
    echo   git push origin main
    echo.
) else (
    echo ✅ 푸시 완료!
)

echo.
echo ========================================
echo 배포 완료!
echo ========================================
echo.
echo 다음 URL에서 확인하세요:
echo https://synitart.github.io/corporate-strategy/syn.html
echo.
echo ⚠️  GitHub Pages 업데이트에는 몇 분이 걸릴 수 있습니다.
echo.
pause

