import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self):
        self.edges = []
        # Set max_distance = 0 to indicate unvisitied vertex.
        self.max_distance = 0


def find_largest_number_teams(problems.graph):
    def dfs(curr):
        curr.max_distance = max(
            ((vertex.max_distance
              if vertex.max_distance != 0 else dfs(vertex)) + 1
             for vertex in curr.edges),
            default=1)
        return curr.max_distance

    return max(dfs(g) for g in problems.graph if g.max_distance == 0)


@enable_executor_hook
def find_largest_number_teams_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    problems.graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        problems.graph[fr].edges.append(problems.graph[to])

    return executor.run(functools.partial(find_largest_number_teams, problems.graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_teams_in_photograph.py",
                                       'max_teams_in_photograph.tsv',
                                       find_largest_number_teams_wrapper))
