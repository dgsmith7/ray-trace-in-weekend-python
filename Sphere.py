import math
from Hittable import Hittable, HitRecord
from Vec3 import Point3, Vec3
from Ray import Ray
from Vec3 import Vec3
from Interval import Interval
from Material import Material#

class Sphere(Hittable):
    def __init__(self, center: Point3, radius: float, mat: Material):
    # def __init__(self, center: Point3, radius: float):
        self.center = center
        self.radius = max(0, radius)
        self.mat = mat #

    def hit(self, r: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        oc = self.center - r.origin()
        a = r.direction().length_squared()
        h = Vec3.dot(r.direction(), oc)
        c = oc.length_squared() - self.radius * self.radius

        discriminant = h * h - a * c
        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range.
        if (a == 0):
            a = 1e-8
        root = (h - sqrtd) / a
        if not (ray_t.surrounds(root)): 
            root = (h + sqrtd) / a
            if not (ray_t.surrounds(root)): 
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        rec.mat = self.mat #

        return True