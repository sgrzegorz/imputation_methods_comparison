import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ImageService {
  url = 'http://localhost:5000/';

  constructor(private httpClient: HttpClient) {
  }

  getImage(imageUrl: string): Observable<Blob> {
    imageUrl = this.url + '/' + imageUrl;
    return this.httpClient.get(imageUrl, {responseType: 'blob'});
  }
}
