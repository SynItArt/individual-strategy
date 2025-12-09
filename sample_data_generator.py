#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
샘플 데이터 생성 스크립트
Genspark Sheets Agent 테스트를 위한 샘플 데이터를 생성합니다.
"""

import csv
import random
from datetime import datetime, timedelta

def generate_customer_data(num_customers=20):
    """고객 재무 데이터 생성"""
    industries = ['미용업', '요식업', '소매업', '서비스업', '제조업', '건설업', '운수업']
    data = [['고객명', '업종', '연령', '사업소득(원)', '세금(원)', '월지출(원)', '가입보험', '연금가입여부', '등록일']]
    
    for i in range(1, num_customers + 1):
        industry = random.choice(industries)
        age = random.randint(35, 60)
        
        # 업종별 평균 소득 설정
        base_income = {
            '미용업': 80000000,
            '요식업': 120000000,
            '소매업': 60000000,
            '서비스업': 90000000,
            '제조업': 150000000,
            '건설업': 180000000,
            '운수업': 100000000
        }
        
        income = base_income.get(industry, 80000000) + random.randint(-20000000, 30000000)
        tax = int(income * random.uniform(0.12, 0.18))
        monthly_expense = int(income / 12 * random.uniform(0.4, 0.6))
        
        insurance = random.choice(['종신보험', '건강보험', '상해보험', '없음'])
        pension = random.choice(['Y', 'N'])
        
        # 등록일 (최근 1년 내)
        days_ago = random.randint(0, 365)
        reg_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
        
        data.append([
            f'고객{i:03d}',
            industry,
            age,
            income,
            tax,
            monthly_expense,
            insurance,
            pension,
            reg_date
        ])
    
    return data

def generate_financial_analysis_data():
    """재무 분석 데이터 생성"""
    data = [['년도', '월', '사업소득(원)', '경비(원)', '세금(원)', '순이익(원)']]
    
    for year in [2022, 2023, 2024]:
        for month in range(1, 13):
            income = random.randint(5000000, 15000000)
            expense = int(income * random.uniform(0.4, 0.6))
            tax = int((income - expense) * random.uniform(0.10, 0.15))
            profit = income - expense - tax
            
            data.append([year, month, income, expense, tax, profit])
    
    return data

def generate_pension_simulation_data():
    """연금 시뮬레이션 데이터 생성"""
    data = [['불입금액(원)', '불입기간(년)', '예상수익률(%)', '세액공제(원)', '예상연금액(원)']]
    
    payment_amounts = [3000000, 4000000, 5000000, 6000000]
    periods = [10, 15, 20, 25, 30]
    returns = [3.0, 3.5, 4.0, 4.5, 5.0]
    
    for amount in payment_amounts:
        for period in periods:
            for ret in returns:
                tax_credit = int(amount * 0.12)  # 12% 세액공제
                # 복리 계산 (간단화)
                future_value = int(amount * period * (1 + ret/100) ** (period/2))
                monthly_pension = int(future_value / (period * 12))
                
                data.append([amount, period, ret, tax_credit, monthly_pension])
    
    return data

def save_to_csv(data, filename):
    """데이터를 CSV 파일로 저장"""
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"✅ {filename} 생성 완료 ({len(data)-1}개 행)")

def main():
    print("=" * 60)
    print("Genspark Sheets Agent용 샘플 데이터 생성")
    print("=" * 60)
    print()
    
    # 고객 데이터 생성
    print("📊 고객 재무 데이터 생성 중...")
    customer_data = generate_customer_data(20)
    save_to_csv(customer_data, 'customer_data.csv')
    print()
    
    # 재무 분석 데이터 생성
    print("📈 재무 분석 데이터 생성 중...")
    financial_data = generate_financial_analysis_data()
    save_to_csv(financial_data, 'financial_analysis.csv')
    print()
    
    # 연금 시뮬레이션 데이터 생성
    print("💰 연금 시뮬레이션 데이터 생성 중...")
    pension_data = generate_pension_simulation_data()
    save_to_csv(pension_data, 'pension_simulation.csv')
    print()
    
    print("=" * 60)
    print("✅ 모든 샘플 데이터 생성 완료!")
    print("=" * 60)
    print()
    print("📋 다음 단계:")
    print("1. Google Sheets에 CSV 파일 업로드")
    print("2. Genspark Sheets Agent에 연결")
    print("3. 자연어로 분석 요청:")
    print("   - '업종별 평균 사업소득을 보여줘'")
    print("   - '연령대별 세금 부담을 비교해줘'")
    print("   - '세금 절감 가능 구간을 분석해줘'")
    print()

if __name__ == '__main__':
    main()
