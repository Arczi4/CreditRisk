import { Component, input, output } from '@angular/core';
import { DecimalPipe } from '@angular/common';
import { PaybackEndpointResponse, LoanDecision } from '../../models/payback-response.model';

@Component({
  selector: 'app-results',
  standalone: true,
  imports: [DecimalPipe],
  templateUrl: './results.component.html',
  styleUrl: './results.component.css',
})
export class ResultsComponent {
  result = input.required<PaybackEndpointResponse>();
  resetRequest = output<void>();

  get decision(): LoanDecision {
    return this.result().loan_decision;
  }

  get probaPercent(): number {
    return this.result().payback_proba * 100;
  }

  get decisionClass(): string {
    const map: Record<LoanDecision, string> = {
      Approve: 'approve',
      Review: 'review',
      Reject: 'reject',
    };
    return map[this.decision] ?? 'reject';
  }

  onReset(): void {
    this.resetRequest.emit();
  }
}
