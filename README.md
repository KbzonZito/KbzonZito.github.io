# KbzonZito.github.io

Mi web personal para presentar mis apps. Se publica con GitHub Pages en https://kbzonzito.github.io

## Estructura

```
index.html                    Portada con la lista de apps
contacto.html                 Contacto / soporte
apps/<app>/index.html         Página de cada app
apps/<app>/privacidad.html    Política de privacidad (la que se enlaza en Google Play / App Store)
assets/                       CSS, iconos e imágenes
```

## Añadir una app nueva

1. Copia la carpeta `apps/mi-app` con el nombre de la nueva app (p. ej. `apps/mi-juego`).
2. Edita el texto, el icono y los enlaces de la tienda.
3. Añade su tarjeta (`<article class="card">`) en `index.html`.
4. `git commit` + `git push` y en ~1 minuto estará online.

## Probar en local

```bash
python3 -m http.server 8000
```

Y abre http://localhost:8000
