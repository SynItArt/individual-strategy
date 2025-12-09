# data.go.kr API 연동 가이드

## 📋 개요

data.go.kr의 공공데이터를 활용하여 업종별 통계 데이터를 수집하고, 이를 맞춤형 제안서 생성에 활용합니다.

## 🔑 API 키 발급

### 1단계: data.go.kr 회원가입
1. https://www.data.go.kr 접속
2. 회원가입 및 로그인

### 2단계: API 키 발급
1. **마이페이지** > **활용신청** > **오픈 API** 클릭
2. 원하는 API 선택:
   - 소상공인 경영현황 통계
   - 세무 통계
   - 업종별 통계
3. 활용신청 후 승인 대기
4. 승인 후 API 키 발급

### 3단계: API 키 설정
```bash
# Windows
set DATA_GO_KR_API_KEY=your_api_key_here

# Linux/Mac
export DATA_GO_KR_API_KEY=your_api_key_here
```

또는 `.env` 파일 생성:
```
DATA_GO_KR_API_KEY=your_api_key_here
```

## 📊 수집 가능한 데이터

### 업종별 통계
- 평균 매출액
- 평균 경비
- 평균 세금
- 업종별 특성

### 세무 통계
- 업종별 평균 세금 부담
- 세액공제 가능 항목
- 절세 전략 데이터

### 소상공인 경영현황
- 업종별 경영 지표
- 성공 사례 데이터
- 리스크 요인

## 🚀 데이터 수집 실행

### 자동 수집
```bash
cd Projects/individual-strategy
python data_go_kr_collector.py
```

### 수집되는 데이터
- `industry_data/미용업_YYYYMMDD.json`
- `industry_data/요식업_YYYYMMDD.json`
- `industry_data/소매업_YYYYMMDD.json`
- ... (각 업종별)

## 📁 데이터 구조

```json
{
  "미용업": {
    "statistics": {
      "평균매출": 80000000,
      "평균경비": 50000000,
      "평균세금": 12000000,
      "업종특성": "..."
    },
    "collected_at": "20251215143025"
  }
}
```

## 🔄 데이터 활용

### 맞춤형 제안서 생성 시
1. 사용자가 업종 선택
2. 해당 업종 데이터 자동 로드
3. Genspark AI 분석에 활용
4. 맞춤형 제안서 생성

### Google Sheets 연동
1. 수집된 데이터를 Google Sheets에 업로드
2. Genspark Sheets Agent에 연결
3. 실시간 분석 및 제안서 생성

## 📝 주요 API 목록

### 1. 소상공인 경영현황 통계
- **API ID**: 1160100
- **용도**: 업종별 평균 매출, 경비, 세금 데이터

### 2. 세무 통계
- **API ID**: 15000000
- **용도**: 업종별 세금 부담, 절세 가능 항목

### 3. 업종별 통계
- **API ID**: (API 검색 필요)
- **용도**: 업종별 특성 및 리스크 요인

## 🔧 커스터마이징

### 업종 추가
`data_go_kr_collector.py`의 `industries` 딕셔너리에 업종 추가:

```python
industries = {
    '미용업': 'IND001',
    '요식업': 'IND002',
    '새업종': 'IND008'  # 추가
}
```

### 데이터 수집 주기
- 매일 자동 수집 (cron job 설정)
- 또는 수동 실행

## ⚠️ 주의사항

1. **API 호출 제한**
   - 일일 호출 제한 확인
   - 필요시 대기 시간 추가

2. **데이터 정확성**
   - 공공데이터는 참고용
   - 실제 상담 시 재확인 필요

3. **개인정보 보호**
   - 수집된 데이터는 통계 데이터만
   - 개인정보는 포함하지 않음

## 🐛 문제 해결

### API 키 오류
- API 키가 올바르게 설정되었는지 확인
- 환경변수 설정 확인

### 데이터 수집 실패
- API 서버 상태 확인
- 네트워크 연결 확인
- API 호출 제한 확인

---

**마지막 업데이트:** 2025년 12월  
**관련 파일:** `data_go_kr_collector.py`

