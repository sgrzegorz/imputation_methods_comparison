import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PredixcanComponent } from './predixcan.component';

describe('PredixcanComponent', () => {
  let component: PredixcanComponent;
  let fixture: ComponentFixture<PredixcanComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PredixcanComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PredixcanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
