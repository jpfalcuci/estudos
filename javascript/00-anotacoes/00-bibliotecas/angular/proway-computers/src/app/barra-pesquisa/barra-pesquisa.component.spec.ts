import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BarraPesquisaComponent } from './barra-pesquisa.component';

describe('BarraPesquisaComponent', () => {
  let component: BarraPesquisaComponent;
  let fixture: ComponentFixture<BarraPesquisaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BarraPesquisaComponent]
    });
    fixture = TestBed.createComponent(BarraPesquisaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
