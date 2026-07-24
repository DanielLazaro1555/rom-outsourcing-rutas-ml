# Ejecutar con Podman

## 1. Crear `.env`

En la raíz del proyecto debe existir:

```env
ACCESS_KEY=Nicolas10
SECRET_KEY=algo_secreto_super_seguro_2026
DB_PASSWORD=Nicolas10
```

## 2. Levantar la aplicación

```bash
podman-compose up --build -d
```

## 3. Verificar que levantó bien

```bash
podman ps --format '{{.Names}} {{.Status}} {{.Ports}}'
```

```bash
podman logs --tail 80 sistema-rutas-promotores
```

Debe verse:

- `sistema-rutas-promotores` en puerto `5000`
- `sistema-rutas-db` en puerto `5432`
- Flask corriendo en `http://127.0.0.1:5000`

## 4. Abrir la aplicación

```text
http://localhost:5000
```

Credenciales base de prueba:

- `admin@rom.com`
- `analista@rom.com`

Contraseña:

```text
password
```

## 5. Compartir con TryCloudflare

Solo después de confirmar que la app ya responde en `localhost:5000`.

```bash
podman run --rm docker.io/cloudflare/cloudflared:latest tunnel --no-autoupdate --url http://host.containers.internal:5000
```

Ese comando devolverá una URL como:

```text
https://xxxxx.trycloudflare.com
```

## 6. Apagar todo

```bash
podman-compose down
```

## Nota

- No se necesita `venv`
- No se necesita instalar dependencias Python en el host
- Todo el flujo oficial corre con Podman
