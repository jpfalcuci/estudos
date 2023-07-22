import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Curso } from './curso';
import { Observable } from 'rxjs/internal/Observable';

@Injectable({
  providedIn: 'root'
})
export class CursoService {

  url = "http://localhost/api/php/";

  vetor:Curso[];

  constructor(private http: HttpClient) { }

  obterCursos(): Observable<Curso[]> {
    return this.http.get(this.url + "listar").pipe(
      map((res) => {
        this.vetor = res['cursos'];
        return this.vetor;
      })
    )
  }

  cadastrarCurso(c:Curso): Observable<Curso[]> {
    return this.http.post(this.url + "cadastrar", {cursos:c}).pipe(
      map((res) => {
        this.vetor.push(res['cursos']);
        return this.vetor;
      })
    )
  }

  removerCurso(c:Curso): Observable<Curso[]> {
    const params = new HttpParams().set("idCurso", c.idCurso.toString());
    return this.http.delete(this.url + "excluir", {params: params}).pipe(
      map((res) => {
        const filtro = this.vetor.filter((curso) => {
          return +curso['idCurso'] !== +c.idCurso;
        });
        return this.vetor = filtro;
      })
    )
  }

  atualizarCurso(c:Curso): Observable<Curso[]> {
    return this.http.put(this.url + "alterar", {cursos:c}).pipe(
      map((res) => {
        const cursoAlterado = this.vetor.find((item) => {
          return +item['idCurso'] === +['idCurso'];
        });
        if (cursoAlterado) {
          cursoAlterado['nomeCurso'] = c.nomeCurso;
          cursoAlterado['valorCurso'] = c.valorCurso;
        }
        return this.vetor;
      })
    )
  }

}
