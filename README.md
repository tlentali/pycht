# Cheshire

Create stencil from pics

<p align="center">
  <a href="#"><img src="./misc/alys.png" /></a>
</p>

Pics by [@alys.cheshire](https://www.instagram.com/alys.cheshire/)

## Why ?

> But, said Alice, if the world has absolutely no sense, who's stopping us from inventing one ?  
> **L. Caroll**

Piece of cake :
```python
>> import cheshire

>> pics = cheshire.Cheshire('/pics_path.jpg', 3)
>> pics.stencil()
```

You just have to cut and that's it ! Enjoy.  

## Install

```
pip install git+https://github.com/tlentali/cheshire.git
```

## How ?
Behind this script, you will find algos used for marketing, financial prediction and client targeting.  
The pics is tranlated into a matrice, each value indicate a pixel color in three dimension.  
Then, clustering algorithm is used to reshape the picture by colors. The number of colors desired is a parameter and is chosen directly by the user.  
As an output you have the picture with the number of color you choose and a picture by color to elaborate each stencils one by one.  
