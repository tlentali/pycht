<p align="center";
    font-family: Georgia, sans-serif;
    text-decoration: none;
    background: #ffbdfb;
    padding: 3px 6px;
    color: #000;
    font-size: 28px;>
    <a href="#"><img src="https://raw.githubusercontent.com/tlentali/pycht/master/misc/pycht_logo.svg"  alt="pycht_logo" width="350"/>
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

Generate a 5 colors stencil model :
```python
>>> import pycht

>>> pycht.stencil('cat.jpg', 5)
```

 |                                    Stencil 1                                    |                                    stencil 2                                    |                                    stencil 3                                    |                                    stencil 4                                    |                                    stencil 5                                    |
 | :-----------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
 | ![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_2.png) | ![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_3.png) | ![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_4.png) | ![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_5.png) | ![](https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_1.png) |


Final result rendering with all stencils :

<p align="center">
  <a href="#"><img src="https://raw.githubusercontent.com/tlentali/pycht/master/misc/stencil_cat.jpg" width="250"></a>
</p>

Cut it, paint it, stare at it.
Enjoy !

## 🛠 Installation

🐍 You need to install **Python 3.12** or above.

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

## 🥄 How Does It Work?

Imagine `pycht` as your personal digital street artist. Here's what happens under the hood, step-by-step:

1. **🖼️ Image loading**
   `pycht` grabs your input image and flattens it like a pancake — every pixel becomes a 3-value row (B, G, R) in a giant NumPy array. Think of it as turning your photo into a spreadsheet of colors.

2. **🎯 K-Means clustering**
   Then comes the science. Using OpenCV’s `kmeans`, we ask: *“Hey, what are the `N` most dominant colors in this image?”*
   The algorithm groups similar pixels into `nb_colors` clusters and assigns each one a centroid — like reducing a rainbow into just a few paint buckets.

3. **🎨 Color mapping**
   Every pixel in your image is replaced by its cluster's centroid. Boom — you've got a stylized version of your image with just `N` bold, poster-style colors.

4. **🔍 Color separation**
   Now the magic: for each color, `pycht` creates a mask. All pixels that **don’t** belong to the current color cluster are set to black (and later transparent).
   Each color gets its own PNG file — like cutting stencils for spray-painting layers IRL.

5. **📁 File drop**
   Your output includes:
   - `output.png` → The clustered image
   - `stencil_1.png`, `stencil_2.png`, ... → Transparent layers, one per color

> It's like building silkscreen layers, but with Python, pixels, and zero mess.

Ready to turn your cat photo into street art? Let `pycht` paint it.

Check out the [API](https://tlentali.github.io/pycht/reference/pycht.html) for a comprehensive overview.

## 🧑‍💻 Development

You can use `pip` or [uv](https://docs.astral.sh/uv/). From the `pycht` root folder, do:

* `uv venv --python /path/to/3.12.x/python`. *Tips*: you can use [pyenv](https://github.com/pyenv/pyenv) to manage and
  install multiple Python versions. You can find a specific version at `~/.pyenv/versions/3.12.2/bin/python` for
  instance.
* `source .venv/bin/activate` to activate the virtualenv `.venv` created by `uv`
* `uv sync --inexact` to install all dependencies
* `pre-commit install` (just one time). The pre-commit hook will run black, isort and pylint before your commit :)

You're ready to hack!

## 🧰 Command-Line Interface (CLI)

You can use `pycht` as a command-line tool to generate stencil layers from an image — perfect for street art, posters, or digital illustration.

### 🖥️ Installation

Install in editable mode (dev mode) with [uv](https://github.com/astral-sh/uv) or pip:

```bash
uv pip install -e .
```

Make sure you have the required dependencies listed in `pyproject.toml`.

### 🚀 Usage

```bash
pycht <input-img> [OPTIONS]
```

**Arguments:**
- `<input-img>`: Path to the input image (JPEG, PNG, etc.)

**Options:**
- `--output-path TEXT` – Directory where output layers will be saved (default: `./output`)
- `--nb-colors INTEGER` – Number of stencil layers to generate (default: `3`)

### ✅ Example

```bash
pycht misc/cat.jpg --nb-colors 4 --output-path .
```

This will create 4 stencil layers and save them in the current folder.

## 🔗 Useful links

- [Documentation](https://tlentali.github.io/pycht/)
- [Package releases](https://pypi.org/project/pycht/#history)

## 🖖 Contributing

Feel free to contribute in any way you like, we're always open to new ideas and approaches. If you want to contribute to the code base please check out the [CONTRIBUTING.md](https://github.com/tlentali/pycht/blob/master/CONTRIBUTING.md) file. Also take a look at the [issue tracker](https://github.com/tlentali/pycht/issues) and see if anything takes your fancy.

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Again, contributions of any kind are welcome!


## 📜 License

`pycht` is free and open-source software licensed under the [MIT license](https://github.com/tlentali/pycht/blob/master/LICENSE).
