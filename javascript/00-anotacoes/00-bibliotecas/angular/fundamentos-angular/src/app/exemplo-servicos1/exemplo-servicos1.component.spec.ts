import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExemploServicos1Component } from './exemplo-servicos1.component';

describe('ExemploServicos1Component', () => {
  let component: ExemploServicos1Component;
  let fixture: ComponentFixture<ExemploServicos1Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ExemploServicos1Component]
    });
    fixture = TestBed.createComponent(ExemploServicos1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
