
# DevCrypt Installation Guide

This guide explains how to install the `devcrypt` package hosted on a custom Netlify server.

---

## ✅ Method 1: Install directly from hosted `.whl` file

If you want to install the package directly using the `.whl` file:

```
pip install https://devcrypts.netlify.app/simple/devcrypt/devcrypt-1.0.0-py3-none-any.whl
```

> This URL must point directly to the `.whl` file.

---

## ⚠️ Method 2: Using a custom index URL (won't work without correct directory setup)

Although normally you'd use:

```
pip install --index-url https://devcrypts.netlify.app/simple/ devcrypt
```

This won't work unless your `/simple/` directory is structured and rendered as a plaintext package index (PEP 503). HTML rendering will break pip's expectations.

### Structure needed:
Your `https://devcrypts.netlify.app/simple/devcrypt/` must serve an HTML page like this:

```html
<!DOCTYPE html>
<html>
  <head><title>Links for devcrypt</title></head>
  <body>
    <h1>Links for devcrypt</h1>
    <a href="devcrypt-1.0.0-py3-none-any.whl">devcrypt-1.0.0-py3-none-any.whl</a><br>
    <a href="devcrypt-1.0.0.tar.gz">devcrypt-1.0.0.tar.gz</a><br>
  </body>
</html>
```

---

## 🛠 If you're installing locally (development mode)

```
pip uninstall devcrypt
python -m build
pip install dist/devcrypt-1.0.0-py3-none-any.whl
```

Make sure `build` is installed:

```
pip install build
```

---

## 📦 Directory structure on Netlify

```
/simple/
  /devcrypt/
    index.html  <-- Proper HTML with .whl and .tar.gz links
    devcrypt-1.0.0-py3-none-any.whl
    devcrypt-1.0.0.tar.gz
```

---

## 🧪 Test if installation works

```python
import devcrypt
print(devcrypt.__version__)
```

---

© 2025 Atharva Panchal, Mohit Chaudhari
