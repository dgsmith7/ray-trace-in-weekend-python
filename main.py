import os
from Vec3 import Vec3, Point3, Color
from HittableList import HittableList
from Sphere import Sphere
from Camera import Camera
from Material import Lambertian, Metal, Dielectric
import math
import random
import datetime

filename = "image21.ppm"

# World
world = HittableList()

material_ground = Lambertian(Color(0.8, 0.8, 0.0))
material_center = Lambertian(Color(0.1, 0.2, 0.5))
#material_left = Metal(Color(0.8, 0.8, 0.8))
material_left   = Dielectric(1.50)
material_bubble = Dielectric(1.0 / 1.50)
material_right  = Metal(Color(0.8, 0.6, 0.2), 0.0)

#image 21
world.add(Sphere(Point3( 0.0, -100.5, -1.0), 100.0, material_ground))
world.add(Sphere(Point3( 0.0,    0.0, -1.2),   0.5, material_center))
world.add(Sphere(Point3(-1.0,    0.0, -1.0),   0.5, material_left))
world.add(Sphere(Point3(-1.0,    0.0, -1.0),   0.4, material_bubble))
world.add(Sphere(Point3( 1.0,    0.0, -1.0),   0.5, material_right))

#image 23
# ground_material = Lambertian(Color(0.5, 0.5, 0.5))
# world.add(Sphere(Point3(0.0,-1000.0,0.0), 1000, ground_material))

# for a in range(-11, 11):
#     for b in range(-11, 11):
#         choose_mat = random.random()
#         center = Point3(a + 0.9*random.random(), 0.2, b + 0.9*random.random())
#         if ((center - Point3(4, 0.2, 0)).length() > 0.9):
#             if (choose_mat < 0.8):
#                 # diffuse
#                 albedo = Color(random.random(),random.random(),random.random())
#                 world.add(Sphere(center, 0.2, Lambertian(albedo)))
#             elif (choose_mat < 0.95):
#                 # metal
#               albedo = Color(Vec3.random_double(0.5, 1.0),Vec3.random_double(0.5, 1.0),Vec3.random_double(0.5, 1.0))
#               fuzz = Vec3.random_range(0.0, 0.5)
#               world.add(Sphere(center, 0.2, Metal(albedo, fuzz)))
#             else:
#                 # glass
#                 world.add(Sphere(center, 0.2, Dielectric(1.5)))

# world.add(Sphere(Point3(0, 1, 0), 1.0, Dielectric(1.5)))

# world.add(Sphere(Point3(-4, 1, 0), 1.0, Lambertian(Color(0.4, 0.2, 0.1))))

# world.add(Sphere(Point3(4, 1, 0), 1.0, Metal(Color(0.7, 0.6, 0.5), 0.0)))

cam = Camera()

def main():
  # Render and write image to file
  starttime = datetime.datetime.now()
  print("Started rendering at: ", starttime)
  f = openNewImageFile()
  cam.render(f, world)
  f.close()
  endtime = datetime.datetime.now()
  print("Finisheded rendering at: ", endtime)
  print("The render took: ", endtime-starttime)
  print("Done.\n")
  

def openNewImageFile():
  if os.path.exists(filename):
    os.remove(filename)
  return open(filename, "a")

main()