def write_color(file, pixelColor):
  r = pixelColor.x()
  g = pixelColor.y()
  b = pixelColor.z()
  rbyte = int(255 * r)
  gbyte = int(255 * g)
  bbyte = int(255 * b)

  txt = f"{rbyte} {gbyte} {bbyte}   \n"
  file.write(txt)
