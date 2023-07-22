import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Curso } from './curso';
import { Observable } from 'rxjs/internal/Observable';

@Injectable({
  providedIn: 'root'
})
export class CursoService {

  url = "http://localhost/api/php/";

  vetor:Curso[] = [];

  constructor(private http: HttpClient) { }

  obterCursos(): Observable<Curso[]> {
    return this.http.get< { cursos: Curso[] } >(this.url + "listar").pipe(
      map((res) => {
        this.vetor = res.cursos;
        return this.vetor;
      })
    );
  }

  cadastrarCurso(c: Curso): Observable<Curso> {
    return this.http.post<Curso>(this.url + "cadastrar", { cursos: c }).pipe(
      map((res) => {
        return res as Curso;
      })
    );
  }

  removerCurso(c: Curso): Observable<Curso[]> {
    if (!c.idCurso) {
      throw new Error('O objeto Curso precisa ter a propriedade "idCurso" definida.');
    }
    const params = new HttpParams().set("idCurso", c.idCurso.toString());
    return this.http.delete<Curso[]>(this.url + "excluir", { params }).pipe(
      map((res) => {
        this.vetor = this.vetor.filter((curso) => curso.idCurso !== c.idCurso);
        return this.vetor;
      })
    );
  }

  atualizarCurso(c: Curso): Observable<Curso[]> {
    if (c.idCurso === undefined) {
      throw new Error('O objeto Curso precisa ter a propriedade "idCurso" definida.');
    }
    return this.http.put<Curso[]>(this.url + "alterar", { cursos: c }).pipe(
      map((res) => {
        const cursoAlterado = this.vetor.find((item) => {
          return item.idCurso !== undefined && +item.idCurso === c.idCurso;
        });
        if (cursoAlterado) {
          cursoAlterado.nomeCurso = c.nomeCurso;
          cursoAlterado.valorCurso = c.valorCurso;
        }
        return this.vetor;
      })
    );
  }

}
