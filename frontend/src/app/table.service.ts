import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {DataItem} from "./dataitem";
import {Observable, of, throwError} from 'rxjs';
import {catchError, retry, tap} from 'rxjs/operators';
import {DATA} from "./mock-data";


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    Authorization: 'my-auth-token'
  })
};

@Injectable({
  providedIn: 'root'
})
export class TableService {
  url = 'http://localhost:5000/';
  // url = '/assets/t.json';
  totalAngularPackages: any;

  constructor(private  http: HttpClient) {
  }

  getTable(methodName : string): Observable<DataItem[]> {
    console.log('hej');
    // get request
    return this.http.get<DataItem[]>(this.url+'/'+methodName).pipe(
      tap(_ => {
        this.log('fetched heroes');
        console.log('nfnaiofnaof');
      }),
      catchError(this.handleError<DataItem[]>('getHeroes', []))
    );
  }


  // askForTable() {
  //   // return this.http.get<DataItem[]>(this.apUrl);
  //   return this.http.post<DataItem[]>(this.url, DATA[0], httpOptions)
  //   .pipe(
  //     catchError(this.handleError('addHero', hero))
  //   );
  // }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.log(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  /** Log a HeroService message with the MessageService */
  private log(message: string) {
    console.log(message);
    // this.messageService.add(`HeroService: ${message}`);
  }


}
