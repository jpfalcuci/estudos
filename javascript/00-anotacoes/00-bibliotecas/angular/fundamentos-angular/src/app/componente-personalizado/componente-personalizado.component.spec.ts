import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentePersonalizadoComponent } from './componente-personalizado.component';

describe('ComponentePersonalizadoComponent', () => {
  let component: ComponentePersonalizadoComponent;
  let fixture: ComponentFixture<ComponentePersonalizadoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ComponentePersonalizadoComponent]
    });
    fixture = TestBed.createComponent(ComponentePersonalizadoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
