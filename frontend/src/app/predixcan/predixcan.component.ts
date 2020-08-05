import {Component, OnInit} from '@angular/core';
import {DataItem} from "../dataitem";
import {DATA} from "../mock-data";
import {TableService} from "../table.service";


@Component({
  selector: 'app-predixcan',
  templateUrl: './predixcan.component.html',
  styleUrls: ['./predixcan.component.css']
})
export class PredixcanComponent implements OnInit {

  data1: DataItem [];


  constructor(private tableService : TableService) {
  }

  ngOnInit(): void {
    this.getMyTable();

  }

  getPredixcanResults(): void {
    console.log('nfiaofnaof');
    this.getMyTable();
  }

  getMyTable(): void {
    this.tableService.getTable().subscribe(data => this.data1 = data);
  }

}
