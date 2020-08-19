import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {PredixcanComponent} from "./predixcan/predixcan.component";
import {TigarComponent} from "./tigar/tigar.component";
import {FusionComponent} from "./fusion/fusion.component";
import {MetaxcanComponent} from "./metaxcan/metaxcan.component";

const routes: Routes = [
  { path: 'predixcan', component: PredixcanComponent },
  { path: 'tigar', component: TigarComponent },
  { path: 'fusion', component: FusionComponent },
  { path: 'metaxcan', component: MetaxcanComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
