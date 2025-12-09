# 메시지 확인 가이드

## 📋 개요

상담 신청 메시지를 확인하는 방법을 안내합니다.

## 🔍 메시지 확인 방법

### 1. 웹 페이지에서 확인 (권장)

**URL:** `https://synitart.github.io/individual-strategy/messages.html`

- 모든 상담 신청 메시지를 한눈에 확인
- 고객 정보, 연락처, 메시지 내용 확인
- 전화/문자 바로 걸기 기능

### 2. Google Sheets에서 확인

**스프레드시트 이름:** "개인사업자 재무전략 관리"

**시트:**
- **고객정보**: 고객 기본 정보
- **체크리스트**: 체크리스트 진행 상황
- **상담예약**: 상담 일정 예약 정보

**확인 방법:**
1. Google Sheets 접속
2. "개인사업자 재무전략 관리" 스프레드시트 열기
3. 각 시트에서 데이터 확인

### 3. 로컬 파일에서 확인

**경로:** `checklist_data/`

**파일 형식:**
- `{customer_id}_checklist.json` - 체크리스트 데이터
- `{customer_id}_booking.json` - 상담 예약 데이터

**확인 방법:**
```bash
# Windows
cd Projects\individual-strategy\checklist_data
dir

# 파일 내용 확인
type {customer_id}_checklist.json
```

### 4. SMS/카카오톡에서 확인

**전화번호:** 010-2088-5383

고객이 직접 전송한 메시지는 휴대폰에서 확인하실 수 있습니다.

## 📊 데이터 구조

### 체크리스트 데이터 (`{customer_id}_checklist.json`)
```json
{
  "customer_id": "CUST_1234567890_abc",
  "name": "홍길동",
  "phone": "010-1234-5678",
  "email": "hong@example.com",
  "business": "미용업",
  "interest": "세금 절세",
  "checklist": {
    "basic": [...],
    "documents": [...],
    "concerns": [...]
  },
  "created_at": "20251215143025"
}
```

### 상담 예약 데이터 (`{customer_id}_booking.json`)
```json
{
  "customer_id": "CUST_1234567890_abc",
  "date": "2025-12-15",
  "time": "14:00",
  "status": "pending",
  "created_at": "20251215143025"
}
```

## 🔔 실시간 알림 (향후 구현)

- 이메일 알림
- SMS 알림
- 푸시 알림

## 📱 빠른 액션

### 메시지 페이지에서
- **전화하기**: 고객에게 바로 전화
- **문자 보내기**: 고객에게 문자 전송
- **상세 보기**: 고객 정보 상세 확인

### Google Sheets에서
- 필터링 및 정렬
- 데이터 분석
- Genspark 연동

## ⚠️ 주의사항

1. **개인정보 보호**
   - 고객 정보는 안전하게 관리
   - 외부 공유 금지

2. **데이터 백업**
   - 정기적으로 Google Sheets 백업
   - 로컬 파일도 백업 권장

3. **접근 권한**
   - 메시지 확인은 관리자만 가능
   - Google Sheets 공유 설정 확인

## 🐛 문제 해결

### 메시지가 안 보이는 경우
1. API 서버가 실행 중인지 확인
2. `checklist_data` 폴더에 파일이 있는지 확인
3. Google Sheets 연동 상태 확인

### Google Sheets 접근 불가
1. credentials.json 파일 확인
2. Google Sheets API 권한 확인
3. 스프레드시트 공유 설정 확인

---

**마지막 업데이트:** 2025년 12월  
**메시지 확인 페이지:** https://synitart.github.io/individual-strategy/messages.html

