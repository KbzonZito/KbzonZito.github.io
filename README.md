# KbzonZito.github.io

Mi web personal para presentar mis apps, en español e inglés. Se publica con GitHub Pages en https://kbzonzito.github.io

## Estructura

```
tools/build.py                  Textos y apps: aquí se edita todo
index.html, contacto.html       Español (generados)
apps/<app>/index.html           Página de cada app
apps/<app>/privacidad.html      Política de privacidad (la URL para Google Play)
en/...                          Inglés (generados: contact.html, privacy.html)
assets/                         CSS, JS e iconos (assets/apps/)
```

## Editar textos o añadir una app

1. Edita `tools/build.py`: los textos de la interfaz están en `T` y las apps en `APPS`
   (copia un bloque existente; pon el icono en `assets/apps/`).
2. Regenera las páginas:

   ```bash
   python3 tools/build.py
   ```

3. `git commit` + `git push` y en ~1 minuto estará online.

No edites los `.html` a mano: se sobrescriben al regenerar.

## Probar en local

```bash
python3 -m http.server 8000
```

Y abre http://localhost:8000
