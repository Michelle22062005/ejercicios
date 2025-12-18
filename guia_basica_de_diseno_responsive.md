# 📱 Guía básica de Diseño Responsive (Responsive Design)

El **diseño responsive** permite que una página web se adapte correctamente a **computadores, tablets y celulares**, mejorando la experiencia del usuario en cualquier dispositivo.

---

## 🧠 1. ¿Qué es Responsive Design?
Es una técnica de diseño web que hace que los elementos:
- Cambien de tamaño
- Se reorganicen
- Se oculten o muestren

dependiendo del **tamaño de la pantalla**.

---

## 2️⃣ Meta viewport (OBLIGATORIO)

Sin esta línea, el responsive **no funciona bien**:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

📌 Debe ir siempre en el `<head>`.

---

## 3️⃣ Media Queries
Las **media queries** permiten aplicar estilos según el tamaño de pantalla.

### Sintaxis básica
```css
@media (max-width: 768px) {
  /* estilos para pantallas pequeñas */
}
```

---

## 4️⃣ Tamaños más usados

| Dispositivo | Tamaño |
|-----------|--------|
| Desktop | +1024px |
| Tablet | 768px |
| Mobile | 480px |

---

## 5️⃣ Ejemplo práctico (responsive con Flexbox)

```css
.navbar {
  display: flex;
  justify-content: space-between;
}

@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    gap: 16px;
  }
}
```

👉 En móvil el menú se pone en columna.

---

## 6️⃣ Responsive con Grid (recomendado)

```css
.productos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
```

✔ Se adapta automáticamente
✔ No necesita media queries

---

## 7️⃣ Imágenes Responsive

```css
img {
  max-width: 100%;
  height: auto;
}
```

📌 Evita que las imágenes se salgan del contenedor.

---

## 8️⃣ Texto Responsive

```css
body {
  font-size: clamp(14px, 2vw, 18px);
}
```

👉 El texto se adapta al tamaño de pantalla.

---

## 9️⃣ Ocultar o mostrar elementos

```css
@media (max-width: 768px) {
  .desktop-only {
    display: none;
  }
}
```

---

## 🔟 Mobile First (RECOMENDADO)

```css
/* Estilos base (mobile) */
.card {
  width: 100%;
}

@media (min-width: 768px) {
  .card {
    width: 50%;
  }
}
```

📌 Primero se diseña para móvil, luego para pantallas grandes.

---

## 🛍️ Aplicado a tu proyecto

```css
.container-imagenes1 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

@media (max-width: 768px) {
  .nav-start ul {
    flex-direction: column;
  }
}
```

---

## 🧠 Buenas prácticas
✔ Usa `auto-fit` y `minmax()`
✔ Evita tamaños fijos (px)
✔ Usa `%`, `fr`, `vw`, `vh`
✔ Prueba en el inspector del navegador

---

## 📌 Conclusión
El diseño responsive es esencial para crear sitios web modernos, accesibles y profesionales. Combinado con **Grid** y **Flexbox**, permite layouts flexibles y adaptables a cualquier dispositivo.

- https://www.figma.com/design/nt3N95w4iIr9Ko6bmaKYDC/Responsive-Landing-Page-Design-_-Website-Home-Page-Design-_-Agency-Website-UI-Design--Community-?node-id=204-686&t=58TUFbO43iPymx5i-1