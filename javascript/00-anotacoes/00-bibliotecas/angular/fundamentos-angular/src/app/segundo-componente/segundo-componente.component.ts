import { Component } from '@angular/core';

@Component({
  selector: 'app-segundo-componente',
  templateUrl: './segundo-componente.component.html',
  styleUrls: ['./segundo-componente.component.css']
})
export class SegundoComponenteComponent {
  nome = "João das Neves";
  dataNascimento = "1992-09-18";
  urlImagem = "/assets/john.jpg";

  mostrarDataNascimento() {
    alert(`A data de nascimento de ${this.nome} é: ${this.dataNascimento}`);
  }
}
