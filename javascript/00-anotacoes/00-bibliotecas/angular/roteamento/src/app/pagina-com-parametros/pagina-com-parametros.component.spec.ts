import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PaginaComParametrosComponent } from './pagina-com-parametros.component';

describe('PaginaComParametrosComponent', () => {
  let component: PaginaComParametrosComponent;
  let fixture: ComponentFixture<PaginaComParametrosComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PaginaComParametrosComponent]
    });
    fixture = TestBed.createComponent(PaginaComParametrosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
