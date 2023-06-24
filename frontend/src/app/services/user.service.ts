import { Injectable } from '@angular/core';
import { WebRequestService } from './web-request.service';
import { User } from './../interfaces/user';


@Injectable({
  providedIn: 'root'
})
export class UserService {
  

  constructor(private webRequestService:WebRequestService) {
  
  }

  createUser(user:User){
    //send web request to content
    return this.webRequestService.put(`new/user`, {user})


  }

}
