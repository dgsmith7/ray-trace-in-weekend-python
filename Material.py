from Ray import Ray
from Vec3 import Vec3, Color
import math
import random

class Material:
    def scatter(self, ray_in, hit_record):
        raise NotImplementedError("Subclasses must implement this method")
    
class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, hit_record):
        scatter_direction = hit_record.normal + Vec3.random_unit_vector()
        if (scatter_direction.near_zero()):
            scatter_direction = hit_record.normal
        scattered = Ray(hit_record.p, scatter_direction)
        attenuation = self.albedo
        return True, scattered, attenuation 
        
class Metal(Material):
    def __init__(self, albedo, fuzz=0.0):
        self.albedo = albedo
        self.fuzz = fuzz

    def scatter(self, ray_in, hit_record):
        reflected = Vec3.reflect(ray_in.direction(), hit_record.normal)
        scattered = Ray(hit_record.p, reflected + (self.fuzz * Vec3.random_unit_vector()))
        attenuation = self.albedo
        return (Vec3.dot(scattered.direction(), hit_record.normal) > 0), scattered, attenuation

class Dielectric(Material):
    def __init__(self, ir):  # Index of Refraction
        self.ir = ir

    def scatter(self, ray_in, hit_record):
        attenuation = Color(1.0, 1.0, 1.0)
        refraction_ratio = 1.0/self.ir if hit_record.front_face else self.ir

        unit_direction = Vec3.unit_vector(ray_in.direction())
        cos_theta = min(Vec3.dot(-unit_direction, hit_record.normal), 1.0)
        sin_theta = math.sqrt(1.0 - cos_theta*cos_theta)

        cannot_refract = refraction_ratio * sin_theta > 1.0

        if cannot_refract or self.reflectance(cos_theta, refraction_ratio) > random.random():
            direction = Vec3.reflect(unit_direction, hit_record.normal)
        else:
            direction = Vec3.refract(unit_direction, hit_record.normal, refraction_ratio)

        scattered = Ray(hit_record.p, direction)
        return True, scattered, attenuation

    def reflectance(self, cosine, ref_idx):
        # Use Schlick's approximation for reflectance.
        r0 = (1 - ref_idx) / (1 + ref_idx)
        r0 = r0 * r0
        return r0 + (1 - r0) * pow((1 - cosine), 5)