import os
from Vec3 import Color, Vec3, Point3
from color import write_color
from Ray import Ray
import math 

filename = "image4.ppm"
aspect_ratio = 16.0 / 9.0
image_width = 400
# Calcualte image height and ensure it is at least 1
image_height = int(image_width / aspect_ratio)
if (image_height < 1):
  image_height = 1
else:
  image_height = image_height
# Camera
focal_length = 1.0
viewport_height = 2.0
viewport_width = viewport_height * (image_width/image_height)
camera_center = Point3(0, 0, 0)
# Calculate Vectors across the horizontal and down the vertical viewport edges.
viewport_u = Vec3(viewport_width, 0, 0)
viewport_v = Vec3(0, -viewport_height, 0)
# Calculate the horizontal and vertical delta vectors from pixel to pixel.
pixel_delta_u = viewport_u / image_width
pixel_delta_v = viewport_v / image_height
# Calculate the location of the upper left pixel.
viewport_upper_left = camera_center - Vec3(0, 0, focal_length) - (viewport_u/2) - (viewport_v/2)
pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

def main():
  # Render and write image to file
  f = openNewImageFile()
  render(f, )

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
      pixel_center = pixel00_loc + (i * pixel_delta_u) + (j * pixel_delta_v)
      ray_direction = pixel_center - camera_center
      r = Ray(camera_center, ray_direction)
      pixel_color = ray_color(r)
      write_color(file, pixel_color)
  file.close()
  print("Done.\n")

def hit_sphere(center, radius, r):
  oc = center - r.origin()
  a = Vec3.dot(r.direction(), r.direction())
  b = -2.0 * Vec3.dot(r.direction(), oc)
  c = Vec3.dot(oc, oc) - radius * radius
  discriminant = b * b - 4 * a * c
  if (discriminant < 0):
    return -1.0
  else:
    return (-b - math.sqrt(discriminant)) / (2.0 * a)

def ray_color(r):
  t = hit_sphere(Point3(0, 0, -1), 0.5, r)
  if (t > 0.0):
    N = Vec3.unit_vector(r.at(t) - Vec3(0, 0, -1))
    return 0.5 * Color(N.x() + 1, N.y() + 1, N.z() + 1);
  
  unit_direction = Vec3.unit_vector(r.direction())
  a = 0.5 * (unit_direction.y() + 1.0)
  return ((1.0 - a) * Color(1.0, 1.0, 1.0)) + (a*Color(0.5, 0.7, 1.0))

main()