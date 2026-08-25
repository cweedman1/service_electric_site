"""Create production WebP derivatives from immutable source photography.

Run from the project root. The role map below is deliberately small; add a new
role only when an image has a defined layout use. Pillow is the only build-time
dependency and is not required to serve the site.
"""

from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "images"
OUTPUT = ROOT / "assets" / "optimized" / "images"

ROLES = {
    "hero-electrical": ("toolmash-expo-PkHf7BUWbtk-unsplash.jpg", (4, 3), [720, 1200, 1600]),
    "panel-detail": ("bruno-guerrero-hP0yzStvp-M-unsplash.jpg", (4, 3), [640, 960, 1440]),
    "diagnostics": ("hobi-industri-NLBJ2I0lNr4-unsplash.jpg", (4, 3), [640, 960, 1440]),
    "thermal-camera": ("jakub-zerdzicki-B1Mx8T3odhI-unsplash.jpg", (4, 3), [640, 960, 1440]),
    "thermal-display": ("dlxmedia-hu-QZBbjCouORc-unsplash.jpg", (3, 2), [720, 1200, 1800]),
    "worker-ladder": ("david-cain-TVPI5pHpNFw-unsplash.jpg", (4, 5), [560, 880, 1200]),
    "finished-lighting": ("erol-ahmed-yP_8zvXWd_c-unsplash.jpg", (3, 2), [720, 1200, 1800]),
    "thermal-operator": ("rene-ranisch-9P9R1s7MSuI-unsplash.jpg", (4, 3), [640, 960, 1440]),
    "thermal-scene": ("jose-matute-azTe7kD3SJk-unsplash.jpg", (4, 3), [640, 960, 1440]),
    "contact-lighting": ("vnwayne-fan-Pgr4KaSevvs-unsplash.jpg", (3, 2), [720, 1200, 1800]),
}


def save_role(role: str, filename: str, ratio: tuple[int, int], widths: list[int]) -> None:
    with Image.open(SOURCE / filename) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        source_ratio = image.width / image.height
        target_ratio = ratio[0] / ratio[1]
        if source_ratio > target_ratio:
            crop_width = round(image.height * target_ratio)
            left = (image.width - crop_width) // 2
            crop = image.crop((left, 0, left + crop_width, image.height))
        else:
            crop_height = round(image.width / target_ratio)
            top = (image.height - crop_height) // 2
            crop = image.crop((0, top, image.width, top + crop_height))

        for width in widths:
            if width > crop.width:
                continue
            height = round(width * ratio[1] / ratio[0])
            resized = crop.resize((width, height), Image.Resampling.LANCZOS)
            resized.save(OUTPUT / f"{role}-{width}.webp", "WEBP", quality=82, method=6)


def save_logo() -> None:
    source = SOURCE / "logo" / "service_electric_logo_original.jpg"
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        # Crop only surrounding blank paper; never reshape, redraw, or trace artwork.
        gray = image.convert("L")
        mask = gray.point(lambda px: 255 if px < 244 else 0)
        bbox = mask.getbbox()
        if not bbox:
            raise RuntimeError("Logo artwork was not detected")
        pad = 28
        bbox = (
            max(0, bbox[0] - pad), max(0, bbox[1] - pad),
            min(image.width, bbox[2] + pad), min(image.height, bbox[3] + pad),
        )
        crop = image.crop(bbox)
        for width in (160, 320, 640, 960):
            if width > crop.width:
                continue
            height = round(width * crop.height / crop.width)
            resized = crop.resize((width, height), Image.Resampling.LANCZOS)
            resized.save(OUTPUT / f"service-electric-logo-{width}.webp", "WEBP", quality=90, method=6)


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for role_name, (source_name, aspect_ratio, output_widths) in ROLES.items():
        save_role(role_name, source_name, aspect_ratio, output_widths)
    save_logo()
    print(f"Generated production images in {OUTPUT}")
