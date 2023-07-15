import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-primeira-pagina',
  templateUrl: './primeira-pagina.component.html',
  styleUrls: ['./primeira-pagina.component.css']
})
export class PrimeiraPaginaComponent {
  constructor(
    private router: Router,
  ) { }

  moverParaSegundaPagina() {
    this.router.navigate(['segunda-pagina']);
  }
}
