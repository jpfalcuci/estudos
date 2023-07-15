import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponenteFilhoComponent } from './componente-filho.component';

describe('ComponenteFilhoComponent', () => {
  let component: ComponenteFilhoComponent;
  let fixture: ComponentFixture<ComponenteFilhoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ComponenteFilhoComponent]
    });
    fixture = TestBed.createComponent(ComponenteFilhoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
