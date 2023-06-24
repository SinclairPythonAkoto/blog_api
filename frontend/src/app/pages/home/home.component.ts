import { Component, Inject } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { User } from 'src/app/interfaces/user';
import { DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  constructor(private contentService:UserService,  @Inject(DOCUMENT) public document: Document){}

  sendCreate( email: HTMLInputElement, pwd: HTMLInputElement, name:HTMLInputElement){
    console.log({email: email.value.toString(), password: pwd.value.toString(), user: name.value.toString()} as User)
    // console.log({email.value , pwd, name} as User)
    this.contentService.createUser({email: email.value.toString(), password: pwd.value.toString(), user: name.value.toString()}).subscribe((response)=> console.log(response))
  }
}
