# 🧹 zimpy  

![Python](https://img.shields.io/badge/python-3.9%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-green)  
![Status](https://img.shields.io/badge/status-teaching--tool-orange)  
![Made with ❤️](https://img.shields.io/badge/made%20with-%E2%9D%A4-red)  

---

`zimpy` is a Python helper library for cleaning and untangling messy data.  
Right now it ships with **ventclean**, a set of functions for spotting and removing sneaky invisible characters in your datasets.  
Later on, it will also include **datewizard** for fixing broken date formats.  

---

## ✨ Features  

### ✅ ventclean  
- Detects weird “wonky” Unicode characters (NBSPs, zero-width spaces, Cyrillic look-alikes, etc.)  
- Visualizes problem spots so you can see where data might trip you up  
- Cleans them out automatically so your analysis doesn’t crash  

### 🔮 datewizard (coming soon)  
- Makes human-ugly date formats human-friendly  
- Converts random formats into standard ISO dates  
- Plays nice with both `pandas` and Python’s built-in `datetime`  

---

## 🚀 Installation  

Clone the repo from GitHub:  

```bash
git clone https://github.com/YOUR-USERNAME/zimpy.git
cd zimpy
pip install -e .
---

## 📚 Usage  

```python
import zimpy.ventclean as vc

# Load demo data
df = vc.test_df  

# Detect wonky characters
vc.detect_wonky(df)

# Clean them out
df_clean = vc.kill_wonky(df)
```

---

## 🔎 Example  

| Column Name (before)         | Problem                              | Column Name (after) |
| ---------------------------- | ------------------------------------ | ------------------- |
| `prіce` *(Cyrillic i)*       | Looks like ASCII `i`, but isn’t       | `price`             |
| `amount usd` *(NBSP)*        | Non-breaking space instead of space   | `amount_usd`        |
| `customer﻿id` *(Zero-width)* | Hidden ZWSP in the middle             | `customer_id`       |

---

## 🎓 Why?  

Data cleaning is a huge part of analytics. Models often fail not because of bad math, but because of invisible gremlins hiding in your data.  

`zimpy` helps students (and instructors!) **see** and **squash** those gremlins early.  

---

## 🤝 Contributing  

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you’d like to add.  

---

## 📜 License  

MIT License – see [LICENSE](LICENSE)
