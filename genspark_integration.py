#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genspark Sheets Agent 연동 모듈
체크리스트 데이터를 분석하여 맞춤형 제안서 생성
"""
import json
import os
from datetime import datetime
from pathlib import Path
from sheets_manager import get_sheets_manager

class GensparkIntegration:
    """Genspark 연동 클래스"""
    
    def __init__(self):
        self.sheets_manager = get_sheets_manager()
        self.industry_data_dir = Path(__file__).parent / "industry_data"
        self.industry_data_dir.mkdir(exist_ok=True)
    
    def analyze_checklist(self, customer_id, checklist_data, industry=None, age_range=None):
        """체크리스트 데이터 분석
        
        Args:
            customer_id: 고객 ID
            checklist_data: 체크리스트 데이터
            industry: 업종
            age_range: 연령대
        """
        try:
            # 업종별 데이터 로드
            industry_data = self._load_industry_data(industry) if industry else None
            
            # 체크리스트 진행률 계산
            progress = self._calculate_progress(checklist_data)
            
            # 고민사항 분석
            concerns = checklist_data.get('concerns', [])
            concern_other = checklist_data.get('concern_other', '')
            
            # 준비된 서류 분석
            documents = checklist_data.get('documents', [])
            
            # 분석 결과 생성
            analysis = {
                'customer_id': customer_id,
                'industry': industry or '미입력',
                'age_range': age_range or '미입력',
                'progress': progress,
                'concerns': concerns,
                'concern_other': concern_other,
                'documents_prepared': len(documents),
                'recommendations': self._generate_recommendations(industry, age_range, concerns, industry_data),
                'created_at': datetime.now().strftime('%Y%m%d%H%M%S')
            }
            
            # Google Sheets에 저장
            if self.sheets_manager.authenticate():
                self.sheets_manager.save_genspark_analysis(customer_id, {
                    'analysis_type': 'checklist_analysis',
                    'chart_url': None,
                    'insights': analysis
                })
            
            return analysis
        except Exception as e:
            print(f"❌ 분석 실패: {e}")
            return None
    
    def _load_industry_data(self, industry):
        """업종별 데이터 로드"""
        if not self.industry_data_dir.exists():
            return None
        
        # 최신 데이터 파일 찾기
        pattern = f"{industry}_*.json"
        files = list(self.industry_data_dir.glob(pattern))
        
        if files:
            latest_file = max(files, key=os.path.getmtime)
            try:
                with open(latest_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return None
        
        return None
    
    def _calculate_progress(self, checklist_data):
        """체크리스트 진행률 계산"""
        total = 0
        checked = 0
        
        # 준비 서류 체크 수
        documents = checklist_data.get('documents', [])
        checked += len(documents)
        total += 20  # 예상 서류 항목 수
        
        # 고민사항 체크 수
        concerns = checklist_data.get('concerns', [])
        checked += len(concerns)
        total += 10  # 예상 고민사항 수
        
        if total == 0:
            return 0
        return round((checked / total) * 100)
    
    def _generate_recommendations(self, industry, age_range, concerns, industry_data):
        """추천 사항 생성"""
        recommendations = []
        
        # 업종별 추천
        if industry:
            if industry == '미용업':
                recommendations.append('세제적격연금을 통한 노후 자금 마련')
                recommendations.append('건강보험을 통한 리스크 관리')
            elif industry == '요식업':
                recommendations.append('사업자 신용카드 활용으로 경비 처리')
                recommendations.append('종업원 복리후생 경비 인정')
            elif industry == '소매업':
                recommendations.append('매출 증빙 관리 체계화')
                recommendations.append('재고 관리 최적화')
        
        # 연령대별 추천
        if age_range:
            if '50대' in age_range or '60대' in age_range:
                recommendations.append('노후 자금 마련이 시급합니다')
                recommendations.append('세제적격연금 가입 권장')
            elif '30대' in age_range or '40대' in age_range:
                recommendations.append('장기 재무 설계 수립')
                recommendations.append('리스크 관리 강화')
        
        # 고민사항별 추천
        for concern in concerns:
            if '세금' in concern:
                recommendations.append('세무 최적화 전략 수립')
            if '노후' in concern:
                recommendations.append('연금 상품 검토')
            if '리스크' in concern:
                recommendations.append('보험 포트폴리오 점검')
        
        # 업종 데이터 기반 추천
        if industry_data:
            stats = industry_data.get('statistics', {})
            if stats:
                recommendations.append(f'{industry} 업종 평균 데이터 기반 맞춤 전략')
        
        return list(set(recommendations))  # 중복 제거
    
    def generate_proposal(self, customer_id, analysis, name):
        """맞춤형 제안서 생성"""
        try:
            industry = analysis.get('industry', '')
            age_range = analysis.get('age_range', '')
            concerns = analysis.get('concerns', [])
            recommendations = analysis.get('recommendations', [])
            
            # 제안서 생성
            proposal = f"""[{industry} 개인사업자 종합 제안서]

대상: {industry} 개인사업자 · {age_range}
주요 관심사: {', '.join(concerns) if concerns else '종합 재무 설계'}

{name} 대표님을 위한 맞춤형 재무전략을 제안합니다.

[업종별 특성 분석]
{industry} 업종의 특성을 고려한 재무전략을 수립했습니다.

[주요 제안 사항]
"""
            
            for i, rec in enumerate(recommendations[:5], 1):
                proposal += f"{i}. {rec}\n"
            
            proposal += """
[다음 단계]
상세한 상담을 통해 더욱 구체적인 제안을 드리겠습니다.

※ 본 제안서는 Genspark AI와 data.go.kr 데이터를 기반으로 생성되었습니다.
더 정확한 분석을 위해 상담을 권장합니다.
"""
            
            return proposal
        except Exception as e:
            print(f"❌ 제안서 생성 실패: {e}")
            return None

def analyze_and_generate_proposal(customer_id, checklist_data, name, industry=None, age_range=None):
    """체크리스트 분석 및 제안서 생성 (편의 함수)"""
    integration = GensparkIntegration()
    
    # 분석 실행
    analysis = integration.analyze_checklist(customer_id, checklist_data, industry, age_range)
    
    if not analysis:
        return None
    
    # 제안서 생성
    proposal = integration.generate_proposal(customer_id, analysis, name)
    
    return {
        'analysis': analysis,
        'proposal': proposal
    }

