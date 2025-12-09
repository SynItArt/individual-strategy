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

# .env 파일에서 API 키 로드 시도
def load_env_file():
    """.env 파일에서 환경변수 로드"""
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

load_env_file()

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
        
    def get_industry_statistics(self, industry_name, year=None):
        """업종별 통계 데이터 조회 (실제 API 연동)
        
        Args:
            industry_name: 업종명 (예: '미용업', '요식업')
            year: 연도 (기본값: 최근 연도)
        """
        if not year:
            year = datetime.now().year - 1  # 작년 데이터
        
        # 실제 data.go.kr API 엔드포인트는 API 키 발급 후 설정
        # 예시: 소상공인 경영현황 통계 API
        # url = f"{self.base_url}/1160100/service/GetSmpcSttusService/getSmpcSttus"
        
        # 임시로 업종별 기본 데이터 반환 (실제 API 연동 전까지)
        industry_defaults = {
            '미용업': {
                '평균매출': 80000000,
                '평균경비': 50000000,
                '평균세금': 12000000,
                '업종특성': '서비스 중심, 현금 거래 많음, 종업원 수 적음'
            },
            '요식업': {
                '평균매출': 120000000,
                '평균경비': 80000000,
                '평균세금': 18000000,
                '업종특성': '원자재비 높음, 인건비 비중 큼, 계절성 있음'
            },
            '소매업': {
                '평균매출': 60000000,
                '평균경비': 40000000,
                '평균세금': 9000000,
                '업종특성': '재고 관리 중요, 매출 증빙 체계화 필요'
            },
            '서비스업': {
                '평균매출': 90000000,
                '평균경비': 55000000,
                '평균세금': 13500000,
                '업종특성': '인적 자원 중심, 경비 증빙 중요'
            },
            '제조업': {
                '평균매출': 150000000,
                '평균경비': 100000000,
                '평균세금': 22500000,
                '업종특성': '설비 투자 큼, 원가 관리 중요'
            },
            '건설업': {
                '평균매출': 180000000,
                '평균경비': 120000000,
                '평균세금': 27000000,
                '업종특성': '프로젝트 단위, 계약금 관리 중요'
            },
            '운수업': {
                '평균매출': 100000000,
                '평균경비': 65000000,
                '평균세금': 15000000,
                '업종특성': '차량 유지비 큼, 연료비 비중 높음'
            }
        }
        
        # 기본 데이터 반환 (실제 API 연동 시 아래 주석 해제)
        if industry_name in industry_defaults:
            return {
                'result': {
                    'items': [{
                        'industry': industry_name,
                        'year': year,
                        **industry_defaults[industry_name]
                    }]
                }
            }
        
        # 실제 API 호출 (API 키가 있을 때)
        if self.api_key and self.api_key != 'YOUR_API_KEY_HERE':
            # 실제 API 호출 코드 (API 키 발급 후 활성화)
            # 주의: 실제 API 엔드포인트는 data.go.kr에서 제공하는 정확한 URL로 변경 필요
            try:
                # 예시: 소상공인 경영현황 통계 API
                # 실제 API URL은 data.go.kr에서 확인 필요
                url = f"{self.base_url}/1160100/service/GetSmpcSttusService/getSmpcSttus"
                
                params = {
                    'serviceKey': self.api_key,
                    'pageNo': 1,
                    'numOfRows': 100,
                    'resultType': 'json',
                    'year': year
                }
                
                # 업종 코드 매핑 (실제 API에 맞게 수정 필요)
                industry_code_map = {
                    '미용업': 'IND001',
                    '요식업': 'IND002',
                    '소매업': 'IND003',
                    '서비스업': 'IND004',
                    '제조업': 'IND005',
                    '건설업': 'IND006',
                    '운수업': 'IND007'
                }
                
                if industry_name in industry_code_map:
                    params['indutyCd'] = industry_code_map[industry_name]
                
                print(f"   🔗 API 호출 시도: {industry_name}")
                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()
                
                result = response.json()
                print(f"   ✅ API 호출 성공: {industry_name}")
                return result
                
            except requests.exceptions.RequestException as e:
                print(f"   ⚠️  API 호출 실패: {e}")
                print(f"   📊 기본 데이터 사용: {industry_name}")
                # API 실패 시 기본 데이터 반환
                if industry_name in industry_defaults:
                    return {
                        'result': {
                            'items': [{
                                'industry': industry_name,
                                'year': year,
                                **industry_defaults[industry_name],
                                'source': 'default_data'
                            }]
                        }
                    }
            except Exception as e:
                print(f"   ❌ 오류 발생: {e}")
                print(f"   📊 기본 데이터 사용: {industry_name}")
                if industry_name in industry_defaults:
                    return {
                        'result': {
                            'items': [{
                                'industry': industry_name,
                                'year': year,
                                **industry_defaults[industry_name],
                                'source': 'default_data'
                            }]
                        }
                    }
        
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
        industries = ['미용업', '요식업', '소매업', '서비스업', '제조업', '건설업', '운수업']
        
        collected_data = {}
        
        for industry_name in industries:
            print(f"\n📊 {industry_name} 데이터 수집 중...")
            
            # 통계 데이터 수집
            stats_data = self.get_industry_statistics(industry_name)
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

