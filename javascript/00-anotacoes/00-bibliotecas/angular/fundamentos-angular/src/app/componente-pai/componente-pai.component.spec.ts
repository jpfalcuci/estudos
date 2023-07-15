import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentePaiComponent } from './componente-pai.component';

describe('ComponentePaiComponent', () => {
  let component: ComponentePaiComponent;
  let fixture: ComponentFixture<ComponentePaiComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ComponentePaiComponent]
    });
    fixture = TestBed.createComponent(ComponentePaiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
