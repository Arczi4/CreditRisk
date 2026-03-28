import { Component, output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { PaybackRequest } from '../../models/payback-request.model';
import {
  GENDER_OPTIONS,
  MARITAL_STATUS_OPTIONS,
  EDUCATION_LEVEL_OPTIONS,
  EMPLOYMENT_STATUS_OPTIONS,
  LOAN_PURPOSE_OPTIONS,
  GRADE_SUBGRADE_OPTIONS,
} from '../../models/form-options';

@Component({
  selector: 'app-loan-form',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './loan-form.component.html',
  styleUrl: './loan-form.component.css',
})
export class LoanFormComponent {
  submitRequest = output<PaybackRequest>();

  readonly genderOptions = GENDER_OPTIONS;
  readonly maritalOptions = MARITAL_STATUS_OPTIONS;
  readonly educationOptions = EDUCATION_LEVEL_OPTIONS;
  readonly employmentOptions = EMPLOYMENT_STATUS_OPTIONS;
  readonly purposeOptions = LOAN_PURPOSE_OPTIONS;
  readonly gradeOptions = GRADE_SUBGRADE_OPTIONS;

  private readonly emptyForm: PaybackRequest = {
    gender: '',
    marital_status: '',
    education_level: '',
    employment_status: '',
    loan_purpose: '',
    grade_subgrade: '',
    annual_income: 0,
    debt_to_income_ratio: 0,
    credit_score: 0,
    loan_amount: 0,
    interest_rate: 0,
  };

  readonly presets: { label: string; data: PaybackRequest | null }[] = [
    {
      label: 'Approve',
      data: {
        gender: 'Female',
        marital_status: 'Single',
        education_level: 'High School',
        employment_status: 'Self-employed',
        loan_purpose: 'Other',
        grade_subgrade: 'C3',
        annual_income: 29367.99,
        debt_to_income_ratio: 0.084,
        credit_score: 736,
        loan_amount: 2528.42,
        interest_rate: 13.67,
      },
    },
    { label: 'Review', data: null },
    { label: 'Reject', data: null },
  ];

  form: PaybackRequest = { ...this.emptyForm };

  fillPreset(preset: { label: string; data: PaybackRequest | null }): void {
    if (preset.data) {
      this.form = { ...preset.data };
    }
  }

  onSubmit(): void {
    if (!this.isFormValid()) return;
    this.submitRequest.emit({ ...this.form });
  }

  isFormValid(): boolean {
    return (
      this.form.gender.length > 0 &&
      this.form.marital_status.length > 0 &&
      this.form.education_level.length > 0 &&
      this.form.employment_status.length > 0 &&
      this.form.loan_purpose.length > 0 &&
      this.form.grade_subgrade.length > 0 &&
      this.form.annual_income >= 0 &&
      this.form.credit_score >= 0 &&
      this.form.loan_amount >= 0 &&
      this.form.interest_rate >= 0
    );
  }
}
