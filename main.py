import os
from Vec3 import Point3, Color
from HittableList import HittableList
from Sphere import Sphere
from Camera import Camera
from Material import Lambertian, Metal, Material#

filename = "image13.ppm"

# World
world = HittableList()

material_ground = Lambertian(Color(0.8, 0.8, 0.0))#
material_center = Lambertian(Color(0.1, 0.2, 0.5))#
material_left = Metal(Color(0.8, 0.8, 0.8))#
material_right = Metal(Color(0.8, 0.6, 0.2))#
world.add(Sphere(Point3( 0.0, -100.5, -1.0), 100.0, material_ground))#
world.add(Sphere(Point3( 0.0,    0.0, -1.2),   0.5, material_center))#
world.add(Sphere(Point3(-1.0,    0.0, -1.0),   0.5, material_left))#
world.add(Sphere(Point3( 1.0,    0.0, -1.0),   0.5, material_right))#

# world.add(Sphere(Point3(0, 0, -1), 0.5))
# world.add(Sphere(Point3(0, -100.5, -1), 100))

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