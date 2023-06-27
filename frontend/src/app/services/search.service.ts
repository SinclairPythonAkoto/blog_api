import { Injectable } from '@angular/core';
import { WebRequestService } from './web-request.service';


@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private webRequestService:WebRequestService) {
  
  }

  searchByEmail(query:string){
    return this.webRequestService.get(`new/${query}`, null)
  }
}
