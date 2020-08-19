import { Component, OnInit } from '@angular/core';
import {ImageService} from "../image.service";

@Component({
  selector: 'app-metaxcan',
  templateUrl: './metaxcan.component.html',
  styleUrls: ['./metaxcan.component.css']
})
export class MetaxcanComponent implements OnInit {
  imgUrl: string = 'metaxcan?id=1';

  imageToShow: any;
  isImageLoading: boolean;

  constructor(private imageService: ImageService) {}

  createImageFromBlob(image: Blob) {
   let reader = new FileReader();
   reader.addEventListener("load", () => {
      this.imageToShow = reader.result;
   }, false);

   if (image) {
      reader.readAsDataURL(image);
   }
  }

  ngOnInit(): void {
    this.getImageFromService();
  }

  getImageFromService() {
      this.isImageLoading = true;
      this.imageService.getImage(this.imgUrl).subscribe(data => {
        this.createImageFromBlob(data);
        this.isImageLoading = false;
      }, error => {
        this.isImageLoading = false;
        console.log(error);
      });
  }

}
