# **Risk Factor and Reason Codes Dictionary**

**Document ID:** RF-RSN-004  
**Version:** 1.0  
**Effective Date:** 2026-01-01  
**Document Owner:** Retail Credit Risk Governance  
**Classification:** Internal Use Only

---

# **1\. Purpose**

This document defines the standardized risk factor taxonomy and associated reason codes used in unsecured consumer loan underwriting. It is intended to support consistent interpretation of applicant risk, improve decision explainability, and ensure that analyst notes, model-supported explanations, and internal review outcomes use a shared vocabulary.

This dictionary provides a structured mapping between underwriting observations, model-relevant features, business-friendly explanations, and standardized adverse or cautionary reason codes.

---

# **2\. Scope**

This dictionary applies to:

* Manual underwriting reviews  
* Model-supported case explanations  
* Approval, review, and rejection rationales  
* Internal analyst notes  
* Exception review summaries  
* Escalation cases  
* Audit and quality assurance reviews  
* AI-assisted analyst support tools that generate decision explanations

This document does not replace underwriting policy or decision thresholds. It is a translation and standardization reference for how risk observations should be described.

---

# **3\. Dictionary Objectives**

The objectives of this dictionary are to:

1. Standardize how risk factors are described across teams and systems  
2. Improve clarity and consistency in approval, review, and rejection rationale  
3. Translate technical model signals into business-friendly language  
4. Support auditable and explainable decisions  
5. Reduce vague or subjective analyst commentary  
6. Enable consistent downstream communication and review workflows

---

# **4\. Core Principles for Using Reason Codes**

## **4.1 Reason Codes Must Be Evidence-Based**

A reason code may only be used when the underlying risk factor is supported by application data, verified documentation, policy interpretation, or a documented case review finding.

## **4.2 Reason Codes Must Be Specific**

Analysts must prefer specific reason codes over generic statements. For example, “high debt burden relative to income” is preferable to “financial profile weak.”

## **4.3 Reason Codes Must Be Business-Understandable**

Reason codes should be understandable without requiring technical model knowledge. They should describe the financial or policy issue, not only the model behavior.

## **4.4 Reason Codes Must Not Use Protected Characteristic Language**

Reason codes must never cite gender, marital status, or any protected characteristic as a basis for adverse treatment. Such attributes must not appear in final approval, review, or rejection explanations.

## **4.5 Multiple Reason Codes May Apply**

A final case may contain more than one valid reason code. Where multiple factors materially influence the decision, the analyst should identify the primary and, where needed, secondary contributing reasons.

## **4.6 Reason Codes Are Not a Substitute for Judgment**

Reason codes support consistency, but they do not replace full-case review. Analysts must ensure that the selected codes accurately reflect the actual case rationale.

---

# **5\. Structure of the Dictionary**

Each entry in this dictionary contains:

* Reason code ID  
* Risk factor name  
* Category  
* Description  
* Typical trigger conditions  
* Typical interpretation  
* Suggested analyst wording  
* Suggested customer-safe wording where relevant  
* Notes on usage restrictions or cautions

---

# **6\. Reason Code Categories**

The reason codes in this dictionary are grouped into the following categories:

1. Affordability and repayment capacity  
2. Credit quality and risk profile  
3. Employment and income stability  
4. Loan structure and proportionality  
5. Documentation and verification  
6. Product fit and loan purpose  
7. Case handling and escalation support  
8. Positive or compensating strength indicators

---

# **7\. Affordability and Repayment Capacity Reason Codes**

## **7.1 RC-A01 — High Debt-to-Income Ratio**

**Category:** Affordability and repayment capacity

**Description:**  
The applicant’s debt burden is elevated relative to income, creating concern that repayment may not be sustainable.

**Typical Trigger Conditions:**

* Debt-to-income ratio near or above internal tolerance  
* Existing obligations appear high relative to earnings  
* Repayment burden likely to strain monthly cash flow

**Typical Interpretation:**  
This is a primary affordability concern and is frequently used in review or rejection decisions.

**Suggested Analyst Wording:**  
Debt-to-income ratio is elevated relative to verified income and weakens confidence in sustainable repayment capacity.

**Suggested Customer-Safe Wording:**  
Current debt obligations appear high relative to income.

**Usage Notes:**  
This code should be used only where the debt burden is materially relevant to repayment assessment.

---

## **7.2 RC-A02 — Insufficient Income for Requested Obligation**

**Category:** Affordability and repayment capacity

**Description:**  
Declared or verified income does not appear sufficient to support the requested loan under reasonable affordability assumptions.

**Typical Trigger Conditions:**

* Income too low relative to requested loan amount  
* Income insufficient after considering debt burden and pricing  
* Repayment would likely create financial stress

**Typical Interpretation:**  
This code is commonly used as a primary rejection or strong caution code.

**Suggested Analyst Wording:**  
Verified income does not adequately support the requested loan amount and associated repayment burden.

**Suggested Customer-Safe Wording:**  
Available income does not sufficiently support the requested credit amount.

**Usage Notes:**  
This code should reflect a clear affordability concern rather than a minor limitation.

---

## **7.3 RC-A03 — Borderline Affordability**

**Category:** Affordability and repayment capacity

**Description:**  
The affordability profile is not clearly unacceptable, but repayment capacity appears close to the bank’s tolerance and requires further review.

**Typical Trigger Conditions:**

* Debt-to-income ratio close to the upper acceptable range  
* Moderate income with relatively high loan request  
* Mixed affordability indicators

**Typical Interpretation:**  
This code is generally appropriate for manual review rather than direct rejection.

**Suggested Analyst Wording:**  
Affordability appears borderline and requires additional review before final decisioning.

**Suggested Customer-Safe Wording:**  
Additional review is needed to confirm affordability.

**Usage Notes:**  
This code is intended for review-stage decisions and should not be used where the affordability failure is already clear.

---

## **7.4 RC-A04 — Unstable Cash Flow Pattern**

**Category:** Affordability and repayment capacity

**Description:**  
The applicant’s income or account activity suggests irregular cash flow, reducing confidence in repayment continuity.

**Typical Trigger Conditions:**

* Irregular salary deposits  
* Material income volatility  
* Evidence of significant month-to-month cash instability

**Typical Interpretation:**  
This code supports caution, review, or rejection depending on severity and documentation quality.

**Suggested Analyst Wording:**  
Cash flow appears irregular or unstable, reducing confidence in the applicant’s ability to sustain repayment over time.

**Suggested Customer-Safe Wording:**  
Income or cash flow pattern appears inconsistent.

**Usage Notes:**  
This code should be grounded in document review or verified income pattern analysis.

---

## **7.5 RC-A05 — Signs of Financial Stress**

**Category:** Affordability and repayment capacity

**Description:**  
Available information suggests the applicant may already be experiencing financial strain.

**Typical Trigger Conditions:**

* Repeated overdraft behavior  
* Persistent near-zero balances  
* Existing repayment pressure visible in account activity  
* Documented evidence of ongoing financial stress

**Typical Interpretation:**  
This code may strengthen a review or rejection rationale, especially when combined with weak affordability.

**Suggested Analyst Wording:**  
The financial profile shows signs of existing repayment stress, weakening confidence in additional borrowing capacity.

**Suggested Customer-Safe Wording:**  
Current financial obligations indicate potential repayment strain.

**Usage Notes:**  
This code should not be used solely on the basis of one isolated account event.

---

# **8\. Credit Quality and Risk Profile Reason Codes**

## **8.1 RC-C01 — Low Credit Score**

**Category:** Credit quality and risk profile

**Description:**  
The applicant’s credit score is below the bank’s preferred or acceptable range for the relevant product tier.

**Typical Trigger Conditions:**

* Credit score materially below target level  
* Score indicates elevated historical repayment risk

**Typical Interpretation:**  
This is a common adverse reason code and may serve as a primary factor in rejection.

**Suggested Analyst Wording:**  
Credit score falls below the bank’s acceptable range and indicates elevated repayment risk.

**Suggested Customer-Safe Wording:**  
Credit history does not meet current lending requirements.

**Usage Notes:**  
This code should be used in conjunction with policy and not as a stand-alone substitute for broader review.

---

## **8.2 RC-C02 — Borderline Credit Profile**

**Category:** Credit quality and risk profile

**Description:**  
The applicant’s credit profile is near the minimum acceptable range and requires contextual review.

**Typical Trigger Conditions:**

* Score close to policy threshold  
* Mixed credit indicators  
* Weaknesses present but not clearly disqualifying

**Typical Interpretation:**  
This code is generally appropriate for manual review cases.

**Suggested Analyst Wording:**  
Credit profile is borderline acceptable and requires additional contextual review.

**Suggested Customer-Safe Wording:**  
Additional review is needed due to the current credit profile.

**Usage Notes:**  
This code is most useful when the credit profile is neither clearly strong nor clearly unacceptable.

---

## **8.3 RC-C03 — Adverse Risk Grade**

**Category:** Credit quality and risk profile

**Description:**  
The internal risk grade or subgrade falls into a range associated with elevated non-repayment risk.

**Typical Trigger Conditions:**

* Grade/subgrade in weaker internal risk band  
* Risk tier not aligned with standard approval profile

**Typical Interpretation:**  
This code supports caution, review, or rejection depending on policy and compensating strengths.

**Suggested Analyst Wording:**  
Internal risk grade indicates elevated repayment risk relative to approvable portfolio norms.

**Suggested Customer-Safe Wording:**  
Overall risk profile does not meet current lending standards.

**Usage Notes:**  
This code should be interpreted together with affordability and documentation quality.

---

## **8.4 RC-C04 — Mixed Credit Signals**

**Category:** Credit quality and risk profile

**Description:**  
Credit indicators do not align cleanly, requiring deeper review before decisioning.

**Typical Trigger Conditions:**

* Acceptable score but weak risk grade  
* Borderline score with otherwise stronger profile  
* Model output and bureau-style indicators point in different directions

**Typical Interpretation:**  
This code is primarily a review-stage explanation.

**Suggested Analyst Wording:**  
Credit indicators are mixed and do not support a clear automated outcome without further analyst assessment.

**Suggested Customer-Safe Wording:**  
Additional review is needed due to mixed credit signals.

**Usage Notes:**  
Use this code when the credit profile is genuinely mixed, not merely weak.

---

## **8.5 RC-C05 — Elevated Probability of Non-Repayment**

**Category:** Credit quality and risk profile

**Description:**  
Model-supported or policy-aligned risk signals indicate a heightened probability that the loan will not be repaid as agreed.

**Typical Trigger Conditions:**

* Weak model payback probability  
* Multiple aligned negative risk indicators  
* Internal risk analysis indicates heightened expected default risk

**Typical Interpretation:**  
This code may support rejection or escalation but must be translated into business terms.

**Suggested Analyst Wording:**  
The overall risk profile indicates a heightened likelihood of non-repayment based on combined credit and affordability indicators.

**Suggested Customer-Safe Wording:**  
The application presents a higher level of repayment risk than the bank can accept.

**Usage Notes:**  
This code should not be presented as a purely technical model output without supporting business interpretation.

---

# **9\. Employment and Income Stability Reason Codes**

## **9.1 RC-E01 — Unstable Employment Profile**

**Category:** Employment and income stability

**Description:**  
The employment profile does not provide sufficient confidence in recurring repayment capacity.

**Typical Trigger Conditions:**

* Frequent job changes  
* Short employment duration  
* Temporary or uncertain work status  
* Employment profile inconsistent with stable repayment assumptions

**Typical Interpretation:**  
This code supports caution, especially where affordability depends heavily on continued income.

**Suggested Analyst Wording:**  
Employment profile appears unstable and reduces confidence in the continuity of income available for repayment.

**Suggested Customer-Safe Wording:**  
Current employment profile does not provide sufficient confidence in ongoing repayment capacity.

**Usage Notes:**  
Use this code only when employment instability materially affects the review.

---

## **9.2 RC-E02 — Income Source Requires Further Verification**

**Category:** Employment and income stability

**Description:**  
The available documentation does not yet provide enough confidence in the claimed income source.

**Typical Trigger Conditions:**

* Missing employment verification  
* Unclear salary source  
* Self-employment income insufficiently supported  
* Alternative income source not fully documented

**Typical Interpretation:**  
This code is most often used in pending review cases.

**Suggested Analyst Wording:**  
The declared income source requires additional verification before a final affordability assessment can be made.

**Suggested Customer-Safe Wording:**  
Additional information is needed to confirm income details.

**Usage Notes:**  
This code is appropriate where the issue is verifiability, not necessarily inadequacy.

---

## **9.3 RC-E03 — Income Volatility**

**Category:** Employment and income stability

**Description:**  
Income appears materially variable over time, reducing confidence in stable repayment.

**Typical Trigger Conditions:**

* Large changes in monthly earnings  
* Irregular self-employment income  
* Variable credits without clear recurring pattern

**Typical Interpretation:**  
This code supports review or rejection depending on severity and available reserves or strengths.

**Suggested Analyst Wording:**  
Income pattern appears volatile, which weakens confidence in stable long-term repayment capacity.

**Suggested Customer-Safe Wording:**  
Income pattern appears inconsistent over time.

**Usage Notes:**  
This code should be based on actual document patterns rather than assumption.

---

## **9.4 RC-E04 — Employment Status Not Supportive of Loan Request**

**Category:** Employment and income stability

**Description:**  
The declared employment status does not adequately support the requested loan under standard policy assumptions.

**Typical Trigger Conditions:**

* Unemployed applicant without eligible alternate income basis  
* Non-standard work arrangement with insufficient support  
* Employment category outside normal approval profile

**Typical Interpretation:**  
This code is often used in rejection or escalation contexts.

**Suggested Analyst Wording:**  
Declared employment status does not provide sufficient support for the requested credit exposure under current policy.

**Suggested Customer-Safe Wording:**  
Current employment circumstances do not sufficiently support the requested loan.

**Usage Notes:**  
Use this code with care and ensure it is supported by policy and documentation.

---

# **10\. Loan Structure and Proportionality Reason Codes**

## **10.1 RC-L01 — Loan Amount Too High Relative to Income**

**Category:** Loan structure and proportionality

**Description:**  
The requested loan amount appears disproportionate to the applicant’s income profile.

**Typical Trigger Conditions:**

* High requested amount with moderate or low income  
* Loan request inconsistent with demonstrated repayment capacity

**Typical Interpretation:**  
This is a common affordability and proportionality code.

**Suggested Analyst Wording:**  
Requested loan amount appears too high relative to the applicant’s verified income and overall repayment profile.

**Suggested Customer-Safe Wording:**  
Requested credit amount is not proportionate to current income.

**Usage Notes:**  
This code should be used where proportionality is a meaningful issue rather than a minor caution.

---

## **10.2 RC-L02 — Pricing Burden Increases Repayment Risk**

**Category:** Loan structure and proportionality

**Description:**  
The offered interest rate materially increases the applicant’s repayment burden and weakens affordability.

**Typical Trigger Conditions:**

* Elevated interest rate combined with marginal affordability  
* Payment burden increases significantly under pricing terms

**Typical Interpretation:**  
This code is often secondary to affordability but may become material in borderline cases.

**Suggested Analyst Wording:**  
The pricing structure increases repayment burden and contributes to affordability pressure in this case.

**Suggested Customer-Safe Wording:**  
Loan pricing increases the required repayment burden.

**Usage Notes:**  
This code should normally be used together with another affordability-related reason code.

---

## **10.3 RC-L03 — Loan Structure Requires Manual Review**

**Category:** Loan structure and proportionality

**Description:**  
The overall structure of the requested loan is not clearly unacceptable, but requires analyst review due to proportionality concerns.

**Typical Trigger Conditions:**

* Moderate affordability with relatively high loan amount  
* Mixed signals between income, amount, and risk tier  
* Structure near policy tolerance boundaries

**Typical Interpretation:**  
This is primarily a review-stage code.

**Suggested Analyst Wording:**  
The requested loan structure warrants manual review due to proportionality concerns relative to the applicant profile.

**Suggested Customer-Safe Wording:**  
Additional review is needed to assess the suitability of the requested loan structure.

**Usage Notes:**  
This code should be used when the concern is meaningful but not decisive.

---

# **11\. Documentation and Verification Reason Codes**

## **11.1 RC-D01 — Income Not Adequately Supported by Documentation**

**Category:** Documentation and verification

**Description:**  
Available financial documents do not sufficiently support the declared income level.

**Typical Trigger Conditions:**

* Income documents incomplete  
* Payslip values materially lower than declared income  
* Bank statements do not support claimed earnings  
* Supporting evidence too limited for confidence

**Typical Interpretation:**  
This code is commonly used in review or rejection decisions.

**Suggested Analyst Wording:**  
Declared income is not adequately supported by the documentation provided.

**Suggested Customer-Safe Wording:**  
The information provided does not sufficiently confirm current income.

**Usage Notes:**  
This code should be used only when the support gap is material.

---

## **11.2 RC-D02 — Employment Verification Incomplete**

**Category:** Documentation and verification

**Description:**  
The current file does not provide sufficient support for the applicant’s declared employment status.

**Typical Trigger Conditions:**

* Missing employer confirmation  
* Inconsistent work status across records  
* Employment claim not reasonably evidenced

**Typical Interpretation:**  
This is generally a review or pending clarification code.

**Suggested Analyst Wording:**  
Employment status has not been sufficiently verified based on the current documentation set.

**Suggested Customer-Safe Wording:**  
Additional information is needed to confirm current employment details.

**Usage Notes:**  
Use this code when the issue is incomplete support, not necessarily a contradiction.

---

## **11.3 RC-D03 — Material Information Inconsistency**

**Category:** Documentation and verification

**Description:**  
The application contains material inconsistencies between declared information and submitted documentation.

**Typical Trigger Conditions:**

* Declared income conflicts with documents  
* Employment status differs across records  
* Loan purpose not aligned with supporting explanation  
* Key applicant details do not reconcile

**Typical Interpretation:**  
This code may justify review, escalation, or rejection depending on the severity and resolvability of the inconsistency.

**Suggested Analyst Wording:**  
Material inconsistencies were identified between the application and supporting documentation, reducing confidence in the reliability of the case file.

**Suggested Customer-Safe Wording:**  
Information provided in the application could not be fully reconciled with supporting records.

**Usage Notes:**  
This code should be used only for meaningful inconsistencies that affect decision confidence.

---

## **11.4 RC-D04 — Documentation Insufficient for Final Decision**

**Category:** Documentation and verification

**Description:**  
The current case file does not contain enough reliable information to support a final underwriting decision.

**Typical Trigger Conditions:**

* Missing core documents  
* Documents unreadable or incomplete  
* Key facts unverifiable  
* Supporting evidence too limited to assess affordability or stability

**Typical Interpretation:**  
This code is suitable for pending review, follow-up, or rejection where unresolved after reasonable request.

**Suggested Analyst Wording:**  
The documentation currently on file is insufficient to support a final underwriting decision.

**Suggested Customer-Safe Wording:**  
Additional documentation is required before the application can be fully assessed.

**Usage Notes:**  
This code should be distinguished from cases where documents are present but contradictory.

---

## **11.5 RC-D05 — Document Integrity Concern**

**Category:** Documentation and verification

**Description:**  
One or more submitted documents present structural or content issues that reduce confidence in their reliability.

**Typical Trigger Conditions:**

* Missing expected fields  
* Unusual formatting  
* Apparent edits or inconsistencies  
* Partial submission that prevents reasonable interpretation

**Typical Interpretation:**  
This code supports escalation, clarification, or referral under separate review procedures.

**Suggested Analyst Wording:**  
Certain submitted documents contain integrity or reliability concerns that limit their use in underwriting assessment.

**Suggested Customer-Safe Wording:**  
Additional verification is required regarding submitted documentation.

**Usage Notes:**  
This code should not be used casually and may trigger separate process requirements.

---

# **12\. Product Fit and Loan Purpose Reason Codes**

## **12.1 RC-P01 — Loan Purpose Requires Additional Review**

**Category:** Product fit and loan purpose

**Description:**  
The stated loan purpose is not clearly ineligible, but requires further review to confirm product fit or risk interpretation.

**Typical Trigger Conditions:**

* Vague purpose  
* Purpose category associated with higher scrutiny  
* Potential policy ambiguity

**Typical Interpretation:**  
This code is generally used for manual review.

**Suggested Analyst Wording:**  
The stated loan purpose requires additional review to confirm policy fit and associated risk interpretation.

**Suggested Customer-Safe Wording:**  
Additional review is needed to confirm the purpose of the requested loan.

**Usage Notes:**  
Use this code when product fit is unclear but not clearly prohibited.

---

## **12.2 RC-P02 — Ineligible Loan Purpose**

**Category:** Product fit and loan purpose

**Description:**  
The requested loan purpose falls outside approved consumer lending policy.

**Typical Trigger Conditions:**

* Purpose category excluded by product rules  
* Use case not permitted under unsecured personal lending scope

**Typical Interpretation:**  
This is a strong rejection code.

**Suggested Analyst Wording:**  
The stated loan purpose is not eligible under current product policy.

**Suggested Customer-Safe Wording:**  
The requested use of funds is not eligible under the current product.

**Usage Notes:**  
This code should be supported by documented product policy.

---

## **12.3 RC-P03 — Loan Purpose Increases Risk Sensitivity**

**Category:** Product fit and loan purpose

**Description:**  
The stated purpose is permitted, but it raises caution because it may be associated with financial stress or weaker repayment resilience.

**Typical Trigger Conditions:**

* Emergency or stress-related spending purpose  
* Discretionary purpose in a weak affordability profile  
* Purpose category requiring higher scrutiny in marginal cases

**Typical Interpretation:**  
This code generally acts as a secondary reason rather than a sole basis for adverse decisioning.

**Suggested Analyst Wording:**  
The stated loan purpose increases case sensitivity and warrants additional caution when considered alongside the broader financial profile.

**Suggested Customer-Safe Wording:**  
The intended use of funds requires additional consideration as part of the overall review.

**Usage Notes:**  
This code should never be used as the sole reason for decline without supporting financial concerns.

---

# **13\. Case Handling and Escalation Support Reason Codes**

## **13.1 RC-H01 — Additional Information Required**

**Category:** Case handling and escalation support

**Description:**  
The application cannot be finalized without further information or clarification from the applicant.

**Typical Trigger Conditions:**

* Missing or incomplete data  
* Unclear documentation  
* Unresolved case facts  
* Borderline decision dependent on clarification

**Typical Interpretation:**  
This is a neutral operational code used for pending review status.

**Suggested Analyst Wording:**  
Additional information is required before the application can be assessed to a final outcome.

**Suggested Customer-Safe Wording:**  
Additional information is needed to continue review of the application.

**Usage Notes:**  
This code should not be used as a final rejection reason.

---

## **13.2 RC-H02 — Case Requires Senior Review**

**Category:** Case handling and escalation support

**Description:**  
The case cannot be finalized within standard analyst authority and requires escalation.

**Typical Trigger Conditions:**

* Potential exception case  
* Policy interpretation ambiguity  
* High-risk but non-standard profile  
* Case exceeds delegated decision authority

**Typical Interpretation:**  
This is an internal-only escalation support code.

**Suggested Analyst Wording:**  
The application requires senior review due to policy, authority, or case complexity considerations.

**Suggested Customer-Safe Wording:**  
The application requires additional internal review.

**Usage Notes:**  
This code is intended for internal workflow use rather than customer-facing explanations.

---

## **13.3 RC-H03 — Exception Consideration Supported by Compensating Factors**

**Category:** Case handling and escalation support

**Description:**  
A case weakness exists, but meaningful documented strengths may justify exception review.

**Typical Trigger Conditions:**

* One moderate policy weakness  
* Strong income and stable employment  
* Strong credit profile despite one limited concern  
* Other documented compensating strengths

**Typical Interpretation:**  
This code supports escalation or exception pathway review, not automatic approval.

**Suggested Analyst Wording:**  
Although the case presents a policy concern, documented compensating strengths may justify exception consideration.

**Suggested Customer-Safe Wording:**  
The application requires additional internal consideration based on the overall profile.

**Usage Notes:**  
This code should not be used where a critical exclusion criterion is triggered.

---

# **14\. Positive and Compensating Strength Reason Codes**

## **14.1 RC-S01 — Strong Verified Income**

**Category:** Positive or compensating strength indicators

**Description:**  
Verified income level provides meaningful support for repayment capacity.

**Typical Trigger Conditions:**

* Income clearly supports requested amount  
* Documentation confirms stable earnings  
* Financial profile stronger than minimum expectations

**Typical Interpretation:**  
This code may offset a moderate weakness but does not override critical policy breaches.

**Suggested Analyst Wording:**  
Verified income level is a meaningful strength and supports the applicant’s repayment capacity.

**Suggested Customer-Safe Wording:**  
Income profile supports the requested borrowing level.

**Usage Notes:**  
This code should be used when the strength is material, not merely acceptable.

---

## **14.2 RC-S02 — Strong Credit History**

**Category:** Positive or compensating strength indicators

**Description:**  
The applicant’s credit profile indicates a strong pattern of historical repayment behavior.

**Typical Trigger Conditions:**

* Strong credit score  
* Positive repayment history  
* Risk profile stronger than standard minimums

**Typical Interpretation:**  
This code can support approval or offset one moderate concern.

**Suggested Analyst Wording:**  
Credit history is a meaningful strength and supports confidence in repayment behavior.

**Suggested Customer-Safe Wording:**  
Credit history is supportive of the application.

**Usage Notes:**  
This code should not be used to offset clear affordability failure.

---

## **14.3 RC-S03 — Stable Employment Supports Repayment**

**Category:** Positive or compensating strength indicators

**Description:**  
The applicant’s employment profile supports confidence in the continuity of income.

**Typical Trigger Conditions:**

* Stable salaried employment  
* Clear recurring earnings pattern  
* Employment evidence consistent and supportive

**Typical Interpretation:**  
This code is often used as a supporting approval factor.

**Suggested Analyst Wording:**  
Employment profile appears stable and supports confidence in continued repayment capacity.

**Suggested Customer-Safe Wording:**  
Employment profile supports the application.

**Usage Notes:**  
This code should be grounded in verified employment evidence.

---

## **14.4 RC-S04 — Loan Amount Proportionate to Financial Profile**

**Category:** Positive or compensating strength indicators

**Description:**  
The requested loan amount appears reasonable relative to the applicant’s income and overall risk profile.

**Typical Trigger Conditions:**

* Requested amount conservative relative to income  
* Repayment burden appears manageable  
* Structure aligned with profile strength

**Typical Interpretation:**  
This code supports approval and may help contextualize moderate caution factors.

**Suggested Analyst Wording:**  
Requested loan amount appears proportionate to the applicant’s verified financial profile.

**Suggested Customer-Safe Wording:**  
Requested amount appears consistent with current financial capacity.

**Usage Notes:**  
This code should be used where proportionality is clearly favorable.

---

## **14.5 RC-S05 — Documentation Supports Declared Profile**

**Category:** Positive or compensating strength indicators

**Description:**  
Submitted documents consistently support the applicant’s declared income, employment, and financial profile.

**Typical Trigger Conditions:**

* Income documents align with application  
* Employment evidence consistent  
* No material contradictions identified

**Typical Interpretation:**  
This code strengthens confidence in case reliability.

**Suggested Analyst Wording:**  
Supporting documentation is consistent with the declared profile and strengthens confidence in the case file.

**Suggested Customer-Safe Wording:**  
Provided information supports the application details.

**Usage Notes:**  
This code is especially useful in cases where documentation quality is a key strength.

---

# **15\. Mapping Between Typical Features and Reason Code Families**

The following feature-level observations commonly map to the reason code families below.

## **15.1 Annual Income**

Annual income may map to:

* RC-A02 — Insufficient Income for Requested Obligation  
* RC-A03 — Borderline Affordability  
* RC-S01 — Strong Verified Income

## **15.2 Debt-to-Income Ratio**

Debt-to-income ratio may map to:

* RC-A01 — High Debt-to-Income Ratio  
* RC-A03 — Borderline Affordability  
* RC-A05 — Signs of Financial Stress

## **15.3 Credit Score**

Credit score may map to:

* RC-C01 — Low Credit Score  
* RC-C02 — Borderline Credit Profile  
* RC-S02 — Strong Credit History

## **15.4 Loan Amount**

Loan amount may map to:

* RC-L01 — Loan Amount Too High Relative to Income  
* RC-L03 — Loan Structure Requires Manual Review  
* RC-S04 — Loan Amount Proportionate to Financial Profile

## **15.5 Interest Rate**

Interest rate may map to:

* RC-L02 — Pricing Burden Increases Repayment Risk  
* RC-A03 — Borderline Affordability

## **15.6 Employment Status**

Employment status may map to:

* RC-E01 — Unstable Employment Profile  
* RC-E02 — Income Source Requires Further Verification  
* RC-E04 — Employment Status Not Supportive of Loan Request  
* RC-S03 — Stable Employment Supports Repayment

## **15.7 Loan Purpose**

Loan purpose may map to:

* RC-P01 — Loan Purpose Requires Additional Review  
* RC-P02 — Ineligible Loan Purpose  
* RC-P03 — Loan Purpose Increases Risk Sensitivity

## **15.8 Grade/Subgrade**

Grade or subgrade may map to:

* RC-C03 — Adverse Risk Grade  
* RC-C04 — Mixed Credit Signals  
* RC-C05 — Elevated Probability of Non-Repayment

---

# **16\. Guidance for Model-Supported Explanations**

## **16.1 Translating Technical Signals into Business Language**

When model explanations are used, the analyst or support tool should convert technical feature contributions into business language using the reason code framework.

Examples:

* A low predicted payback probability supported by high debt burden should map to RC-A01 and RC-A02 rather than only “negative model contribution.”  
* A strong positive contribution from credit score may map to RC-S02.  
* A weak contribution from loan amount proportionality may map to RC-L01.

## **16.2 Priority of Reason Selection**

Where multiple technical signals exist, priority should generally be given to the business reason that is:

1. Most material to the final decision  
2. Most understandable in financial terms  
3. Best supported by policy and evidence  
4. Least dependent on technical model language

## **16.3 Limits on Model Translation**

Model-driven reason mapping must not:

* Cite protected characteristics  
* Present speculative causal claims  
* Exaggerate the certainty of the model  
* Replace document-based or policy-based review

---

# **17\. Reason Code Selection Rules**

## **17.1 Primary Reason Code**

The primary reason code should reflect the strongest and most decision-relevant factor.

## **17.2 Secondary Reason Codes**

Secondary codes may be used where additional factors materially influenced the outcome.

## **17.3 Avoid Over-Coding**

Analysts should avoid listing excessive reason codes. A concise and accurate rationale is preferable to a long but diluted list.

## **17.4 Internal vs Customer-Facing Usage**

Some codes are suitable only for internal review and should not be communicated externally in their full form. Internal operational codes include:

* RC-H02 — Case Requires Senior Review  
* RC-H03 — Exception Consideration Supported by Compensating Factors  
* RC-D05 — Document Integrity Concern

Customer-facing wording should be selected carefully and should avoid unnecessary operational details.

---

# **18\. Reason Code Usage Examples**

## **18.1 Approval Example**

**Case Pattern:**  
Strong credit score, stable full-time employment, moderate debt-to-income ratio, loan amount proportionate to income, documents consistent.

**Possible Codes:**

* RC-S01 — Strong Verified Income  
* RC-S02 — Strong Credit History  
* RC-S03 — Stable Employment Supports Repayment  
* RC-S04 — Loan Amount Proportionate to Financial Profile  
* RC-S05 — Documentation Supports Declared Profile

---

## **18.2 Review Example**

**Case Pattern:**  
Income appears acceptable, but debt-to-income ratio is near upper tolerance, credit profile is borderline, and employment support requires minor follow-up.

**Possible Codes:**

* RC-A03 — Borderline Affordability  
* RC-C02 — Borderline Credit Profile  
* RC-E02 — Income Source Requires Further Verification  
* RC-H01 — Additional Information Required

---

## **18.3 Reject Example**

**Case Pattern:**  
Low credit score, high debt burden, requested amount too high for verified income, and documents do not sufficiently support the declared earnings.

**Possible Codes:**

* RC-C01 — Low Credit Score  
* RC-A01 — High Debt-to-Income Ratio  
* RC-L01 — Loan Amount Too High Relative to Income  
* RC-D01 — Income Not Adequately Supported by Documentation

---

# **19\. Prohibited Usage Patterns**

Reason codes must not be used in the following ways:

* As stand-alone decisions without full case review  
* As direct substitutes for underwriting policy  
* To justify outcomes based on protected characteristics  
* To conceal uncertainty where clarification is required  
* To overstate the precision of model-based findings  
* To replace factual analyst notes with generic labels only

---

# **20\. Analyst Note Integration Guidance**

When reason codes are used in analyst notes, they should be integrated into plain-language rationale.

## **20.1 Strong Example**

**Decision:** Reject

**Rationale:** Verified income does not sufficiently support the requested loan amount, and debt burden appears elevated relative to earnings. Credit score is below the bank’s acceptable range, and the current profile does not provide sufficient confidence in sustainable repayment capacity.

## **20.2 Weak Example**

**Decision:** Reject

**Rationale:** RC-A01, RC-C01, RC-D01.

The above example is not sufficient because it lacks narrative explanation.

---

# **21\. Use of This Dictionary in Analyst Support Tools**

This dictionary may be used by internal analyst support tools to:

* convert feature-level model signals into standardized business explanations  
* propose reason codes for analyst review  
* generate first-draft case summaries  
* support consistent approval, review, and rejection language  
* improve retrieval quality in knowledge-based AI systems

All AI-generated reason code suggestions must remain subject to analyst confirmation.

---

# **22\. Review and Maintenance**

This dictionary must be reviewed annually or sooner if triggered by:

* updates to underwriting policy  
* changes to internal risk model features  
* quality assurance findings  
* audit observations  
* changes in adverse action or explanation standards  
* updates to analyst support tooling

All changes must be version-controlled and approved by Retail Credit Risk Governance.

---

# **23\. Glossary**

## **Primary Reason Code**

The single most important reason supporting the decision outcome.

## **Secondary Reason Code**

An additional reason that materially contributed to the decision.

## **Risk Factor**

A financial, credit, documentation, or policy-related element that influences underwriting judgment.

## **Reason Code**

A standardized label used to describe a specific risk factor or compensating strength in consistent business language.

## **Customer-Safe Wording**

A simplified explanation format intended for external communication or customer-facing interpretation where appropriate.

## **Model-Supported Explanation**

A business interpretation informed by model outputs, but framed in non-technical language and grounded in policy-relevant evidence.

---

# **24\. Final Dictionary Statement**

Reason codes are intended to improve clarity, consistency, and explainability in underwriting decisions. They help translate complex case findings into structured business language, but they must always remain tied to evidence, policy, and sound analyst judgment.

A good reason code framework supports explainable decisions without oversimplifying them. Analysts are expected to select reason codes carefully, describe them clearly, and ensure that every coded rationale reflects the actual substance of the case.
