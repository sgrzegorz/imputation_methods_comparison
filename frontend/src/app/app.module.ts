import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {PredixcanComponent} from './predixcan/predixcan.component';
import {HttpClientModule} from "@angular/common/http";
import { MetaxcanComponent } from './metaxcan/metaxcan.component';
import { FusionComponent } from './fusion/fusion.component';
import { TigarComponent } from './tigar/tigar.component';

@NgModule({
  declarations: [
    AppComponent,
    PredixcanComponent,
    MetaxcanComponent,
    FusionComponent,
    TigarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
