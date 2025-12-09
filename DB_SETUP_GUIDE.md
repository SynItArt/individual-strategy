# 데이터베이스 관리 시스템 설정 가이드

## 📋 개요

체크리스트 데이터와 상담 예약 데이터를 Google Sheets에 자동으로 저장하고 관리하는 시스템입니다.

## 🚀 설정 방법

### 1단계: Google Cloud Console 설정

1. **Google Cloud Console 접속**
   - https://console.cloud.google.com/

2. **프로젝트 생성 또는 선택**
   - 새 프로젝트 생성 또는 기존 프로젝트 선택

3. **Google Sheets API 활성화**
   - 'API 및 서비스' > '라이브러리'
   - 'Google Sheets API' 검색 및 활성화
   - 'Google Drive API' 검색 및 활성화

4. **서비스 계정 생성**
   - 'API 및 서비스' > '사용자 인증 정보'
   - '사용자 인증 정보 만들기' > '서비스 계정'
   - 서비스 계정 이름 입력 (예: 'individual-strategy-sheets')
   - 역할: '편집자' 선택
   - '완료' 클릭

5. **JSON 키 다운로드**
   - 생성된 서비스 계정 클릭
   - '키' 탭 > '키 추가' > 'JSON 만들기'
   - 다운로드된 JSON 파일을 `credentials.json`으로 이름 변경

6. **프로젝트 폴더에 배치**
   ```
   Projects/individual-strategy/
   ├── credentials.json  ← 여기에 배치
   ├── sheets_manager.py
   └── api_server.py
   ```

### 2단계: 스프레드시트 생성 확인

`sheets_manager.py`를 실행하면 자동으로 다음 시트가 생성됩니다:

- **고객정보**: 고객 기본 정보
- **체크리스트**: 체크리스트 항목별 체크 상태
- **상담예약**: 상담 일정 예약 정보
- **Genspark분석**: Genspark 분석 결과

### 3단계: API 서버 실행

```bash
cd Projects/individual-strategy
python api_server.py
```

서버가 시작되면:
- `http://localhost:5000`에서 API 서버 실행
- Google Sheets 연동 상태 확인

## 📊 데이터 구조

### 고객정보 시트
| 고객ID | 성명 | 연락처 | 이메일 | 사업자명 | 등록일 | 최종수정일 |
|--------|------|--------|--------|----------|--------|------------|
| CUST_... | 홍길동 | 010-... | ... | ... | 2025-12-... | 2025-12-... |

### 체크리스트 시트
| 고객ID | 카테고리 | 항목ID | 항목명 | 체크여부 | 체크일시 |
|--------|----------|--------|--------|----------|----------|
| CUST_... | basic | name | 성명 | Y | 2025-12-... |

### 상담예약 시트
| 고객ID | 예약일 | 예약시간 | 상태 | 메모 | 생성일 |
|--------|--------|----------|------|------|--------|
| CUST_... | 2025-12-15 | 14:00 | pending | ... | 2025-12-... |

### Genspark분석 시트
| 고객ID | 분석타입 | 차트URL | 인사이트 | 생성일 |
|--------|----------|---------|----------|--------|
| CUST_... | tax_analysis | ... | {...} | 2025-12-... |

## 🔄 자동 동기화

### 체크리스트 저장 시
1. 로컬스토리지에 저장
2. API 서버로 전송 (`/api/checklist/save`)
3. 로컬 파일로 저장 (`checklist_data/{customer_id}_checklist.json`)
4. Google Sheets에 자동 업로드 (비동기)

### 상담 예약 시
1. 로컬스토리지에 저장
2. API 서버로 전송 (`/api/consultation/booking`)
3. 로컬 파일로 저장 (`checklist_data/{customer_id}_booking.json`)
4. Google Sheets에 자동 업로드 (비동기)

## 🛠 사용 방법

### Python에서 직접 사용

```python
from sheets_manager import get_sheets_manager

# SheetsManager 인스턴스 가져오기
manager = get_sheets_manager()

# 인증
if manager.authenticate():
    # 고객 정보 저장
    customer_data = {
        'customer_id': 'CUST_123',
        'name': '홍길동',
        'phone': '010-1234-5678',
        'email': 'hong@example.com',
        'business': '미용업'
    }
    manager.save_customer(customer_data)
    
    # 체크리스트 저장
    checklist_data = {
        'basic': [
            {'id': 'name', 'text': '성명', 'checked': True},
            {'id': 'phone', 'text': '연락처', 'checked': True}
        ]
    }
    manager.save_checklist('CUST_123', checklist_data)
    
    # 상담 예약 저장
    booking_data = {
        'customer_id': 'CUST_123',
        'date': '2025-12-15',
        'time': '14:00',
        'status': 'pending'
    }
    manager.save_booking(booking_data)
```

### API를 통한 사용

```javascript
// 체크리스트 저장
fetch('/api/checklist/save', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        customer_id: 'CUST_123',
        name: '홍길동',
        phone: '010-1234-5678',
        checklist: {
            basic: [...],
            documents: [...],
            concerns: [...]
        }
    })
});

// 상담 예약 저장
fetch('/api/consultation/booking', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        customer_id: 'CUST_123',
        date: '2025-12-15',
        time: '14:00',
        status: 'pending'
    })
});
```

## 🔍 데이터 조회

### 고객 정보 조회
```python
customer = manager.get_customer_data('CUST_123')
print(customer)
```

### 상담 예약 조회
```python
booking = manager.get_booking('CUST_123')
print(booking)
```

### 스프레드시트 URL 가져오기
```python
url = manager.get_spreadsheet_url()
print(f"스프레드시트 URL: {url}")
```

## ⚠️ 주의사항

1. **credentials.json 보안**
   - Git에 커밋하지 않도록 `.gitignore`에 추가
   - 공개 저장소에 업로드하지 않기

2. **API 할당량**
   - Google Sheets API는 분당 60회 요청 제한
   - 대량 데이터는 배치 처리 권장

3. **에러 처리**
   - `credentials.json`이 없어도 로컬 저장은 정상 작동
   - Google Sheets 연동 실패 시 로컬 파일로만 저장

## 🐛 문제 해결

### 인증 실패
- `credentials.json` 파일 경로 확인
- Google Sheets API 활성화 확인
- 서비스 계정 권한 확인

### 데이터 저장 실패
- 스프레드시트 공유 권한 확인
- API 할당량 확인
- 네트워크 연결 확인

## 📚 참고 자료

- [Google Sheets API 문서](https://developers.google.com/sheets/api)
- [gspread 라이브러리 문서](https://docs.gspread.org/)
- [서비스 계정 생성 가이드](https://cloud.google.com/iam/docs/service-accounts)

---

**작성일:** 2025년 12월  
**버전:** 1.0.0

© SYNDΛESIK · Individual Strategy · Empathy Strategy 2025

