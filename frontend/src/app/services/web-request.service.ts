import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { User } from '../interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class WebRequestService {

  readonly ROOT_URL;

  constructor( private http: HttpClient) {
    this.ROOT_URL = 'http://localhost:5000'
   }

  // get(uri: string){

  //   return this.http.get(`${this.ROOT_URL}/${uri}`);
  // }
  // post(uri: string, payload: User){

  //   return this.http.post(`${this.ROOT_URL}/${uri}`, payload);
  // }

  put(uri: string, payload: Object){
    return this.http.put(`${this.ROOT_URL}/${uri}`, payload)
  }

  get(uri: string, payload: Object | null){
    if(payload){
      return this.http.get(`${this.ROOT_URL}/${uri}`, payload)
    } else {
      return this.http.get(`${this.ROOT_URL}/${uri}`)
    }
   
  }
}