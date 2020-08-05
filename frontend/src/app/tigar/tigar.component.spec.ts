import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TigarComponent } from './tigar.component';

describe('TigarComponent', () => {
  let component: TigarComponent;
  let fixture: ComponentFixture<TigarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TigarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TigarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
