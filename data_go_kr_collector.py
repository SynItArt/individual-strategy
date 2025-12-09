#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data.go.kr API 데이터 수집 스크립트
업종별 통계 데이터를 수집하여 데이터베이스에 저장
"""
import requests
import json
import os
from datetime import datetime
from pathlib import Path
import time

# data.go.kr API 키 (환경변수 또는 설정 파일에서 가져오기)
API_KEY = os.getenv('DATA_GO_KR_API_KEY', 'YOUR_API_KEY_HERE')

# 데이터 저장 경로
DATA_DIR = Path(__file__).parent / "industry_data"
DATA_DIR.mkdir(exist_ok=True)

class DataGoKrCollector:
    """data.go.kr API 데이터 수집 클래스"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY
        self.base_url = "http://apis.data.go.kr"
        
    def get_industry_statistics(self, industry_code, year=None):
        """업종별 통계 데이터 조회
        
        Args:
            industry_code: 업종 코드
            year: 연도 (기본값: 최근 연도)
        """
        if not year:
            year = datetime.now().year - 1  # 작년 데이터
        
        # 예시: 소상공인 경영현황 통계 API
        # 실제 API는 data.go.kr에서 제공하는 API에 맞게 수정 필요
        url = f"{self.base_url}/1160100/service/GetSmpcSttusService/getSmpcSttus"
        
        params = {
            'serviceKey': self.api_key,
            'pageNo': 1,
            'numOfRows': 100,
            'resultType': 'json',
            'indutyCd': industry_code,
            'year': year
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ API 호출 실패: {e}")
            return None
    
    def get_tax_statistics(self, industry_code):
        """업종별 세금 통계 데이터 조회"""
        # 국세청 세무 통계 API 예시
        url = f"{self.base_url}/15000000/tax/taxStatistics"
        
        params = {
            'serviceKey': self.api_key,
            'indutyCd': industry_code,
            'resultType': 'json'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ 세금 통계 API 호출 실패: {e}")
            return None
    
    def save_industry_data(self, industry_name, data):
        """업종별 데이터 저장"""
        filename = f"{industry_name}_{datetime.now().strftime('%Y%m%d')}.json"
        filepath = DATA_DIR / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 데이터 저장 완료: {filepath}")
        return filepath
    
    def collect_all_industries(self):
        """모든 주요 업종 데이터 수집"""
        industries = {
            '미용업': 'IND001',
            '요식업': 'IND002',
            '소매업': 'IND003',
            '서비스업': 'IND004',
            '제조업': 'IND005',
            '건설업': 'IND006',
            '운수업': 'IND007'
        }
        
        collected_data = {}
        
        for industry_name, industry_code in industries.items():
            print(f"\n📊 {industry_name} 데이터 수집 중...")
            
            # 통계 데이터 수집
            stats_data = self.get_industry_statistics(industry_code)
            if stats_data:
                collected_data[industry_name] = {
                    'statistics': stats_data,
                    'collected_at': datetime.now().strftime('%Y%m%d%H%M%S')
                }
                
                # 파일로 저장
                self.save_industry_data(industry_name, collected_data[industry_name])
            
            # API 호출 제한 고려 (1초 대기)
            time.sleep(1)
        
        # 전체 데이터 통합 저장
        summary_file = DATA_DIR / f"industry_summary_{datetime.now().strftime('%Y%m%d')}.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(collected_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 전체 데이터 수집 완료: {summary_file}")
        return collected_data

def main():
    print("=" * 60)
    print("data.go.kr 업종별 데이터 수집")
    print("=" * 60)
    print()
    
    if API_KEY == 'YOUR_API_KEY_HERE':
        print("⚠️  API 키가 설정되지 않았습니다.")
        print()
        print("📋 data.go.kr API 키 발급 방법:")
        print("1. https://www.data.go.kr 접속")
        print("2. 회원가입 및 로그인")
        print("3. '마이페이지' > '활용신청' > '오픈 API'")
        print("4. 원하는 API 선택 후 활용신청")
        print("5. 발급받은 API 키를 환경변수로 설정:")
        print("   Windows: set DATA_GO_KR_API_KEY=your_api_key")
        print("   Linux/Mac: export DATA_GO_KR_API_KEY=your_api_key")
        print()
        return
    
    collector = DataGoKrCollector()
    
    # 모든 업종 데이터 수집
    data = collector.collect_all_industries()
    
    print()
    print("=" * 60)
    print("✅ 데이터 수집 완료!")
    print("=" * 60)
    print()
    print(f"📁 저장 위치: {DATA_DIR}")
    print(f"📊 수집된 업종 수: {len(data)}")
    print()
    print("📋 다음 단계:")
    print("1. 수집된 데이터를 Google Sheets에 업로드")
    print("2. Genspark Sheets Agent에 연결")
    print("3. 맞춤형 제안서 생성에 활용")
    print()

if __name__ == '__main__':
    main()

