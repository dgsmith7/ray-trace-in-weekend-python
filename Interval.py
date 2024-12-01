class Interval:
  def __init__(self, min=float('inf'), max=-float('inf')):
    self.min = min
    self.max = max

  def size(self):
    return self.max - self.min

  def contains(self, x):
    return self.min <= x and x <= self.max

  def surrounds(self, x):
    return self.min < x and x < self.max
  
  def clamp(self, x):
    if (x < self.min):
      return self.min
    if (x > self.max):
      return self.max
    else:
      return x

# Define the empty and universe intervals as class attributes
Interval.empty = Interval(float('inf'), -float('inf'))
Interval.universe = Interval(-float('inf'), float('inf'))