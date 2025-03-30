# 🚀 Getting Started

Welcome to **Pycht** – a tool for transforming images into colorful stencil layers using K-Means clustering. This guide will help you install, use, and customize Pycht step-by-step.

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/tlentali/pycht.git
cd pycht
pip install -r requirements.txt
```

Alternatively, if you're using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🖼️ Usage Example

Here’s how to process an image and create stencils:

```python
from pycht import Pycht

p = Pycht()
p.stencil("images/input.jpg", nb_colors=4, output_path="output/")
```

This will:
- Load `input.jpg`
- Cluster its colors into 4 dominant tones
- Save:
  - `output/`: the final image with clustered colors
  - `stencil_1.png`, `stencil_2.png`, ...: one per color, with transparency

---

## ⚙️ Parameters

- `input_img` (str): Path to the original image.
- `output_path` (str): Path to save the clustered version of the image.
- `nb_colors` (int): Number of color clusters (stencils) to generate.

---

## 📁 Project Structure

```
pycht/
│
├── clustering.py         # Handles K-Means color clustering
├── image_processing.py   # Image reading, reshaping, saving, display
├── pycht.py              # Main class combining everything
├── images/               # Your input/output folder (create it)
└── ...
```

---

## 🧪 Try It With Your Own Image

Put any `.jpg` or `.png` in the `images/` folder and run the script.  
The tool will output one clustered image and one stencil per color.

---

## 🛠️ Customization Ideas

- Try different numbers of `nb_colors` to control stencil complexity.
- Preprocess the image (e.g., resize or blur) before clustering.
- Adjust the clustering criteria in `clustering.py` if needed.
- Change output paths to organize your stencil layers better.

---

## 📚 Next Steps

- [Browse the API Reference](reference/pycht.md)
- [View example images](https://github.com/tlentali/pycht/tree/main/examples) *(if available)*

---

## ❓ Need Help?

Feel free to [open an issue](https://github.com/tlentali/pycht/issues) on GitHub if you run into trouble.

Happy stenciling! 🎨