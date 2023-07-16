import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetalhesProdutoComponent } from './detalhes-produto.component';

describe('DetalhesProdutoComponent', () => {
  let component: DetalhesProdutoComponent;
  let fixture: ComponentFixture<DetalhesProdutoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DetalhesProdutoComponent]
    });
    fixture = TestBed.createComponent(DetalhesProdutoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
