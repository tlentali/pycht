# Cheshire

Create stencil from pics

<p align="center">
  <a href="#"><img src="./misc/alys.png" /></a>
</p>

Pics by [@alys.cheshire](https://www.instagram.com/alys.cheshire/)

## Why ?

> But, said Alice, if the world has absolutely no sense, who's stopping us from inventing one ?  
> **L. Caroll**

## Install

```
pip install git+https://github.com/tlentali/cheshire.git
```

## Exemple
Take a nice picture :  
<p align="center">
  <a href="#"><img src="./misc/cat.jpg" width="250"></a>
</p>

Piece of cake, here for 4 colors :
```python
>> import cheshire

>> pics = cheshire.Cheshire('/pics_path.jpg', 4)
>> pics.stencil()
```

 Stencil 1                 |  stencil 2                 |   stencil 3               | stencil 4                 |
:-------------------------:|:--------------------------:| :-----------------------: | :-----------------------: |
![](./misc/stencil_2.jpg)  |  ![](./misc/stencil_3.jpg) | ![](./misc/stencil_4.jpg) | ![](./misc/stencil_5.jpg) |


Final result rendering with all stencils :

<p align="center">
  <a href="#"><img src="./misc/resultat_final.jpg" width="250"></a>
</p>

You just have to cut and to paint it ! Enjoy.  

## How ?
Behind this script, you will find algos used for marketing, financial prediction and client targeting.  
The pics is tranlated into a matrice, each value indicate a pixel color in three dimension.  
Then, clustering algorithm is used to reshape the picture by colors. The number of colors desired is a parameter and is chosen directly by the user.  
As an output you have the picture with the number of color you choose and a picture by color to elaborate each stencils one by one.  
