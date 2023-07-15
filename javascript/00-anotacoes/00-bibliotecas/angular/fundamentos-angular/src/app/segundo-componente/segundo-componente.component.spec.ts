import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SegundoComponenteComponent } from './segundo-componente.component';

describe('SegundoComponenteComponent', () => {
  let component: SegundoComponenteComponent;
  let fixture: ComponentFixture<SegundoComponenteComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SegundoComponenteComponent]
    });
    fixture = TestBed.createComponent(SegundoComponenteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
