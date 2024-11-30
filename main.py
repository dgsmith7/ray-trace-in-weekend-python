import os

filename = "image1.ppm"
imageHeight = 256
imageWidth = 256

def main():
  f = openNewImageFile()
  render(f)

def openNewImageFile():
  if os.path.exists(filename):
    os.remove(filename)
  return open(filename, "a")

def render(file):
  print(type(file))
  file.write("P3\n")
  txt = f"{imageWidth} {imageHeight}\n"
  file.write(txt)
  file.write("255\n")
  for i in range(imageHeight):
    counter = 0
    for j in range(imageWidth):
      lines = imageHeight - j
      txt = f"Scanlines remaining: {lines}"
      print(txt)
      r = int(255 * (i / (imageHeight-1)))
      g = int(255 * (j / (imageWidth-1)))
      b = int(255 * (0.0))
      txt = f"{r} {g} {b}   "
      file.write(txt)
      counter = counter + 1
      if (counter == 4): 
        counter = 0
        file.write("\n")
  file.close()
  print("Done.\n")

main()