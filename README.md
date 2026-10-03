# Evento Evaluativo 2 · Análisis de Datos — NYC Taxi Trips

**Instituto Tecnológico Metropolitano (ITM)** · Ingeniería de Sistemas · Análisis de Datos · 2026-2
**Docente:** Daniel Alexis Nieto Mora · **Grupo 8**

**Integrantes**

- Diego Alejandro Gómez Carmona
- Jorge Elias Builes Chavarria
- Juan Pablo Vasquez Tobon
- Sergio Alvarez Hernandez

**Video:** [Ver video en YouTube](https://youtu.be/BHiJ4O1mWec)

---

## Objetivo

Explorar varias bases de datos, justificar la elección de una, hacer un análisis exploratorio completo (EDA) y aplicar preprocesamiento y reducción de dimensionalidad para dejar los datos listos para un modelado posterior.

## Estructura del repositorio

```
├── data/
│   ├── raw/                 # datos originales (taxis.csv, sms.tsv)
│   └── processed/           # taxis_clean.csv, taxis_preprocesado.csv, taxis_pca.csv
├── notebooks/
│   ├── 01_exploracion_bases.ipynb           # Fase 1
│   ├── 02_eda.ipynb                         # Fase 2
│   └── 03_preprocesamiento_reduccion.ipynb  # Fase 3
├── reports/figures/         # todas las gráficas exportadas
├── src/utils.py             # rutas y funciones compartidas (outliers, guardado de figuras)
└── requirements.txt
```

## Cómo ejecutar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Ejecutar los notebooks **en orden** (01 → 02 → 03): el 02 genera `taxis_clean.csv`, que usa el 03. Digits se carga desde `scikit-learn`, no requiere descarga.

## Fase 1 · Bases exploradas

| Base | Tipo | Fuente | Tipo de fuente | Registros × atributos | Documentación |
|---|---|---|---|---|---|
| NYC Taxi Trips (mar-2019) | Tabular | NYC TLC, vía `seaborn-data` | Secundaria | 6.433 × 14 | Alta |
| Handwritten Digits | Imágenes 8×8 | UCI, vía `scikit-learn` | Secundaria | 1.797 × 64 px | Alta |
| SMS Spam Collection | Texto | UCI (Almeida et al., 2011) | Secundaria | 5.572 × 2 | Media |

**Seleccionada: NYC Taxi Trips** (puntaje ponderado 4,8/5). Es la única que combina variables numéricas, categóricas y de fecha-hora, con faltantes y outliers reales, lo que permite aplicar todo lo que pide el EDA. Digits y SMS son muy limpias y homogéneas.

## Fase 2 · EDA

Faltantes (tratamiento con categoría + indicador), outliers (boxplot + IQR), distribuciones (histogramas con densidad), análisis univariado, multivariado (correlación, dispersión, tablas cruzadas, mapa de calor hora × día), 5 hipótesis e insights.

**Hallazgos principales**

1. La tarifa es casi función de la distancia (r = 0,92); distancia, tarifa, total y duración son redundantes.
2. La propina en efectivo siempre es 0: el sistema no la registra.
3. Los viajes a aeropuertos (~6 %) explican el 53 % de los outliers de tarifa (mediana 36 vs 9 USD). Se conservan porque son reales.
4. Manhattan concentra el 82 % de las recogidas; los taxis verdes operan fuera del centro.
5. Picos de demanda entre semana a las 8–9 h y 18–19 h.

**Calidad de datos:** faltantes < 1 % en pago y zonas (zona y municipio faltan siempre juntos), 96 viajes con 0 pasajeros, 51 con distancia 0 y 6 con duración ≤ 0. Se imputó con categorías explícitas + indicadores y se marcaron los viajes sospechosos, sin eliminar filas.

## Fase 3 · Preprocesamiento y reducción

- **Codificación:** One-Hot para color, pago y municipios.
- **Escalado:** `log1p` + `StandardScaler` para las variables sesgadas; `StandardScaler` para las demás numéricas. Todo en un `ColumnTransformer` → 29 columnas sin faltantes.
- **PCA:** 5 componentes retienen el 96 % de la varianza numérica. PC1 = tamaño del viaje (48 %), PC2 = hora/día, PC3 = pasajeros.

## Fuentes

- NYC Taxi & Limousine Commission — TLC Trip Record Data.
- Waskom, M. — `seaborn-data` (https://github.com/mwaskom/seaborn-data).
- Alpaydin, E. & Kaynak, C. (1998). *Optical Recognition of Handwritten Digits*. UCI ML Repository.
- Almeida, T., Gómez Hidalgo, J. M. & Yamakami, A. (2011). *SMS Spam Collection*. UCI ML Repository.
