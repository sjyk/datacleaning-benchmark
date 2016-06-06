"""
"""

import numpy
import NoiseModel

class WorkFlowOperator(object):
  """
  """
  def __init__(self, parent=None, children=None):
    self.parent = parent
    self.children = filter(bool, list(children))

  def run(self, X, Y):
    X, Y = self.apply(X, Y)
    if X.shape[0] != Y.shape[0]:
      raise ValueError("X and Y have different shapes: %s != %s" % (X.shape, Y.shape))
    return X, Y
  
  def apply(self, X, Y):
    return X, Y

  def iterpaths(self):
    """
    returns an iterator of paths (list of operators)
    """
    for path in self._iterpaths(self.root, []):
      yield path

  def _iterpaths(self, node, pathsofar=None):
    """
    Runs DFS
    """
    if not pathsofar:
      pathsofar = []

    if node is None:
      if pathsofar:
        yield list(pathsofar)
      else:
        return

    pathsofar.append(node)
    for child in node.children:
      for subpath in self._iterpaths(child, pathsofar):
        yield list(subpath)
    pathsofar.pop()


class WorkFlowNoiseModel(NoiseModel.NoiseModel):
  def __init__(self, 
               shape, 
               probability=0,
               feature_importance=[],
               wf=None):
    """
    wf is the root node of the workflow
    """

    super(WorkFlowNoiseModel, self).__init__(shape, 
    	                             probability, 
    	                             feature_importance)
    if not wf:
      raise ValueError("Workflow should not be empty")

    self.wf = wf
    self.allpaths = list(self.wf.iterpaths)

  def sample_path(self):
    path = random.sample(self.allpaths, 1)[0]
    idx = random.randint(0, len(path)-1)
    path = path[:idx]
    return path
  
  def corrupt(self, X, Y):
    path = self.sample_path()
    Xp, Yp = X, Y
    for o in path:
      Xp, Yp = o.run(Xp, Yp)
    return Xp, Yp

