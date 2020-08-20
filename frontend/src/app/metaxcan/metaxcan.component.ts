import {Component, OnInit} from '@angular/core';
import {ImageService} from "../image.service";

@Component({
  selector: 'app-metaxcan',
  templateUrl: './metaxcan.component.html',
  styleUrls: ['./metaxcan.component.css']
})

export class MethodComponent(){


}

export class MetaxcanComponent implements OnInit {
  imgUrl: string = 'metaxcan?id=';
  NUMBER_PICTURES: number = 3;
  pictures = [];
  isImageLoading = [];


  constructor(private imageService: ImageService) {
  }

  createImageFromBlob(image: Blob, imageId: number) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.pictures[imageId] = reader.result;
    }, false);

    if (image) {
      reader.readAsDataURL(image);
    }
  }

  ngOnInit(): void {
    this.getPicturesFromService();
  }

  getPicturesFromService() {
    for (let i = 0; i < this.NUMBER_PICTURES; i++) {
      this.getImageFromService(i);
    }
  }

  getImageFromService(imageId: number) {
    this.isImageLoading[imageId] = true;
    this.imageService.getImage(this.imgUrl+imageId).subscribe(data => {
      this.createImageFromBlob(data, imageId);
      this.isImageLoading[imageId] = false;
    }, error => {
      this.isImageLoading[imageId] = false;
    });
  }

}
