# Cheshire

From pics to stencil

<p align="center">
  <a href="#"><img src="./misc/alys.png" /></a>
</p>

> But, said Alice, if the world has absolutely no sense, who's stopping us from inventing one?  
> **L. Caroll**

It allows you to product stencil in an automatic way. In one shot and without Photoshop. You just told it how many color you want.

## Why?
To color the world!  
The majority uses Photoshop to build a stencil. Based on the famous quote "Better done than perfect", I looked for the simplest way to get something quick (and dirty). Paradoxically, even if the result is generated by an algo, it is closer to the spirit of street art, in my point of view of course. And above all, I like the fact that behind this script, you will find algos used for marketing, financial prediction, client targeting etc.  

## Principles
The pics is tranlated into a matrice, each value indicate a pixel color.
Then clustering is used to reshape the picture by colors. The number of colors desired is a parameter and is chosen directly by the user. As an output you have the picture with the number of color you choose and a picture by color to elaborate each stencils one by one. You just have to cut and that's it and enjoy.

## Install

## Demo
In the project location in a terminal, just type :
```
$ ./launch_demo
```

## to do
- generate one file by cluster
- generate a simplified image with an high clustering and then the actual clusterisation
