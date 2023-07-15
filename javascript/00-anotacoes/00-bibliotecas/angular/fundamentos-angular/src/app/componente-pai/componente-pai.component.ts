import { Component } from '@angular/core';

@Component({
  selector: 'app-componente-pai',
  templateUrl: './componente-pai.component.html',
  styleUrls: ['./componente-pai.component.css']
})
export class ComponentePaiComponent {
  sobrenome = "da Silva";

  mostraNomeCompleto(nomeCompleto: any): void {
    alert(`O nome completo é: ${nomeCompleto}`);
  }
}
