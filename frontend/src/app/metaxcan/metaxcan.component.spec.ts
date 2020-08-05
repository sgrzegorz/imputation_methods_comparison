import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MetaxcanComponent } from './metaxcan.component';

describe('MetaxcanComponent', () => {
  let component: MetaxcanComponent;
  let fixture: ComponentFixture<MetaxcanComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MetaxcanComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MetaxcanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
