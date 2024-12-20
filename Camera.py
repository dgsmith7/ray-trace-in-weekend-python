from Hittable import HitRecord
from Vec3 import Color, Vec3, Point3
from Interval import Interval
from Ray import Ray
from color import write_color
import math
import random

class Camera:

  def __init__(self):
    self.aspect_ratio = 16.0 / 9.0 # Ratio of image width over height
    self.image_width = 500 # Rendered image width in pixel count
    self.samples_per_pixel = 50 # Count of random samples for each pixel
    self.pixel_samples_scale = 1.0 / self.samples_per_pixel # Divisor for averaging samples
    self.max_depth = 50 # Maximum number of ray bounces into scene.  Keep below 48.
    self.vfov = 20 # Vertical view angle (field of view)
    self.lookfrom = Point3(-2,2,1)#(13,2,3)
    self.lookat = Point3(0, 0, -1)
    self.vup = Vec3(0, 1, 0)
    self.defocus_angle = 0#0.6
    self.focus_dist = 10.0

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
        pixel_color = Vec3(0.0,0.0,0.0)
        for sample in range(self.samples_per_pixel):
          r = self.get_ray(i, j)
          pixel_color += self.ray_color(r, self.max_depth, world)
        write_color(file, self.pixel_samples_scale * pixel_color)

  def ray_color(self, r, depth, world):
    # If we've exceeded the ray bounce limit, no more light is gathered.
    if (depth <= 0):
      return Color(0.0,0.0,0.0)
    rec = HitRecord()
    if (world.hit(r, Interval(0.001, float('inf')), rec)): 
      hit, scattered, attenuation = rec.mat.scatter(r, rec)
      if hit:
        return attenuation * self.ray_color(scattered, depth - 1, world)
      return Color(0.0,0.0,0.0)  # Black if ray doesn't scatter
    unit_direction = Vec3.unit_vector(r.direction())
    a = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - a) * Color(1.0, 1.0, 1.0) + a * Color(0.5, 0.7, 1.0)

  def get_ray(self, i, j):
    # Construct a camera ray originating from the origin and directed at randomly sampled
    # point around the pixel location i, j.
    offset = self.sample_square()
    pixel_sample = self.pixel00_loc + ((i + offset.x()) * self.pixel_delta_u) + ((j + offset.y()) * self.pixel_delta_v)
    ray_origin = self.center if (self.defocus_angle <= 0) else self.defocus_disk_sample()
    ray_direction = pixel_sample - ray_origin
    return Ray(ray_origin, ray_direction)

  def sample_square(self):
    # Returns the vector to a random point in the [-.5,-.5]-[+.5,+.5] unit square.
    return Vec3(random.random() - 0.5, random.random() - 0.5, 0)
  
  def defocus_disk_sample(self):
    p = Vec3.random_in_unit_disk()
    return self.center + (p[0] * self.defocus_disk_u) + (p[1] * self.defocus_disk_v)
  
  def initialize(self):
    # Calcualte image height and ensure it is at least 1
    self.image_height = int(self.image_width / self.aspect_ratio)
    if (self.image_height < 1):
      self.image_height = 1
    self.center = self.lookfrom
    # Determine viewport dimensions
    self.theta = math.radians(self.vfov)
    self.h = math.tan(self.theta/2)
    self.viewport_height = 2.0 * self.h * self.focus_dist
    self.viewport_width = self.viewport_height * (self.image_width/self.image_height)
    # Calculate the u,v,w unit basis vectors for the camera coordinate frame
    self.w = Vec3.unit_vector(self.lookfrom - self.lookat)
    self.u = Vec3.unit_vector(Vec3.cross(self.vup, self.w))
    self.v = Vec3.cross(self.w, self.u)
    # Calculate Vectors across the horizontal and down the vertical viewport edges.
    self.viewport_u = self.viewport_width * self.u
    self.viewport_v = self.viewport_height * -self.v
    # Calculate the horizontal and vertical delta vectors from pixel to pixel.
    self.pixel_delta_u = self.viewport_u / self.image_width
    self.pixel_delta_v = self.viewport_v / self.image_height
    # Calculate the location of the upper left pixel.
    self.viewport_upper_left = self.center - (self.focus_dist * self.w) - (self.viewport_u/2) - (self.viewport_v/2)
    self.pixel00_loc = self.viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)
    # Calculate the defouc disk basis vectors
    self.defocus_radius = self.focus_dist * math.tan(math.radians(self.defocus_angle / 2))
    self.defocus_disk_u = self.u * self.defocus_radius
    self.defocus_disk_v = self.v * self.defocus_radius