# 📐 Guía básica de CSS Grid

CSS Grid es un sistema de diseño en CSS que permite organizar elementos en **filas y columnas**. Es ideal para crear layouts completos, galerías de productos y diseños responsive como los de una tienda online.

---

## 🧱 1. ¿Qué es CSS Grid?
Grid trabaja con un **contenedor padre** y varios **elementos hijos**.
- El contenedor define la estructura (filas y columnas)
- Los hijos se acomodan automáticamente dentro de esa estructura

---

## 2️⃣ Activar Grid
Para usar Grid, primero debes activarlo en el contenedor:

```css
.contenedor {
  display: grid;
}
```

---

## 3️⃣ Crear columnas (grid-template-columns)

### 🔹 Columnas iguales
```css
.contenedor {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}
```

📌 `1fr` significa una fracción del espacio disponible.

---

## 4️⃣ Espaciado entre elementos (gap)

```css
.contenedor {
  gap: 20px;
}
```

👉 Reemplaza el uso de `margin` entre tarjetas o productos.

---

## 5️⃣ Ejemplo práctico (productos)

### HTML
```html
<div class="productos">
  <div class="card">Producto 1</div>
  <div class="card">Producto 2</div>
  <div class="card">Producto 3</div>
  <div class="card">Producto 4</div>
</div>
```

### CSS
```css
.productos {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
```

---

## 6️⃣ Grid Responsive (recomendado)

```css
.productos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}
```

✔ Se adapta automáticamente a cualquier tamaño de pantalla
✔ Perfecto para tiendas online

---

## 7️⃣ Filas (grid-template-rows)

```css
.contenedor {
  grid-template-rows: auto 300px auto;
}
```

📌 Normalmente no es necesario definir filas, Grid las crea solo.

---

## 8️⃣ Alinear elementos

### Centrar todo
```css
.contenedor {
  place-items: center;
}
```

### Separado
```css
.contenedor {
  justify-items: center;
  align-items: center;
}
```

---

## 9️⃣ Hacer que un elemento ocupe más espacio

```css
.card-grande {
  grid-column: span 2;
}
```

👉 Hace que el elemento ocupe 2 columnas

---

## 🔟 Grid vs Flexbox

| Grid | Flexbox |
|-----|--------|
| Filas y columnas | Una sola dirección |
| Layouts grandes | Elementos pequeños |
| Galerías | Navs y botones |

📌 En proyectos web:
- **Grid** → estructura general
- **Flex** → alineación interna

---

## 🛍️ Aplicado a tu proyecto

```css
.container-imagenes1 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}
```

---

## 🧠 Regla de oro
1️⃣ Grid en el contenedor padre
2️⃣ Flex en los hijos
3️⃣ Usa `auto-fit + minmax()` para responsive

---

📌 **Conclusión:**
CSS Grid facilita crear diseños ordenados, responsive y profesionales con poco código. Es una herramienta esencial para layouts modernos.

