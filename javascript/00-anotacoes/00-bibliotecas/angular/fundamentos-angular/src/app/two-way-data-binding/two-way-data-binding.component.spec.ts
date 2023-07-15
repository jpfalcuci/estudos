import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwoWayDataBindingComponent } from './two-way-data-binding.component';

describe('TwoWayDataBindingComponent', () => {
  let component: TwoWayDataBindingComponent;
  let fixture: ComponentFixture<TwoWayDataBindingComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TwoWayDataBindingComponent]
    });
    fixture = TestBed.createComponent(TwoWayDataBindingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
