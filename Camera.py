from Hittable import HitRecord
from Vec3 import Color, Vec3, Point3
from Interval import Interval
from Ray import Ray
from color import write_color

class Camera:

  def __init__(self):
    self.aspect_ratio = 16.0 / 9.0
    self.image_width = 400

  def render(self, file, world):
    self.initialize()
    file.write("P3\n")
    txt = f"{self.image_width} {self.image_height}\n"
    file.write(txt)
    file.write("255\n")
    for j in range(self.image_height):
      lines = self.image_height - j
      txt = f"Scanlines remaining: {lines}"
      print(txt)
      for i in range(self.image_width):
        pixel_center = self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
        ray_direction = pixel_center - self.center
        r = Ray(self.center, ray_direction)
        pixel_color = self.ray_color(r, world)
        write_color(file, pixel_color)

  def ray_color(self, r, world):
    rec = HitRecord()
    if (world.hit(r, Interval(0, float('inf')), rec)):  
      return 0.5 * (rec.normal + Color(1, 1, 1))
    unit_direction = Vec3.unit_vector(r.direction())
    a = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - a) * Color(1.0, 1.0, 1.0) + a * Color(0.5, 0.7, 1.0)

  def initialize(self):
    # Calcualte image height and ensure it is at least 1
    self.image_height = int(self.image_width / self.aspect_ratio)
    if (self.image_height < 1):
      self.image_height = 1
    self.center = Point3(0, 0, 0)
    # Determine viewpot dimensions
    self.focal_length = 1.0
    self.viewport_height = 2.0
    self.viewport_width = self.viewport_height * (self.image_width/self.image_height)
    # Calculate Vectors across the horizontal and down the vertical viewport edges.
    self.viewport_u = Vec3(self.viewport_width, 0, 0)
    self.viewport_v = Vec3(0, -self.viewport_height, 0)
    # Calculate the horizontal and vertical delta vectors from pixel to pixel.
    self.pixel_delta_u = self.viewport_u / self.image_width
    self.pixel_delta_v = self.viewport_v / self.image_height
    # Calculate the location of the upper left pixel.
    self.viewport_upper_left = self.center - Vec3(0, 0, self.focal_length) - (self.viewport_u/2) - (self.viewport_v/2)
    self.pixel00_loc = self.viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)
