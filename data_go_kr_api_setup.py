#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data.go.kr API 키 설정 및 테스트 스크립트
"""
import os
import json
from pathlib import Path

def setup_api_key():
    """API 키 설정 가이드"""
    print("=" * 70)
    print("data.go.kr API 키 설정 가이드")
    print("=" * 70)
    print()
    
    print("📋 API 키 발급 방법:")
    print("1. https://www.data.go.kr 접속")
    print("2. 회원가입 및 로그인")
    print("3. '마이페이지' > '활용신청' > '오픈 API' 메뉴로 이동")
    print("4. 원하는 API 선택 (예: 소상공인 경영현황 통계)")
    print("5. 활용신청 후 승인 대기")
    print("6. 승인 후 발급받은 API 키 복사")
    print()
    
    print("🔑 API 키 설정 방법:")
    print()
    print("방법 1: 환경변수로 설정 (권장)")
    print("  Windows PowerShell:")
    print("    $env:DATA_GO_KR_API_KEY='your_api_key_here'")
    print()
    print("  Windows CMD:")
    print("    set DATA_GO_KR_API_KEY=your_api_key_here")
    print()
    print("  Linux/Mac:")
    print("    export DATA_GO_KR_API_KEY='your_api_key_here'")
    print()
    
    print("방법 2: .env 파일 생성 (프로젝트 루트에)")
    print("  DATA_GO_KR_API_KEY=your_api_key_here")
    print()
    
    print("방법 3: 직접 입력 (이 스크립트 사용)")
    print()
    
    # API 키 입력 받기
    api_key = input("API 키를 입력하세요 (Enter로 건너뛰기): ").strip()
    
    if api_key:
        # .env 파일 생성
        env_file = Path(__file__).parent / ".env"
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(f"DATA_GO_KR_API_KEY={api_key}\n")
        
        print()
        print(f"✅ API 키가 {env_file} 파일에 저장되었습니다.")
        print()
        print("⚠️  주의: .env 파일은 .gitignore에 추가하여 Git에 커밋하지 마세요!")
        print()
        
        # 환경변수로도 설정 (현재 세션)
        os.environ['DATA_GO_KR_API_KEY'] = api_key
        print("✅ 현재 세션의 환경변수도 설정되었습니다.")
    else:
        print()
        print("⏭️  API 키 입력을 건너뛰었습니다.")
        print("   기본 데이터를 사용하여 테스트할 수 있습니다.")
    
    print()
    print("=" * 70)
    print("다음 단계:")
    print("=" * 70)
    print("1. python data_go_kr_collector.py 실행하여 데이터 수집")
    print("2. python auto_genspark_trigger.py 실행하여 분석 테스트")
    print("=" * 70)

def test_api_connection():
    """API 연결 테스트"""
    api_key = os.getenv('DATA_GO_KR_API_KEY', '')
    
    if not api_key or api_key == 'YOUR_API_KEY_HERE':
        print("⚠️  API 키가 설정되지 않았습니다.")
        print("   기본 데이터를 사용합니다.")
        return False
    
    print("🔍 API 키 확인됨")
    print(f"   키 길이: {len(api_key)} 문자")
    print("   (실제 API 호출은 data_go_kr_collector.py에서 테스트하세요)")
    return True

if __name__ == '__main__':
    setup_api_key()
    print()
    test_api_connection()

