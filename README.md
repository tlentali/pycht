<p align="center";
    font-family: Georgia, sans-serif;
    text-decoration: none;
    background: #ffbdfb;
    padding: 3px 6px;
    color: #000;
    font-size: 28px;>
    <a href="#"><img src="https://raw.githubusercontent.com/tlentali/pycht/master/misc/pycht_logo_pink.png"  alt="pycht_logo" width="350"/>
    </a>
</p>

<p align="center">
  <b>Street art by clustering.
</p>

<p align="center">
  <a href="#"><img src="https://raw.githubusercontent.com/tlentali/pycht/master/misc/alys.png" /></a>
</p>

<p align="right">
Pics by <a href="https://www.instagram.com/alys.cheshire/">@alys.cheshire</a>
</p>


## ⚡️ Quick start

Take a nice picture :
<p align="center">
  <a href="#"><img src="https://raw.githubusercontent.com/tlentali/pycht/master/misc/cat.jpg" width="250"></a>
</p>

Generate a 4 colors stencil model :
```python
>> from pycht import Pycht

>> Pycht().stencil('cat.jpg', 'stencil_cat.jpg', 4)
```

 Stencil 1                 |  stencil 2                 |   stencil 3               | stencil 4                 |
:-------------------------:|:--------------------------:| :-----------------------: | :-----------------------: |
![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_2.jpg)  |  ![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_3.jpg) | ![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_4.jpg) | ![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_5.jpg) |


Final result rendering with all stencils :

<p align="center">
  <a href="#"><img src="https://raw.githubusercontent.com/tlentali/pycht/master/misc/resultat_final.jpg" width="250"></a>
</p>

Cut it, paint it, stare at it, leave it.
Enjoy !


## 🛠 Installation

:snake: You need to install **Python 3.7** or above.

Installation can be done by using `pip`.
There are [wheels available](https://pypi.org/project/pycht/#files) for **Linux**, **MacOS**, and **Windows**.

```bash
pip install pycht
```

You can also install the latest development version as so:

```bash
pip install git+https://github.com/tlentali/pycht

# Or, through SSH:
pip install git+ssh://git@github.com/tlentali/pycht.git
```


## 🥄 How ?

Behind this script, you will find algos used for marketing, financial prediction and client targeting.
The pics is tranlated into a matrice, each value indicate a pixel color in three dimension.
Then, a clustering algorithm is used to reshape the picture by colors. The number of colors desired is a parameter and is chosen directly by the user.
As an output you have the picture with the number of color you choose and a picture by color to elaborate each stencils one by one.

## 🖖 Contributing

Feel free to contribute in any way you like, we're always open to new ideas and approaches. If you want to contribute to the code base please check out the [CONTRIBUTING.md](https://github.com/tlentali/pycht/blob/master/CONTRIBUTING.md) file. Also take a look at the [issue tracker](https://github.com/tlentali/pycht/issues) and see if anything takes your fancy.

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Again, contributions of any kind are welcome!


## 📜 License

```pycht``` is free and open-source software licensed under the [MIT license](https://github.com/tlentali/pycht/blob/master/LICENSE).
