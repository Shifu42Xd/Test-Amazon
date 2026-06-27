# 🛒 Testing Automático – Página de Compras (Amazon)

Proyecto de testing automático desarrollado para el **Práctico N° 7.3 – Actividad 2** de la asignatura **Ingeniería de Software III** (UNSJ, ciclo 2026).

Se automatizan 3 casos de prueba sobre el sitio [Amazon](https://www.amazon.com) utilizando **Selenium + Python**, cubriendo los flujos principales de una página de compras.

---

## 📋 Casos de Prueba

| ID | Descripción |
|---|---|
| CP-01 | Búsqueda de producto existente |
| CP-02 | Agregar producto al carrito |
| CP-03 | Búsqueda de producto inexistente |

---

## ⚙️ Requisitos

- Python 3.8 o superior
- pip
- Un navegador basado en Chromium instalado (Google Chrome, Brave, Opera, etc.)
- ChromeDriver compatible con tu versión del navegador → [Descargar aquí](https://chromedriver.chromium.org/downloads)

> **Nota:** ChromeDriver debe ser de la misma versión que tu navegador. Para verificar la versión de tu navegador, ingresá a `chrome://settings/help` (o equivalente).

---

## 🚀 Instalación

**1. Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

**2. (Opcional) Crear un entorno virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

**3. Instalar dependencias**
```bash
pip install selenium
```

**4. Configurar ChromeDriver**

Descargá ChromeDriver y colocá la ruta en el script `testAmazon.py`:

```python
CHROMEDRIVER_PATH = r"C:\ruta\a\tu\chromedriver.exe"
```

Si usás Brave u otro navegador basado en Chromium, también configurá la ruta del ejecutable:

```python
options.binary_location = r"C:\ruta\a\tu\navegador.exe"
```

---

## ▶️ Ejecución

Desde la terminal, dentro del directorio del proyecto:

```bash
python testAmazon.py
```

Si todo está configurado correctamente, se abrirá una ventana del navegador y verás la ejecución de los 3 casos de prueba en tiempo real.

---

## ✅ Salida Esperada

```
test_01_busqueda_producto_existente ... 
CP-01 OK: 22 resultados encontrados
ok

test_02_agregar_al_carrito ... 
CP-02 OK: Página de producto cargada correctamente
ok

test_03_busqueda_producto_inexistente ... 
CP-03 OK: Amazon respondió con sugerencias ante búsqueda inválida (comportamiento válido)
ok

----------------------------------------------------------------------
Ran 3 tests in ~30s

OK
```

---

## 📁 Estructura del Proyecto

```
📦 tu-repositorio
 ┣ 📄 testAmazon.py       # Script principal con los 3 casos de prueba
 ┗ 📄 README.md           # Este archivo
```

---

## ⚠️ Consideraciones

- Amazon puede bloquear accesos automatizados dependiendo de la región o la velocidad de conexión. En ese caso, intentá ejecutar el script con una VPN o en otro momento.
- Los tiempos de ejecución varían según la velocidad de conexión a internet.
- El script fue probado con el navegador **Brave** sobre **Windows**.

---

## 👥 Autores

- ZUMEL, Candela – Reg: 20576
- ESPEJO, Luciano – Reg: 20782
- SANTILLÁN, Joaquín – Reg: 20260

**Cátedra:** Ingeniería de Software III – UNSJ  
**Profesores:** Zapata Sergio / Luna Humberto  
**Año:** 2026
