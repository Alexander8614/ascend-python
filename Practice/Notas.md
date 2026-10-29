# NOTAS · Capacidad IA
Bitácora personal. Solo entra lo que me costó.

---

## COMANDOS

### Entorno virtual
Mi terminal es **Git Bash** (se ve `MINGW64` en la línea).

Crear:
    python -m venv .venv

Activar:
    source .venv/Scripts/activate

En PowerShell sería `.venv\Scripts\activate` — barras al revés.
Funciona si aparece `(.venv)` al inicio de la línea.

### Comprobar instalación
    python --version

---

## CONCEPTOS

### PATH
Lista de carpetas donde Windows busca los programas cuando escribo
un comando. Si Python no está en el PATH, queda instalado pero el
sistema no lo encuentra y dice "comando no reconocido".
Por eso hay que marcar "Add python.exe to PATH" al instalar.

### Entorno virtual
Caja aislada de librerías para un solo proyecto. Sin esto, todo se
instala en el sistema y un proyecto puede romper a otro.
Se desactiva al cerrar VS Code: hay que activarlo cada vez.

---

## ERRORES RESUELTOS

### `bash: .venvScriptsactivate: command not found`
**Causa:** usé barras invertidas en Git Bash, que las ignora.
**Solución:** `source .venv/Scripts/activate` con barras normales.
**Aprendizaje:** el mismo comando cambia según la terminal, y los
tutoriales casi nunca dicen cuál están usando.

---

## POR REVISAR

- (aquí van las dudas que quedan abiertas)
## VARIABLES DE HOY
print()  Mostrar en pantalla
len()  cantidad de caracteres
input()  solicita que el usuario haga algo (siempre genra string aunque le pase un numero)
str() lo vuelve string
int() lo vuelve entero
float() lo vuelve decimal
type() me da el tipo
round()  me devuelve el entero mas cercano, con parametro adicioal puedo decidir cuantos decimales dejo
abs() me devuelve al valor absoluto 