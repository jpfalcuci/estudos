import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PipeCustomizadoComponent } from './pipe-customizado.component';

describe('PipeCustomizadoComponent', () => {
  let component: PipeCustomizadoComponent;
  let fixture: ComponentFixture<PipeCustomizadoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PipeCustomizadoComponent]
    });
    fixture = TestBed.createComponent(PipeCustomizadoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
