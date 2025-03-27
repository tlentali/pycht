# 🎨 Pycht

**Pycht** is a lightweight Python tool that transforms images into colorful street art-style stencils using K-Means clustering.

It automatically reduces an image’s color palette into distinct clusters and generates transparent PNG layers for each one — ideal for digital or physical stencil creation, creative coding projects, or simply exploring image segmentation.

---

## ✨ Features

- 🧠 Simple image clustering using OpenCV’s K-Means algorithm  
- 🖼️ Color separation with transparency masks  
- 📁 Input/output file handling with minimal setup  
- 🧰 Modular architecture for easy extension

---

## 🚀 How It Works

1. **Load** an image.
2. **Process** the pixels into a 2D format.
3. **Cluster** colors using K-Means.
4. **Separate** each color cluster into its own transparent stencil.
5. **Save** the final image and each stencil layer as a `.png`.

---

## 📦 Example Usage

```python
from pycht import Pycht

# Create a stencil with 5 color clusters
p = Pycht()
p.stencil("images/input.jpg", "images/output.png", nb_colors=5)
```