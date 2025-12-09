#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
업종별 기본 데이터 초기화 스크립트
"""
import json
from datetime import datetime
from pathlib import Path

# 데이터 저장 경로
DATA_DIR = Path(__file__).parent / "industry_data"
DATA_DIR.mkdir(exist_ok=True)

# 업종별 기본 데이터
INDUSTRY_DATA = {
    '미용업': {
        'statistics': {
            'result': {
                'items': [{
                    'industry': '미용업',
                    'year': 2024,
                    '평균매출': 80000000,
                    '평균경비': 50000000,
                    '평균세금': 12000000,
                    '업종특성': '서비스 중심, 현금 거래 많음, 종업원 수 적음',
                    '주요경비': ['인건비', '임대료', '재료비', '광고비'],
                    '세금절세팁': ['경비 증빙 철저히', '현금영수증 발급', '부가가치세 신고 최적화']
                }]
            }
        },
        'collected_at': datetime.now().strftime('%Y%m%d%H%M%S')
    },
    '요식업': {
        'statistics': {
            'result': {
                'items': [{
                    'industry': '요식업',
                    'year': 2024,
                    '평균매출': 120000000,
                    '평균경비': 80000000,
                    '평균세금': 18000000,
                    '업종특성': '원자재비 높음, 인건비 비중 큼, 계절성 있음',
                    '주요경비': ['원자재비', '인건비', '임대료', '광고비'],
                    '세금절세팁': ['원자재 구매 증빙', '종업원 복리후생 경비', '부가가치세 신고 최적화']
                }]
            }
        },
        'collected_at': datetime.now().strftime('%Y%m%d%H%M%S')
    },
    '소매업': {
        'statistics': {
            'result': {
                'items': [{
                    'industry': '소매업',
                    'year': 2024,
                    '평균매출': 60000000,
                    '평균경비': 40000000,
                    '평균세금': 9000000,
                    '업종특성': '재고 관리 중요, 매출 증빙 체계화 필요',
                    '주요경비': ['상품매입비', '임대료', '인건비', '광고비'],
                    '세금절세팁': ['재고 관리 체계화', '매출 증빙 철저히', '부가가치세 신고 최적화']
                }]
            }
        },
        'collected_at': datetime.now().strftime('%Y%m%d%H%M%S')
    },
    '서비스업': {
        'statistics': {
            'result': {
                'items': [{
                    'industry': '서비스업',
                    'year': 2024,
                    '평균매출': 90000000,
                    '평균경비': 55000000,
                    '평균세금': 13500000,
                    '업종특성': '인적 자원 중심, 경비 증빙 중요',
                    '주요경비': ['인건비', '임대료', '광고비', '기타 경비'],
                    '세금절세팁': ['경비 증빙 체계화', '세금계산서 발급', '부가가치세 신고 최적화']
                }]
            }
        },
        'collected_at': datetime.now().strftime('%Y%m%d%H%M%S')
    },
    '제조업': {
        'statistics': {
            'result': {
                'items': [{
                    'industry': '제조업',
                    'year': 2024,
                    '평균매출': 150000000,
                    '평균경비': 100000000,
                    '평균세금': 22500000,
                    '업종특성': '설비 투자 큼, 원가 관리 중요',
                    '주요경비': ['원자재비', '인건비', '설비비', '임대료'],
                    '세금절세팁': ['설비 투자 최적화', '원가 관리 체계화', '부가가치세 신고 최적화']
                }]
            }
        },
        'collected_at': datetime.now().strftime('%Y%m%d%H%M%S')
    },
    '건설업': {
        'statistics': {
            'result': {
                'items': [{
                    'industry': '건설업',
                    'year': 2024,
                    '평균매출': 180000000,
                    '평균경비': 120000000,
                    '평균세금': 27000000,
                    '업종특성': '프로젝트 단위, 계약금 관리 중요',
                    '주요경비': ['자재비', '인건비', '장비비', '임대료'],
                    '세금절세팁': ['계약금 관리 체계화', '자재 구매 증빙', '부가가치세 신고 최적화']
                }]
            }
        },
        'collected_at': datetime.now().strftime('%Y%m%d%H%M%S')
    },
    '운수업': {
        'statistics': {
            'result': {
                'items': [{
                    'industry': '운수업',
                    'year': 2024,
                    '평균매출': 100000000,
                    '평균경비': 65000000,
                    '평균세금': 15000000,
                    '업종특성': '차량 유지비 큼, 연료비 비중 높음',
                    '주요경비': ['연료비', '차량 유지비', '인건비', '보험료'],
                    '세금절세팁': ['차량 경비 증빙', '연료비 관리', '부가가치세 신고 최적화']
                }]
            }
        },
        'collected_at': datetime.now().strftime('%Y%m%d%H%M%S')
    }
}

def init_industry_data():
    """업종별 기본 데이터 파일 생성"""
    print("=" * 60)
    print("업종별 기본 데이터 초기화")
    print("=" * 60)
    print()
    
    for industry_name, data in INDUSTRY_DATA.items():
        filename = f"{industry_name}_{data['collected_at']}.json"
        filepath = DATA_DIR / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ {industry_name} 데이터 생성: {filename}")
    
    print()
    print("=" * 60)
    print(f"✅ 총 {len(INDUSTRY_DATA)}개 업종 데이터 생성 완료!")
    print("=" * 60)

if __name__ == '__main__':
    init_industry_data()

