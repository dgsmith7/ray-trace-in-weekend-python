from Hittable import Hittable, HitRecord
from Ray import Ray
from Interval import Interval

class HittableList(Hittable):
    def __init__(self, object=None):
        self.objects = []
        if object:
            self.add(object)

    def clear(self):
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def hit(self, r: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = ray_t.max
        for obj in self.objects:
            if obj.hit(r, Interval(ray_t.min, closest_so_far), temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.front_face = temp_rec.front_face
                rec.mat = temp_rec.mat
        return hit_anything