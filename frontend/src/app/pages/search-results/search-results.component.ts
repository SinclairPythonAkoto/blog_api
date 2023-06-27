import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { SearchService } from "../../services/search.service"


@Component({
  selector: 'app-search-results',
  templateUrl: './search-results.component.html',
  styleUrls: ['./search-results.component.scss']
})
export class SearchResultsComponent implements OnInit {
  query:string = "";
  constructor(private route: ActivatedRoute, private search: SearchService) { }
  ngOnInit(): void {
    this.route.queryParams.subscribe(params =>{
      this.query = params["query"]

      this.search.searchByEmail(this.query);
      

    }
    )
  }
}



