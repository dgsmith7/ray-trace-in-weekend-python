from Ray import Ray
from Vec3 import Vec3

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
        scattered = Ray(hit_record.p, reflected + self.fuzz * Vec3.random_unit_vector())
        attenuation = self.albedo
        return (Vec3.dot(scattered.direction(), hit_record.normal) > 0), scattered, attenuation
