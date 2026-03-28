import { Component, input } from '@angular/core';

@Component({
  selector: 'app-loading-modal',
  standalone: true,
  templateUrl: './loading-modal.component.html',
  styleUrl: './loading-modal.component.css',
})
export class LoadingModalComponent {
  visible = input.required<boolean>();
}
