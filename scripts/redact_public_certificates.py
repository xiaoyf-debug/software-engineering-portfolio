from pathlib import Path

from PIL import Image, ImageFilter


root = Path(__file__).resolve().parent.parent
images = root / "public" / "images"


def blur_regions(source_name, output_name, regions):
    image = Image.open(images / source_name).convert("RGB")
    for box in regions:
        crop = image.crop(box).filter(ImageFilter.GaussianBlur(radius=18))
        image.paste(crop, box)
    image.save(images / output_name, quality=92, optimize=True)


blur_regions(
    "award-lanqiao-cpp.jpg",
    "award-lanqiao-cpp-public.jpg",
    [(390, 770, 920, 860), (420, 1340, 830, 1425)],
)

blur_regions(
    "award-math-competition.jpg",
    "award-math-competition-public.jpg",
    [(210, 775, 660, 845)],
)
