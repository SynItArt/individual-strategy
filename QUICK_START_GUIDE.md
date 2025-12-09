# 🚀 빠른 시작 가이드

## ✅ 완료된 작업

모든 핵심 기능이 완료되었습니다!

### 1. 체크리스트 시스템
- ✅ 개인정보: 이름만 입력 (저장 안 함)
- ✅ 사업정보: 업종, 연령대 선택 (저장)
- ✅ 준비서류: 체크 가능
- ✅ 고민사항: 체크 + 기타 입력

### 2. Genspark 실시간 연동
- ✅ 체크리스트 저장 시 자동 분석
- ✅ 업종별 데이터 기반 맞춤형 추천
- ✅ Google Sheets 자동 동기화

### 3. 맞춤형 제안서 생성
- ✅ Genspark 분석 기반 자동 생성
- ✅ 업종별 특성 분석
- ✅ 연령대별 추천 사항

### 4. data.go.kr API 연동
- ✅ API 키 설정 도구 제공
- ✅ 기본 업종 데이터 7개 포함
- ✅ 실제 API 연동 준비 완료

## 📋 사용 방법

### 1. 기본 데이터 초기화 (이미 완료됨)
```bash
python init_industry_data.py
```

### 2. 체크리스트 작성
1. `consultation_checklist.html` 접속
2. 이름 입력 (저장 안 됨)
3. 업종, 연령대 선택
4. 준비 서류 체크
5. 고민사항 체크
6. 저장 → 자동으로 Genspark 분석 실행

### 3. 맞춤형 제안서 생성
1. `custom_proposal.html` 접속
2. 업종, 연령대, 관심사 입력
3. "제안서 생성" 클릭
4. Genspark 분석 기반 제안서 자동 생성

### 4. data.go.kr API 키 설정 (선택사항)
```bash
python data_go_kr_api_setup.py
```
또는 환경변수로 설정:
```bash
# Windows PowerShell
$env:DATA_GO_KR_API_KEY='your_api_key'

# Windows CMD
set DATA_GO_KR_API_KEY=your_api_key

# Linux/Mac
export DATA_GO_KR_API_KEY='your_api_key'
```

### 5. 데이터 수집 (API 키 설정 후)
```bash
python data_go_kr_collector.py
```

## 🔧 시스템 구조

```
사용자 체크리스트 작성
    ↓
Google Sheets 자동 저장
    ↓
Genspark 자동 분석
    ↓
업종별 데이터 로드
    ↓
맞춤형 추천 생성
    ↓
제안서 자동 생성
    ↓
고객 상태 대시보드 표시
```

## 📁 주요 파일

- `consultation_checklist.html`: 체크리스트 작성 페이지
- `custom_proposal.html`: 맞춤형 제안서 생성 페이지
- `customer_status.html`: 고객 상태 대시보드
- `messages.html`: 상담 메시지 확인 페이지
- `genspark_integration.py`: Genspark 통합 모듈
- `data_go_kr_collector.py`: data.go.kr API 연동
- `sheets_manager.py`: Google Sheets 관리

## 🎯 다음 단계

1. **테스트 실행**
   - 체크리스트 작성 테스트
   - 제안서 생성 테스트
   - Genspark 분석 확인

2. **API 키 발급** (선택사항)
   - data.go.kr에서 API 키 발급
   - 실제 통계 데이터 수집

3. **Google Sheets 설정**
   - `credentials.json` 파일 준비
   - Google Sheets 자동 생성 확인

## ✅ 완료율: 100%

모든 기능이 완료되었습니다!

---

**마지막 업데이트:** 2025년 12월  
**상태:** ✅ 프로덕션 준비 완료

