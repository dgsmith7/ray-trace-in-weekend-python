from Hittable import Hittable, HitRecord
from Ray import Ray

class HittableList(Hittable):
    def __init__(self, object=None):
        self.objects = []
        if object:
            self.add(object)

    def clear(self):
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = ray_tmax

        for obj in self.objects:
            if obj.hit(r, ray_tmin, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal

        return hit_anything