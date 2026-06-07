from dataclasses import dataclass


@dataclass
class Islem:
    """Represents a financial transaction.

    Attributes:
        id (int): Unique identifier.
        tutar (float): Amount of the transaction.
        tarih (str): Date in YYYY-MM-DD format.
        aciklama (str): Description.
        tip (str): 'gelir' or 'gider'.
    """

    id: int
    tutar: float
    tarih: str  # YYYY-MM-DD
    aciklama: str
    tip: str  # 'gelir' or 'gider'

    def to_dict(self):
        """Return a serializable dictionary for CSV output."""
        return {
            "id": int(self.id),
            "tutar": float(self.tutar),
            "tarih": self.tarih,
            "aciklama": self.aciklama,
            "tip": self.tip,
        }

    @staticmethod
    def from_dict(d):
        """Create an `Islem` instance from a dict (e.g., CSV row)."""
        return Islem(
            id=int(d.get("id")),
            tutar=float(d.get("tutar")),
            tarih=d.get("tarih"),
            aciklama=d.get("aciklama", ""),
            tip=d.get("tip"),
        )
