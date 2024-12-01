import os
from Vec3 import Point3
from HittableList import HittableList
from Sphere import Sphere
from Camera import Camera

filename = "image10.ppm"

# World
world = HittableList()
world.add(Sphere(Point3(0, 0, -1), 0.5))
world.add(Sphere(Point3(0, -100.5, -1), 100))

cam = Camera()

def main():
  # Render and write image to file
  f = openNewImageFile()
  cam.render(f, world)
  f.close()
  print("Done.\n")

def openNewImageFile():
  if os.path.exists(filename):
    os.remove(filename)
  return open(filename, "a")

main()