from Interval import Interval

def write_color(file, pixelColor):
  r = pixelColor.x()
  g = pixelColor.y()
  b = pixelColor.z()

  intensity = Interval(0.000, 0.999)
  rbyte = int(256 * intensity.clamp(r))
  gbyte = int(256 * intensity.clamp(g))
  bbyte = int(256 * intensity.clamp(b))

  txt = f"{rbyte} {gbyte} {bbyte}   \n"
  file.write(txt)
