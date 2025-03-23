from dataclasses import dataclass

@dataclass
class Immobilier:
    titre: str
    prix: str
    url: str
    images_urls:str = None
    latitude: float = None
    longitude: float = None
    balcon: bool = None
    concierge: bool = None
    ville: str = None
    surface_totale_m2: float = None
    salles_de_bains: int = None
    chambres: int = None
    source: str = "Avito"
    prix_en_m2: float = None
    date_d_achevement: str = None  # 🆕 Completion Date
    developer: str = None  # 🆕 Developer
    contact_phone: str = None  # 🆕 Contact Phone
