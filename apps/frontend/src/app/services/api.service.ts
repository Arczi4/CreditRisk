import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PaybackRequest } from '../models/payback-request.model';
import { PaybackEndpointResponse } from '../models/payback-response.model';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class ApiService {
  private readonly baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  analyzeApplication(request: PaybackRequest): Observable<PaybackEndpointResponse> {
    return this.http.post<PaybackEndpointResponse>(
      `${this.baseUrl}/api/payback/single`,
      request
    );
  }
}
