# 상세 프로필 페이지에 뒤로 가기 버튼 추가 방법

## 📝 수정할 파일
`corporate-strategy` 저장소의 `syn.html` 파일 (또는 해당 프로필 페이지)

## 🔧 추가할 코드

상세 프로필 페이지 상단 또는 하단에 다음 코드를 추가하세요:

### 옵션 1: 상단에 추가 (Header 영역)

```html
<!-- Header 영역에 추가 -->
<header>
    <div style="padding: 1rem 2rem; background: #1a202c; border-bottom: 1px solid rgba(255,255,255,0.1);">
        <a href="https://synitart.github.io/individual-strategy/" 
           style="display: inline-flex; 
                  align-items: center; 
                  gap: 0.5rem; 
                  color: #60a5fa; 
                  text-decoration: none; 
                  font-weight: 600;
                  transition: all 0.3s ease;">
            ← 개인사업자 페이지로 돌아가기
        </a>
    </div>
</header>
```

### 옵션 2: 하단에 추가 (Footer 영역)

```html
<!-- Footer 영역에 추가 -->
<footer>
    <div style="text-align: center; padding: 2rem; border-top: 1px solid rgba(255,255,255,0.1);">
        <a href="https://synitart.github.io/individual-strategy/" 
           style="display: inline-flex; 
                  align-items: center; 
                  gap: 0.5rem; 
                  color: #60a5fa; 
                  text-decoration: none; 
                  font-weight: 600;
                  padding: 0.75rem 1.5rem;
                  border: 1px solid rgba(96, 165, 250, 0.3);
                  border-radius: 8px;
                  transition: all 0.3s ease;">
            ← 개인사업자 페이지로 돌아가기
        </a>
    </div>
</footer>
```

### 옵션 3: 고정 버튼 (우측 하단)

```html
<!-- Body 태그 닫기 전에 추가 -->
<div style="position: fixed; 
            bottom: 2rem; 
            right: 2rem; 
            z-index: 1000;">
    <a href="https://synitart.github.io/individual-strategy/" 
       style="display: inline-flex; 
              align-items: center; 
              gap: 0.5rem; 
              background: linear-gradient(135deg, #667eea, #764ba2);
              color: white; 
              text-decoration: none; 
              font-weight: 600;
              padding: 1rem 1.5rem;
              border-radius: 50px;
              box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
              transition: all 0.3s ease;">
        ← 개인사업자 페이지
    </a>
</div>
```

## 🎨 스타일 통일

개인사업자 페이지와 동일한 다크 테마를 유지하려면:
- 배경: `#1a202c` 또는 `#0f172a`
- 텍스트: `#e2e8f0` 또는 `#cbd5e1`
- 링크: `#60a5fa` → `#93c5fd` (호버)
- 테두리: `rgba(255, 255, 255, 0.1)`

## 📍 권장 위치

1. **상단 Header**: 항상 보이는 위치
2. **하단 Footer**: 페이지를 다 본 후 돌아가기
3. **고정 버튼**: 스크롤해도 항상 보임

가장 추천하는 것은 **상단 Header**에 추가하는 것입니다.

