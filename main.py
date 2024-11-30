import os
from Vec3 import Color, Vec3, Point3
from color import write_color

filename = "image1.ppm"
image_height = 256
image_width = 256

def main():
  f = openNewImageFile()
  render(f)

def openNewImageFile():
  if os.path.exists(filename):
    os.remove(filename)
  return open(filename, "a")

def render(file):
  file.write("P3\n")
  txt = f"{image_width} {image_height}\n"
  file.write(txt)
  file.write("255\n")
  for j in range(image_height):
    lines = image_height - j
    txt = f"Scanlines remaining: {lines}"
    print(txt)
    for i in range(image_width):
      pixel_color = Color(i/(image_width-1), j/(image_height-1), 0)
      write_color(file, pixel_color)
  file.close()
  print("Done.\n")

main()