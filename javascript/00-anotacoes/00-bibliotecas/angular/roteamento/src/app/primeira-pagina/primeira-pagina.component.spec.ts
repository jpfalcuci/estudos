import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrimeiraPaginaComponent } from './primeira-pagina.component';

describe('PrimeiraPaginaComponent', () => {
  let component: PrimeiraPaginaComponent;
  let fixture: ComponentFixture<PrimeiraPaginaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PrimeiraPaginaComponent]
    });
    fixture = TestBed.createComponent(PrimeiraPaginaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
