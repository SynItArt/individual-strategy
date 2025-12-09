# Genspark Sheets Agent 통합 가이드

## 📋 개요

이 가이드는 Genspark Sheets Agent를 개인사업자 재무전략 프로젝트에 통합하는 방법을 설명합니다.

## 🚀 빠른 시작

### 1단계: 샘플 데이터 생성

```bash
python sample_data_generator.py
```

생성되는 파일:
- `customer_data.csv` - 고객 재무 데이터 (20명)
- `financial_analysis.csv` - 재무 분석 데이터 (3년치)
- `pension_simulation.csv` - 연금 시뮬레이션 데이터

### 2단계: Google Sheets에 업로드

#### 방법 A: 자동 업로드 (권장)

```bash
python upload_to_sheets.py
```

**필수 준비사항:**
1. Google Cloud Console에서 프로젝트 생성
2. Google Sheets API 활성화
3. 서비스 계정 생성 및 JSON 키 다운로드
4. `credentials.json` 파일로 저장

#### 방법 B: 수동 업로드

1. Google Sheets 새 문서 생성
2. CSV 파일을 드래그 앤 드롭으로 업로드
3. 데이터 확인

### 3단계: Genspark Sheets Agent 연결

1. [Genspark Sheets Agent](https://www.genspark.ai/agents?type=sheets_agent_new) 접속
2. Google Sheets 데이터 연결
3. 자연어로 분석 요청

**예시 질문:**
- "업종별 평균 사업소득을 보여줘"
- "연령대별 세금 부담을 비교해줘"
- "세금 절감 가능 구간을 분석해줘"
- "연금 시뮬레이션 결과를 시각화해줘"

### 4단계: 차트를 PPTX에 삽입

Genspark에서 생성된 차트를 이미지로 저장한 후:

```python
from create_presentation import add_chart_slide, create_presentation

# 프레젠테이션 생성
prs = create_presentation()

# 차트 슬라이드 추가
add_chart_slide(
    prs, 
    chart_image_path="genspark_chart.png",
    title="업종별 평균 사업소득 분석",
    subtitle="Genspark Sheets Agent 분석 결과"
)

# 저장
prs.save('개인사업자_재무전략_차트포함.pptx')
```

## 📊 데이터 구조

### 고객 데이터 (customer_data.csv)
- 고객명, 업종, 연령
- 사업소득, 세금, 월지출
- 가입보험, 연금가입여부
- 등록일

### 재무 분석 데이터 (financial_analysis.csv)
- 년도, 월
- 사업소득, 경비, 세금, 순이익

### 연금 시뮬레이션 데이터 (pension_simulation.csv)
- 불입금액, 불입기간
- 예상수익률, 세액공제, 예상연금액

## 🔧 고급 활용

### 자동화 워크플로우

1. **데이터 수집** → `sample_data_generator.py`
2. **Google Sheets 업로드** → `upload_to_sheets.py`
3. **Genspark 분석** → 수동 또는 API (향후)
4. **차트 다운로드** → 수동 저장
5. **PPTX 생성** → `create_presentation.py` + `add_chart_slide()`

### PPTX에 여러 차트 삽입

```python
# 여러 차트를 한 슬라이드에 배치
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(slide)

# 차트 1 (왼쪽)
add_image_to_slide(slide, "chart1.png", 
                   left=Inches(0.5), top=Inches(2), 
                   width=Inches(4.5), height=Inches(3))

# 차트 2 (오른쪽)
add_image_to_slide(slide, "chart2.png", 
                   left=Inches(5), top=Inches(2), 
                   width=Inches(4.5), height=Inches(3))
```

## 📝 체크리스트

### 초기 설정
- [ ] Google Cloud Console 프로젝트 생성
- [ ] Google Sheets API 활성화
- [ ] 서비스 계정 생성 및 credentials.json 다운로드
- [ ] Python 패키지 설치 (`pip install -r requirements.txt`)

### 데이터 준비
- [ ] 샘플 데이터 생성 (`sample_data_generator.py`)
- [ ] Google Sheets에 업로드 (`upload_to_sheets.py`)
- [ ] 데이터 검증

### Genspark 연동
- [ ] Genspark Sheets Agent 접속
- [ ] Google Sheets 연결
- [ ] 샘플 분석 요청
- [ ] 결과 확인

### PPTX 통합
- [ ] 차트 이미지 다운로드
- [ ] `add_chart_slide()` 함수 테스트
- [ ] 최종 PPTX 생성

## 🐛 문제 해결

### credentials.json 오류
- 파일이 올바른 위치에 있는지 확인
- 서비스 계정이 Google Sheets API에 접근 권한이 있는지 확인
- JSON 파일 형식이 올바른지 확인

### 이미지 삽입 실패
- 이미지 파일 경로 확인
- 파일 형식 확인 (PNG, JPG 지원)
- 파일 크기 확인 (너무 크면 압축 필요)

### Google Sheets 업로드 실패
- 인터넷 연결 확인
- API 할당량 확인
- 스프레드시트 공유 권한 확인

## 📚 참고 자료

- [Genspark Sheets Agent](https://www.genspark.ai/agents?type=sheets_agent_new)
- [Google Sheets API 문서](https://developers.google.com/sheets/api)
- [python-pptx 문서](https://python-pptx.readthedocs.io/)

## 💡 다음 단계

1. 실제 고객 데이터로 테스트
2. 자동화 스크립트 개발
3. 웹사이트에 대시보드 추가
4. 실시간 데이터 연동

---

**작성일:** 2025년 12월  
**버전:** 1.0.0

© SYNDΛESIK · Individual Strategy · Empathy Strategy 2025

