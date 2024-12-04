from abc import ABC, abstractmethod
from Vec3 import Point3, Vec3
from Ray import Ray
from Interval import Interval
from Material import Material

class HitRecord:
    def __init__(self):
        self.p = Point3()
        self.normal = Vec3()
        self.t = 0.0
        self.front_face = False
        self.mat = None#Material()

    def set_face_normal(self, r, outward_normal):
        # Sets the hit record normal vector.
        # NOTE: the parameter `outward_normal` is assumed to have unit length.
        self.front_face = Vec3.dot(r.direction(), outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        pass