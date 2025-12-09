# 설치 가이드

## 필수 패키지 설치

```bash
pip install -r requirements.txt
```

또는 개별 설치:

```bash
pip install python-pptx flask flask-cors pandas gspread oauth2client requests
```

## Google Sheets 설정

1. Google Cloud Console에서 프로젝트 생성
2. Google Sheets API 활성화
3. 서비스 계정 생성
4. `credentials.json` 파일 다운로드
5. 프로젝트 루트에 `credentials.json` 배치

자세한 내용은 `DB_SETUP_GUIDE.md` 참고

## data.go.kr API 키 설정 (선택사항)

```bash
python data_go_kr_api_setup.py
```

또는 환경변수로 설정:
```bash
# Windows PowerShell
$env:DATA_GO_KR_API_KEY='your_api_key'

# Windows CMD
set DATA_GO_KR_API_KEY=your_api_key
```

## 초기 데이터 생성

```bash
python init_industry_data.py
```

## 테스트

```bash
# 데이터 수집 테스트
python data_go_kr_collector.py

# Genspark 분석 테스트
python auto_genspark_trigger.py
```

