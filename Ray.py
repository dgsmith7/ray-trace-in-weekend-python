class Ray:
  """Simple Ray comprised of two points"""
  def __init__(self, orig, dir):
    self.orig = orig
    self.dir = dir

  def origin(self):
    return self.orig
  
  def direction(self):
    return self.dir

  def at(self, t):
    return self.orig + (t * self.dir)
    