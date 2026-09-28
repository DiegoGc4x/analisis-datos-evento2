"""Funciones auxiliares compartidas por los notebooks."""
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
FIGS = ROOT / "reports" / "figures"


def guardar_fig(nombre: str, fig=None, dpi: int = 120):
    """Guarda la figura actual (o la indicada) en reports/figures."""
    FIGS.mkdir(parents=True, exist_ok=True)
    (fig or plt.gcf()).savefig(FIGS / f"{nombre}.png", dpi=dpi, bbox_inches="tight")


def outliers_iqr(s, k: float = 1.5):
    """Máscara booleana de outliers por el criterio de Tukey (IQR)."""
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    return (s < q1 - k * iqr) | (s > q3 + k * iqr)

