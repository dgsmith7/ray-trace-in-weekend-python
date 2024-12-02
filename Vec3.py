import math
import random
from utilities import random_range
class Vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, i):
        return self.e[i]

    def __setitem__(self, i, value):
        self.e[i] = value

    def __iadd__(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self

    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __itruediv__(self, t):
        return self.__imul__(1/t)

    def __add__(self, v):
        return Vec3(self.e[0] + v.e[0], self.e[1] + v.e[1], self.e[2] + v.e[2])

    def __sub__(self, v):
        return Vec3(self.e[0] - v.e[0], self.e[1] - v.e[1], self.e[2] - v.e[2])

    def __mul__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.e[0] * t.e[0], self.e[1] * t.e[1], self.e[2] * t.e[2])
        else:
            return Vec3(self.e[0] * t, self.e[1] * t, self.e[2] * t)

    def __rmul__(self, t):
        return self.__mul__(t)

    def __truediv__(self, t):
        return Vec3(self.e[0] / t, self.e[1] / t, self.e[2] / t)

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0]**2 + self.e[1]**2 + self.e[2]**2

    def near_zero(self):
        s = 1e-8
        return (abs(self.e[0]) < s) and (abs(self.e[1]) < s) and (abs(self.e[2]) < s)

    @staticmethod
    def random():
        return Vec3(random.random(), random.random(), random.random())

    @staticmethod
    def random_range(min, max):
        return Vec3(random_range(min, max), random_range(min, max), random_range(min, max))

# Vector Utility Functions

    def vec3_add(u, v):
        return Vec3(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2])
    
    def vec3_sub(u, v):
        return Vec3(u.e[0] - v.e[0], u.e[1] - v.e[1], u.e[2] - v.e[2])
    
    def vec3_mul(u, v):
        return Vec3(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2])
    
    def vec3_mul_scalar(t, v):
        return Vec3(t * v.e[0], t * v.e[1], t * v.e[2])
    
    def vec3_div_scalar(v, t):
        if (t == 0):
            t = 1e-8
        return Vec3(v.e[0] / t, v.e[1] / t, v.e[2] / t)
    
    def dot(u, v):
        return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2]

    def cross(u, v):
        return Vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
                    u.e[2] * v.e[0] - u.e[0] * v.e[2],
                    u.e[0] * v.e[1] - u.e[1] * v.e[0])
    
    def unit_vector(v):
        return Vec3.vec3_div_scalar(v, v.length())

    def random_unit_vector():
        while True:
            p = Vec3.random_range(-1, 1)
            lensq = p.length_squared()
            if 1e-160 < lensq <= 1.0:
                return Vec3.vec3_div_scalar(p, math.sqrt(lensq))

    def random_on_hemisphere(normal):
        on_unit_sphere = Vec3.random_unit_vector()
        if Vec3.dot(on_unit_sphere, normal) > 0.0:
            return on_unit_sphere
        else:
            return -on_unit_sphere

    def reflect(v, n):
        return Vec3.vec3_sub(v, Vec3.vec3_mul_scalar(2 * Vec3.dot(v, n), n))
        #return v - 2*Vec3.dot(v,n)*n
        #return v - n * ((v[0] * n[0] + v[1] * n[1] + v[2] * n[2] ) * 2)
    
# Point3 is just an alias for Vec3, but useful for geometric clarity in the code.
Point3 = Vec3

# Color is just an alias for Vec3, but useful for clarity in the code.
Color = Vec3