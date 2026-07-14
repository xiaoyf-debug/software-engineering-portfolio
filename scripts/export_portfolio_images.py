from pathlib import Path

from PIL import Image


root = Path(__file__).resolve().parent.parent
source = root / "tmp" / "pdfs"
output = root / "output" / "images"
output.mkdir(parents=True, exist_ok=True)

pages = []
for index in range(1, 6):
    image = Image.open(source / f"portfolio-page-{index}.png").convert("RGB")
    page_path = output / f"Xiao_Yufei_Portfolio_Page_{index}.jpg"
    image.save(page_path, "JPEG", quality=90, optimize=True, progressive=True)
    pages.append(image)

target_width = 1200
resized = []
for page in pages:
    height = round(page.height * target_width / page.width)
    resized.append(page.resize((target_width, height), Image.Resampling.LANCZOS))

gap = 20
canvas = Image.new("RGB", (target_width, sum(page.height for page in resized) + gap * (len(resized) - 1)), "#e8f0fe")
y = 0
for page in resized:
    canvas.paste(page, (0, y))
    y += page.height + gap

canvas.save(output / "Xiao_Yufei_Portfolio_Long.jpg", "JPEG", quality=88, optimize=True, progressive=True)
