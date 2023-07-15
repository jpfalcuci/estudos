import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  // https://jwt.io/
  acessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c';

  constructor() { }

  estaAutenticado(): boolean {
    return !!sessionStorage.getItem('acess-token');
  }

  login(email: string, senha: string): boolean {
    if (email === 'admin@admin.com.br' && senha === '123456') {
      sessionStorage.setItem('acess-token', this.acessToken);
      return true;
    }
    return false;
  }

  logout() {
    sessionStorage.clear();
  }
}
