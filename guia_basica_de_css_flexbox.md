# 📦 Guía básica de CSS Flexbox

CSS Flexbox es un sistema de diseño en CSS que permite **alinear y distribuir elementos en una sola dirección** (fila o columna). Es ideal para menús, barras de navegación, botones y alineaciones internas.

---

## 🧱 1. ¿Qué es Flexbox?
Flexbox trabaja con:
- Un **contenedor padre** (flex container)
- Varios **elementos hijos** (flex items)

Sirve para alinear elementos fácilmente tanto **horizontal** como **verticalmente**.

---

## 2️⃣ Activar Flexbox

```css
.contenedor {
  display: flex;
}
```

📌 Por defecto los elementos se colocan en **fila (row)**.

---

## 3️⃣ Dirección (flex-direction)

```css
.contenedor {
  flex-direction: row;      /* por defecto */
  /* column | row-reverse | column-reverse */
}
```

Ejemplo:
```css
.columna {
  display: flex;
  flex-direction: column;
}
```

---

## 4️⃣ Espacio entre elementos (gap)

```css
.contenedor {
  gap: 20px;
}
```

👉 Muy útil para navbars y botones.

---

## 5️⃣ Alineación horizontal (justify-content)

```css
.contenedor {
  justify-content: space-between;
}
```

Opciones comunes:
- `flex-start`
- `center`
- `space-between`
- `space-around`
- `space-evenly`

---

## 6️⃣ Alineación vertical (align-items)

```css
.contenedor {
  align-items: center;
}
```

Opciones:
- `stretch` (por defecto)
- `center`
- `flex-start`
- `flex-end`

---

## 7️⃣ Centrar completamente un elemento

```css
.contenedor {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

🔥 Muy usado para centrar iconos, botones o cards.

---

## 8️⃣ Ejemplo práctico (Navbar)

### HTML
```html
<nav class="navbar">
  <h1>CRUD.STORE</h1>
  <ul class="menu">
    <li>Shop</li>
    <li>On Sale</li>
    <li>Brands</li>
  </ul>
</nav>
```

### CSS
```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.menu {
  display: flex;
  gap: 16px;
}
```

---

## 9️⃣ Control individual (flex-grow, flex-shrink, flex-basis)

```css
.item {
  flex: 1;
}
```

📌 Hace que los elementos crezcan de forma proporcional.

---

## 🔟 Flexbox responsive (básico)

```css
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
  }
}
```

---

## 🆚 Flexbox vs Grid

| Flexbox | Grid |
|-------|------|
| Una dirección | Filas y columnas |
| Menús, botones | Layouts grandes |
| Alineación | Estructura |

📌 En proyectos web:
- **Flexbox** → navbar, footer, cards
- **Grid** → productos, secciones principales

---

## 🛍️ Aplicado a tu proyecto

```css
.nav-start {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

## 🧠 Regla de oro
1️⃣ Usa Flexbox para **alinear**
2️⃣ Usa Grid para **estructurar**
3️⃣ Combínalos sin miedo

---

📌 **Conclusión:**
Flexbox hace que la alineación en CSS sea sencilla, limpia y adaptable. Es indispensable para interfaces modernas.

