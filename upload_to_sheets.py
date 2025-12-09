#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Sheets 업로드 스크립트
CSV 데이터를 Google Sheets에 자동으로 업로드합니다.
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import os
import json

# Google Sheets API 설정
SCOPE = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

def authenticate_google_sheets(credentials_file='credentials.json'):
    """Google Sheets API 인증"""
    if not os.path.exists(credentials_file):
        print("❌ credentials.json 파일이 없습니다.")
        print()
        print("📋 Google Sheets API 인증 설정 방법:")
        print("1. Google Cloud Console 접속: https://console.cloud.google.com/")
        print("2. 새 프로젝트 생성 또는 기존 프로젝트 선택")
        print("3. 'API 및 서비스' > '라이브러리'에서 'Google Sheets API' 활성화")
        print("4. 'API 및 서비스' > '사용자 인증 정보' > '사용자 인증 정보 만들기' > '서비스 계정'")
        print("5. 서비스 계정 생성 후 JSON 키 다운로드")
        print("6. 다운로드한 JSON 파일을 'credentials.json'으로 이름 변경")
        print("7. credentials.json을 이 스크립트와 같은 폴더에 배치")
        print()
        return None
    
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, SCOPE)
        client = gspread.authorize(creds)
        print("✅ Google Sheets API 인증 성공")
        return client
    except Exception as e:
        print(f"❌ 인증 실패: {e}")
        return None

def create_or_open_spreadsheet(client, spreadsheet_name):
    """스프레드시트 생성 또는 열기"""
    try:
        # 기존 스프레드시트 찾기
        spreadsheet = client.open(spreadsheet_name)
        print(f"✅ 기존 스프레드시트 열기: {spreadsheet_name}")
    except gspread.SpreadsheetNotFound:
        # 새 스프레드시트 생성
        spreadsheet = client.create(spreadsheet_name)
        print(f"✅ 새 스프레드시트 생성: {spreadsheet_name}")
        
        # 공유 설정 (읽기 권한)
        spreadsheet.share('', perm_type='anyone', role='reader')
        print("✅ 공개 읽기 권한 설정 완료")
    
    return spreadsheet

def upload_csv_to_sheet(spreadsheet, csv_file, sheet_name=None):
    """CSV 파일을 Google Sheets에 업로드"""
    if not os.path.exists(csv_file):
        print(f"❌ 파일을 찾을 수 없습니다: {csv_file}")
        return False
    
    try:
        # 시트 이름 설정
        if not sheet_name:
            sheet_name = os.path.splitext(os.path.basename(csv_file))[0]
        
        # 기존 시트가 있으면 삭제
        try:
            worksheet = spreadsheet.worksheet(sheet_name)
            spreadsheet.del_worksheet(worksheet)
        except gspread.WorksheetNotFound:
            pass
        
        # 새 시트 생성
        worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=1000, cols=20)
        
        # CSV 파일 읽기
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            data = list(reader)
        
        # 데이터 업로드
        worksheet.update('A1', data)
        
        # 헤더 행 포맷팅
        worksheet.format('A1:Z1', {
            'backgroundColor': {'red': 0.2, 'green': 0.4, 'blue': 0.8},
            'textFormat': {'bold': True, 'foregroundColor': {'red': 1.0, 'green': 1.0, 'blue': 1.0}}
        })
        
        print(f"✅ {csv_file} → {sheet_name} 업로드 완료 ({len(data)}개 행)")
        return True
        
    except Exception as e:
        print(f"❌ 업로드 실패: {e}")
        return False

def main():
    print("=" * 60)
    print("Google Sheets 업로드 스크립트")
    print("=" * 60)
    print()
    
    # Google Sheets 인증
    client = authenticate_google_sheets()
    if not client:
        return
    
    print()
    
    # 스프레드시트 이름
    spreadsheet_name = "개인사업자 재무전략 데이터"
    
    # 스프레드시트 생성 또는 열기
    spreadsheet = create_or_open_spreadsheet(client, spreadsheet_name)
    print()
    
    # CSV 파일 업로드
    csv_files = [
        ('customer_data.csv', '고객데이터'),
        ('financial_analysis.csv', '재무분석'),
        ('pension_simulation.csv', '연금시뮬레이션')
    ]
    
    print("📤 CSV 파일 업로드 중...")
    print()
    
    for csv_file, sheet_name in csv_files:
        if os.path.exists(csv_file):
            upload_csv_to_sheet(spreadsheet, csv_file, sheet_name)
        else:
            print(f"⚠️  {csv_file} 파일이 없습니다. 먼저 sample_data_generator.py를 실행하세요.")
        print()
    
    # 스프레드시트 URL 출력
    print("=" * 60)
    print("✅ 업로드 완료!")
    print("=" * 60)
    print()
    print(f"📊 스프레드시트 URL: {spreadsheet.url}")
    print()
    print("📋 다음 단계:")
    print("1. 위 URL로 스프레드시트 확인")
    print("2. Genspark Sheets Agent 접속: https://www.genspark.ai/agents?type=sheets_agent_new")
    print("3. 스프레드시트 연결")
    print("4. 자연어로 분석 요청")
    print()

if __name__ == '__main__':
    main()

