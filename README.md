# 🔄 Compilador de Notas Musicales

<div align="center">
  <h3><i>Un compilador e intérprete para generar música a través de código</i></h3>
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![ANTLR4](https://img.shields.io/badge/ANTLR4-lightgrey?style=for-the-badge)
  ![LilyPond](https://img.shields.io/badge/LilyPond-red?style=for-the-badge)
  ![MIDI](https://img.shields.io/badge/MIDI-black?style=for-the-badge)
</div>

## 📋 Descripción

Este proyecto implementa un compilador e intérprete para un lenguaje de programación musical personalizado. Permite escribir código que genera música, produciendo tanto partituras en PDF (usando LilyPond) como archivos MIDI reproducibles.

## ✨ Características Principales

### 🎼 Funcionalidades Musicales
- **Notas Musicales**: Soporte para notas básicas (C, D, E, F, G, A, B) con octavas
- **Reproducción**: Generación automática de archivos MIDI
- **Partituras**: Creación de partituras profesionales en PDF
- **Composición**: Sintaxis intuitiva para escribir música

### 🔧 Características Técnicas
- **Análisis Léxico**: Tokenización de código musical
- **Análisis Sintáctico**: Parsing mediante ANTLR4
- **Interpretación**: Visitor pattern para ejecución
- **Generación de Código**: Salida a formatos LilyPond y MIDI

## 🛠️ Tecnologías

### Compilador
- **Python 3.x**: Lenguaje principal de implementación
- **ANTLR4**: Generador de parser
- **LilyPond**: Sistema de notación musical
- **Biblioteca MIDI**: Generación de archivos MIDI

## 📝 Sintaxis del Lenguaje

```
### Ejemplo de melodía simple
PlayMelody |:
    ### Escala ascendente
    (:) C
    (:) D
    (:) E
    (:) F
    (:) G
    
    ### Melodía
    (:) C
    (:) C
    (:) G
    (:) G
    (:) A
    (:) A
    (:) G
:|
```

## 🎵 Elementos del Lenguaje

### Símbolos Especiales
- `(:)` - Reproducir nota
- `|:` - Inicio de bloque
- `:|` - Fin de bloque
- `###` - Comentarios

### Estructuras
- **Procedimientos**: Definición de melodías y secuencias
- **Bloques**: Agrupación de instrucciones musicales
- **Notas**: Símbolos musicales con octavas opcionales

## ⚙️ Instalación

### Prerrequisitos
- Python 3.x
- ANTLR4
- LilyPond
- Java Runtime Environment (JRE)

### Pasos
1. **Clonar el repositorio**
```bash
git clone https://github.com/Alexandeeer-0/Desarrollo-de-Compiladores-e-Interpretes-Notas-Musical.git
cd Desarrollo-de-Compiladores-e-Interpretes-Notas-Musical
```

2. **Instalar ANTLR4**
```bash
# Descargar ANTLR
curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar

# Configurar CLASSPATH
export CLASSPATH=".:path/to/antlr-4.13.1-complete.jar:$CLASSPATH"
```

3. **Instalar LilyPond**
- Windows: Usar el instalador proporcionado
- Linux/MacOS: Usar el gestor de paquetes del sistema

4. **Generar Parser**
```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 Algoritmia.g4
```

## 🚀 Uso

1. **Escribir código musical**
```bash
# Crear archivo .alg
echo "PlayMelody |: (:) C (:) D (:) E :|" > melodia.alg
```

2. **Compilar y ejecutar**
```bash
python Algoritmia.py melodia.alg
```

3. **Resultados**
- `output.pdf`: Partitura en formato PDF
- `output.ly`: Código fuente LilyPond
- `output.mid`: Archivo MIDI reproducible

## 📊 Estructura del Proyecto

```
PROYECTO_ALGORITMIA/
├── Algoritmia.g4           # Gramática ANTLR4
├── Algoritmia.py           # Programa principal
├── AlgoritmiaLexer.py      # Analizador léxico
├── AlgoritmiaParser.py     # Analizador sintáctico
├── AlgoritmiaVisitor.py    # Intérprete
├── AlgoritmiaInterpreter.py # Implementación del visitor
└── codigo.alg              # Ejemplo de código
```

## 🔍 Proceso de Compilación

1. **Análisis Léxico**: Tokenización del código fuente
2. **Análisis Sintáctico**: Construcción del AST
3. **Interpretación**: Recorrido del AST
4. **Generación**: Creación de archivos de salida

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir: nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## ✨ Agradecimientos

- A la comunidad de ANTLR4
- A los desarrolladores de LilyPond
- A todos los contribuidores del proyecto

---

<div align="center">
  <p>Desarrollado con ❤️ para la comunidad de programadores musicales</p>
</div>
