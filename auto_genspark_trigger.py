#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
체크리스트 완성 시 자동으로 Genspark 분석 트리거
"""
import json
import os
from pathlib import Path
from genspark_integration import analyze_and_generate_proposal
from sheets_manager import get_sheets_manager

CHECKLIST_DATA_DIR = Path(__file__).parent / "checklist_data"
CHECKLIST_DATA_DIR.mkdir(exist_ok=True)

def check_and_analyze():
    """체크리스트 데이터 확인 및 자동 분석"""
    if not CHECKLIST_DATA_DIR.exists():
        print("체크리스트 데이터 폴더가 없습니다.")
        return
    
    # 체크리스트 파일 찾기
    checklist_files = list(CHECKLIST_DATA_DIR.glob("*_checklist.json"))
    
    if not checklist_files:
        print("분석할 체크리스트가 없습니다.")
        return
    
    print(f"📊 {len(checklist_files)}개의 체크리스트 발견")
    print()
    
    for checklist_file in checklist_files:
        try:
            with open(checklist_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            customer_id = data.get('customer_id', '')
            if not customer_id:
                customer_id = checklist_file.stem.replace('_checklist', '')
            
            # 이미 분석된 경우 스킵
            analysis_file = CHECKLIST_DATA_DIR / f"{customer_id}_analysis.json"
            if analysis_file.exists():
                print(f"⏭️  {customer_id}: 이미 분석됨")
                continue
            
            # 분석 실행
            print(f"🔍 {customer_id} 분석 중...")
            
            name = data.get('name', '고객')
            industry = data.get('industry', '')
            age_range = data.get('age_range', '')
            
            result = analyze_and_generate_proposal(
                customer_id=customer_id,
                checklist_data=data,
                name=name,
                industry=industry,
                age_range=age_range
            )
            
            if result:
                # 분석 결과 저장
                with open(analysis_file, 'w', encoding='utf-8') as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)
                
                print(f"✅ {customer_id}: 분석 완료")
                print(f"   - 진행률: {result['analysis'].get('progress', 0)}%")
                print(f"   - 추천 사항: {len(result['analysis'].get('recommendations', []))}개")
            else:
                print(f"❌ {customer_id}: 분석 실패")
            
            print()
            
        except Exception as e:
            print(f"❌ {checklist_file.name} 처리 실패: {e}")
            print()

def main():
    print("=" * 60)
    print("Genspark 자동 분석 트리거")
    print("=" * 60)
    print()
    
    check_and_analyze()
    
    print("=" * 60)
    print("✅ 분석 완료!")
    print("=" * 60)

if __name__ == '__main__':
    main()

