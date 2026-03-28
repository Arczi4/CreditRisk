import { Component, signal } from '@angular/core';
import { LoanFormComponent } from './components/loan-form/loan-form.component';
import { LoadingModalComponent } from './components/loading-modal/loading-modal.component';
import { ResultsComponent } from './components/results/results.component';
import { ApiService } from './services/api.service';
import { PaybackRequest } from './models/payback-request.model';
import { PaybackEndpointResponse } from './models/payback-response.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [LoanFormComponent, LoadingModalComponent, ResultsComponent],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  loading = signal(false);
  result = signal<PaybackEndpointResponse | null>(null);
  error = signal<string | null>(null);

  constructor(private api: ApiService) {}

  onSubmit(request: PaybackRequest): void {
    this.loading.set(true);
    this.result.set(null);
    this.error.set(null);

    this.api.analyzeApplication(request).subscribe({
      next: (response) => {
        this.result.set(response);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set(
          err?.error?.detail ?? 'An unexpected error occurred. Please try again.'
        );
        this.loading.set(false);
      },
    });
  }

  onReset(): void {
    this.result.set(null);
    this.error.set(null);
  }
}
