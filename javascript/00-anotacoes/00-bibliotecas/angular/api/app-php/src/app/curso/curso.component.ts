import { Component, OnInit } from '@angular/core';
import { Curso } from './curso';
import { CursoService } from './curso.service';

@Component({
  selector: 'app-curso',
  templateUrl: './curso.component.html',
  styleUrls: ['./curso.component.css']
})
export class CursoComponent implements OnInit {

	vetor: Curso[] = [];

	curso = new Curso();

	constructor(private curso_servico: CursoService) { }

	ngOnInit() {
		this.selecao();
	}
	
	selecao() {
		this.curso_servico.obterCursos().subscribe(
			(res: Curso[]) => {
				this.vetor = res;
			}
		);
	}

	cadastro() {
		this.curso_servico.cadastrarCurso(this.curso).subscribe(
			(res: Curso) => {
				this.vetor.push(res);
				this.curso.nomeCurso = '';
				this.curso.valorCurso = 0;
				this.selecao();
			}
		);
	}
	  

	alterar() {
		this.curso_servico.atualizarCurso(this.curso).subscribe(
			(res) => {
				this.vetor = res;
				this.curso.nomeCurso = '';
				this.curso.valorCurso = 0;
				this.selecao();
			}
		)
	}

	remover() {
		this.curso_servico.removerCurso(this.curso).subscribe(
			(res: Curso[]) => {
				this.vetor = res;
				this.curso.nomeCurso = '';
				this.curso.valorCurso = 0;
			}
		)
	}

	selecionarCurso(c:Curso) {
		this.curso.idCurso = c.idCurso;
		this.curso.nomeCurso = c.nomeCurso;
		this.curso.valorCurso = c.valorCurso;
	}
}
