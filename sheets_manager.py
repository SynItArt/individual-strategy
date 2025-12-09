#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Sheets 데이터 관리 모듈
체크리스트, 상담 예약, 고객 데이터를 Google Sheets에 자동 저장
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from datetime import datetime
from pathlib import Path

# Google Sheets API 설정
SCOPE = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

class SheetsManager:
    """Google Sheets 관리 클래스"""
    
    def __init__(self, credentials_file='credentials.json'):
        self.credentials_file = credentials_file
        self.client = None
        self.spreadsheet = None
        self.spreadsheet_name = "개인사업자 재무전략 관리"
        
    def authenticate(self):
        """Google Sheets API 인증"""
        if not os.path.exists(self.credentials_file):
            print(f"⚠️  {self.credentials_file} 파일이 없습니다.")
            print("Google Sheets 연동을 사용하려면 credentials.json 파일이 필요합니다.")
            return False
        
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(
                self.credentials_file, SCOPE
            )
            self.client = gspread.authorize(creds)
            print("✅ Google Sheets API 인증 성공")
            return True
        except Exception as e:
            print(f"❌ Google Sheets 인증 실패: {e}")
            return False
    
    def get_or_create_spreadsheet(self):
        """스프레드시트 가져오기 또는 생성"""
        if not self.client:
            if not self.authenticate():
                return None
        
        try:
            # 기존 스프레드시트 찾기
            self.spreadsheet = self.client.open(self.spreadsheet_name)
            print(f"✅ 스프레드시트 열기: {self.spreadsheet_name}")
        except gspread.SpreadsheetNotFound:
            # 새 스프레드시트 생성
            self.spreadsheet = self.client.create(self.spreadsheet_name)
            print(f"✅ 새 스프레드시트 생성: {self.spreadsheet_name}")
            
            # 기본 시트 생성
            self._create_default_sheets()
            
            # 공유 설정 (읽기 권한)
            self.spreadsheet.share('', perm_type='anyone', role='reader')
            print("✅ 공개 읽기 권한 설정 완료")
        
        return self.spreadsheet
    
    def _create_default_sheets(self):
        """기본 시트 생성"""
        if not self.spreadsheet:
            return
        
        # 기본 시트 목록
        default_sheets = [
            ('고객정보', ['고객ID', '성명', '연락처', '이메일', '사업자명', '등록일', '최종수정일']),
            ('체크리스트', ['고객ID', '카테고리', '항목ID', '항목명', '체크여부', '체크일시']),
            ('상담예약', ['고객ID', '예약일', '예약시간', '상태', '메모', '생성일']),
            ('Genspark분석', ['고객ID', '분석타입', '차트URL', '인사이트', '생성일'])
        ]
        
        # 기본 시트 삭제 (이미 있으면)
        try:
            default_sheet = self.spreadsheet.sheet1
            self.spreadsheet.del_worksheet(default_sheet)
        except:
            pass
        
        # 시트 생성
        for sheet_name, headers in default_sheets:
            try:
                worksheet = self.spreadsheet.worksheet(sheet_name)
            except gspread.WorksheetNotFound:
                worksheet = self.spreadsheet.add_worksheet(
                    title=sheet_name, 
                    rows=1000, 
                    cols=len(headers)
                )
                # 헤더 추가
                worksheet.append_row(headers)
                # 헤더 포맷팅
                worksheet.format('A1:Z1', {
                    'backgroundColor': {'red': 0.2, 'green': 0.4, 'blue': 0.8},
                    'textFormat': {'bold': True, 'foregroundColor': {'red': 1.0, 'green': 1.0, 'blue': 1.0}}
                })
                print(f"✅ 시트 생성: {sheet_name}")
    
    def save_customer(self, customer_data):
        """고객 정보 저장"""
        if not self.spreadsheet:
            self.get_or_create_spreadsheet()
        
        if not self.spreadsheet:
            return False
        
        try:
            worksheet = self.spreadsheet.worksheet('고객정보')
            
            # 기존 고객 확인
            customer_id = customer_data.get('customer_id')
            if customer_id:
                # 기존 행 찾기
                try:
                    cell = worksheet.find(customer_id)
                    row = cell.row
                    # 업데이트
                    worksheet.update_cell(row, 2, customer_data.get('name', ''))
                    worksheet.update_cell(row, 3, customer_data.get('phone', ''))
                    worksheet.update_cell(row, 4, customer_data.get('email', ''))
                    worksheet.update_cell(row, 5, customer_data.get('business', ''))
                    worksheet.update_cell(row, 7, datetime.now().strftime('%Y%m%d%H%M%S'))
                    print(f"✅ 고객 정보 업데이트: {customer_id}")
                except gspread.exceptions.CellNotFound:
                    # 새 고객 추가
                    row = [
                        customer_id,
                        customer_data.get('name', ''),
                        customer_data.get('phone', ''),
                        customer_data.get('email', ''),
                        customer_data.get('business', ''),
                        datetime.now().strftime('%Y%m%d%H%M%S'),
                        datetime.now().strftime('%Y%m%d%H%M%S')
                    ]
                    worksheet.append_row(row)
                    print(f"✅ 새 고객 정보 저장: {customer_id}")
            else:
                print("⚠️  고객 ID가 없습니다.")
                return False
            
            return True
        except Exception as e:
            print(f"❌ 고객 정보 저장 실패: {e}")
            return False
    
    def save_checklist(self, customer_id, checklist_data):
        """체크리스트 데이터 저장"""
        if not self.spreadsheet:
            self.get_or_create_spreadsheet()
        
        if not self.spreadsheet:
            return False
        
        try:
            worksheet = self.spreadsheet.worksheet('체크리스트')
            
            # 기존 체크리스트 데이터 삭제 (고객별)
            try:
                cells = worksheet.findall(customer_id)
                for cell in cells:
                    if cell.col == 1:  # 고객ID 컬럼
                        worksheet.delete_rows(cell.row)
            except:
                pass
            
            # 체크리스트 데이터 추가
            rows_added = 0
            for category, items in checklist_data.items():
                if isinstance(items, list):
                    for item in items:
                        if isinstance(item, dict):
                            row = [
                                customer_id,
                                category,
                                item.get('id', ''),
                                item.get('text', ''),
                                'Y' if item.get('checked', False) else 'N',
                                datetime.now().strftime('%Y%m%d%H%M%S') if item.get('checked', False) else ''
                            ]
                            worksheet.append_row(row)
                            rows_added += 1
            
            print(f"✅ 체크리스트 저장 완료: {customer_id} ({rows_added}개 항목)")
            return True
        except Exception as e:
            print(f"❌ 체크리스트 저장 실패: {e}")
            return False
    
    def save_booking(self, booking_data):
        """상담 예약 저장"""
        if not self.spreadsheet:
            self.get_or_create_spreadsheet()
        
        if not self.spreadsheet:
            return False
        
        try:
            worksheet = self.spreadsheet.worksheet('상담예약')
            
            customer_id = booking_data.get('customer_id')
            
            # 기존 예약 확인 및 업데이트
            try:
                cell = worksheet.find(customer_id)
                row = cell.row
                # 업데이트
                worksheet.update_cell(row, 2, booking_data.get('date', ''))
                worksheet.update_cell(row, 3, booking_data.get('time', ''))
                worksheet.update_cell(row, 4, booking_data.get('status', 'pending'))
                worksheet.update_cell(row, 5, booking_data.get('notes', ''))
                print(f"✅ 상담 예약 업데이트: {customer_id}")
            except gspread.exceptions.CellNotFound:
                # 새 예약 추가
                row = [
                    customer_id,
                    booking_data.get('date', ''),
                    booking_data.get('time', ''),
                    booking_data.get('status', 'pending'),
                    booking_data.get('notes', ''),
                    datetime.now().strftime('%Y%m%d%H%M%S')
                ]
                worksheet.append_row(row)
                print(f"✅ 새 상담 예약 저장: {customer_id}")
            
            return True
        except Exception as e:
            print(f"❌ 상담 예약 저장 실패: {e}")
            return False
    
    def save_genspark_analysis(self, customer_id, analysis_data):
        """Genspark 분석 결과 저장"""
        if not self.spreadsheet:
            self.get_or_create_spreadsheet()
        
        if not self.spreadsheet:
            return False
        
        try:
            worksheet = self.spreadsheet.worksheet('Genspark분석')
            
            row = [
                customer_id,
                analysis_data.get('analysis_type', ''),
                analysis_data.get('chart_url', ''),
                json.dumps(analysis_data.get('insights', {}), ensure_ascii=False),
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ]
            worksheet.append_row(row)
            
            print(f"✅ Genspark 분석 결과 저장: {customer_id}")
            return True
        except Exception as e:
            print(f"❌ Genspark 분석 결과 저장 실패: {e}")
            return False
    
    def get_customer_data(self, customer_id):
        """고객 데이터 조회"""
        if not self.spreadsheet:
            self.get_or_create_spreadsheet()
        
        if not self.spreadsheet:
            return None
        
        try:
            worksheet = self.spreadsheet.worksheet('고객정보')
            cell = worksheet.find(customer_id)
            
            row = worksheet.row_values(cell.row)
            return {
                'customer_id': row[0],
                'name': row[1],
                'phone': row[2],
                'email': row[3],
                'business': row[4],
                'created_at': row[5],
                'updated_at': row[6] if len(row) > 6 else ''
            }
        except:
            return None
    
    def get_booking(self, customer_id):
        """상담 예약 조회"""
        if not self.spreadsheet:
            self.get_or_create_spreadsheet()
        
        if not self.spreadsheet:
            return None
        
        try:
            worksheet = self.spreadsheet.worksheet('상담예약')
            cell = worksheet.find(customer_id)
            
            row = worksheet.row_values(cell.row)
            return {
                'customer_id': row[0],
                'date': row[1],
                'time': row[2],
                'status': row[3],
                'notes': row[4] if len(row) > 4 else '',
                'created_at': row[5] if len(row) > 5 else ''
            }
        except:
            return None
    
    def get_spreadsheet_url(self):
        """스프레드시트 URL 반환"""
        if self.spreadsheet:
            return self.spreadsheet.url
        return None


# 싱글톤 인스턴스
_sheets_manager = None

def get_sheets_manager():
    """SheetsManager 싱글톤 인스턴스 반환"""
    global _sheets_manager
    if _sheets_manager is None:
        _sheets_manager = SheetsManager()
    return _sheets_manager

