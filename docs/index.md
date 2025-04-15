# 🎨 Pycht

**Pycht** is a lightweight Python tool that transforms images into colorful street art-style stencils using K-Means clustering.

It automatically reduces an image’s color palette into distinct clusters and generates transparent PNG layers for each one — ideal for digital or physical stencil creation, creative coding projects, or simply exploring image segmentation.

---

## ✨ Features

- 🧠 Simple image clustering using Scikit-Learn’s K-Means algorithm  
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
import pycht

# Create a stencil with 5 color clusters
pycht.stencil("images/input.jpg", nb_colors=5)
```

This will generate:
- stencil_final.png → final clustered image
- stencil_1.png, stencil_2.png, etc. → one per color cluster, with transparency

---

## 🧪 Try It Out

Want to experiment? Just provide any image and see how it gets broken down into layers of color.

---

## 📚 Documentation

- [Getting Started](getting-started.md)
- API Reference

---

## 🛠️ Technologies Used

- Python 3.12+
- OpenCV
- NumPy
- MkDocs (for this documentation!)

---

## 🙌 Contributing

Pull requests are welcome! Feel free to open an issue or suggest improvements.

---

## 📄 License

MIT License © Thomas Lentali