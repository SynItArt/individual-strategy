# Genspark 실시간 연동 완료 가이드

## ✅ 완료된 작업

### 1. Genspark 통합 모듈 생성
- `genspark_integration.py`: 체크리스트 분석 및 제안서 생성
- `auto_genspark_trigger.py`: 자동 분석 트리거

### 2. 주요 기능

#### 체크리스트 자동 분석
- 체크리스트 저장 시 자동으로 Genspark 분석 실행
- 업종별 데이터 기반 맞춤형 추천 생성
- 진행률 자동 계산

#### 맞춤형 제안서 생성
- 업종별 특성 분석
- 연령대별 추천 사항
- 고민사항별 맞춤 전략

#### Google Sheets 자동 동기화
- 분석 결과 자동 저장
- 고객별 분석 이력 관리

## 📋 사용 방법

### 1. 체크리스트 완성 시 자동 분석

체크리스트를 작성하고 저장하면 자동으로 분석이 실행됩니다:

```python
# api_server.py에서 자동 실행됨
from genspark_integration import analyze_and_generate_proposal

result = analyze_and_generate_proposal(
    customer_id=customer_id,
    checklist_data=checklist_items,
    name=name,
    industry=industry,
    age_range=age_range
)
```

### 2. 수동 분석 실행

```bash
python auto_genspark_trigger.py
```

### 3. 맞춤형 제안서 생성

`custom_proposal.html`에서:
1. 업종 선택
2. 연령대 선택
3. 주요 관심사 입력
4. 체크리스트 데이터 입력
5. "제안서 생성" 클릭

→ Genspark 분석 기반 맞춤형 제안서 자동 생성

## 🔧 설정

### 업종별 데이터

`industry_data/` 폴더에 업종별 데이터가 저장됩니다:
- `미용업_YYYYMMDDHHMMSS.json`
- `요식업_YYYYMMDDHHMMSS.json`
- 등등...

### data.go.kr API 키 설정

1. https://www.data.go.kr 접속
2. API 키 발급
3. 환경변수 설정:
   ```bash
   export DATA_GO_KR_API_KEY="your_api_key_here"
   ```

또는 `data_go_kr_collector.py`에서 직접 설정:
```python
API_KEY = "your_api_key_here"
```

### 데이터 수집 실행

```bash
python data_go_kr_collector.py
```

## 📊 분석 결과 구조

```json
{
  "analysis": {
    "customer_id": "CUST_20250101120000",
    "industry": "미용업",
    "age_range": "50대",
    "progress": 65,
    "concerns": ["세금 부담", "노후 자금"],
    "recommendations": [
      "세제적격연금을 통한 노후 자금 마련",
      "건강보험을 통한 리스크 관리"
    ]
  },
  "proposal": "[미용업 개인사업자 종합 제안서]..."
}
```

## 🚀 다음 단계

1. **data.go.kr API 키 발급**
   - 실제 업종별 통계 데이터 수집

2. **Genspark Sheets Agent 연동**
   - Google Sheets 데이터를 Genspark에 업로드
   - 자동 분석 및 시각화

3. **실시간 업데이트**
   - 고객 상태 대시보드에 실시간 반영
   - 자동 알림 설정

## 📝 참고

- 분석 결과는 `checklist_data/` 폴더에 저장됩니다
- Google Sheets의 "Genspark분석" 시트에 자동 저장됩니다
- 고객 상태 대시보드에서 확인 가능합니다

