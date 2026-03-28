export interface PolicyProcessInsight {
  insight: string;
  source_document: string;
}

export interface LlmAnalyseResponse {
  applicant_snapshot: string;
  supportive_factors: string[];
  risk_factors: string[];
  policy_process_insights: PolicyProcessInsight[];
  missing_information: string[];
  recommended_review_actions: string[];
  analyst_rationale_draft: string;
  confidence_limitations: string;
}

export type LoanDecision = 'Approve' | 'Review' | 'Reject';

export interface PaybackEndpointResponse {
  loan_decision: LoanDecision;
  payback_proba: number;
  insights: LlmAnalyseResponse;
}
