class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = self.root

    while nodes_to_visit:
      current = nodes_to_visit.pop(0)
      if current['id'] == id:
        return current
      
      nodes_to_visit = nodes_to_visit + current['children']

    return None



  def breadth_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      result.append(node['value'])
      nodes_to_visit = nodes_to_visit + node['children']

      return result
    
  def depth_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      result.append(node['value'])
      nodes_to_visit = node['children'] + nodes_to_visit

    return result

child_1 = {
  'value': 2,
  'children': []
}

child_2 = {
  'value': 3,
  'children': []
}

child_3 = {
  'value': 4,
  'children': []
}

root = {
  'value': 1,
  'children': [child_1, child_2, child_3]
}
