import { DOCUMENT } from '@angular/common';
import { Component, Inject, OnInit } from '@angular/core';
import { Router } from "@angular/router";
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit{
  constructor(@Inject(DOCUMENT) private document: Document, private router: Router){

  }
  value=''
  ngOnInit(): void {
   
  }
  searchClick(){
    this.router.navigateByUrl(`/searchResult?query=${this.value}`);
  }

}
