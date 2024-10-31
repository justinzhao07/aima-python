import collections, sys, os
from logic import *
from planning import *

############################################################
# Problem: Planning 

# Blocks world modification
def blocksWorldModPlan():
    # BEGIN_YOUR_CODE (make modifications to the initial and goal states)
    initial_state = 'On(A, B) & Clear(A) & OnTable(B) & OnTable(C) & Clear(C)'
    goal_state = 'On(B, A) & On(C, B)'
    # END_YOUR_CODE

    planning_problem = \
    PlanningProblem(initial=initial_state,
                    goals=goal_state,
                    actions=[Action('ToTable(x, y)',
                                    precond='On(x, y) & Clear(x)',
                                    effect='~On(x, y) & Clear(y) & OnTable(x)'),
                             Action('FromTable(y, x)',
                                    precond='OnTable(y) & Clear(y) & Clear(x)',
                                    effect='~OnTable(y) & ~Clear(x) & On(y, x)')])
    
    return linearize(GraphPlan(planning_problem).execute())

def logisticsPlan():
    # BEGIN_YOUR_CODE (use the previous problem as a guide and uncomment the starter code below if you want!)
    # initial_state = 
    # goal_state = 
    # planning_problem = \
    # PlanningProblem(initial=initial_state,
    #                 goals=goal_state,
    #                 actions=[Action('',
    #                                 precond='',
    #                                 effect=''),
    #                          Action('',
    #                                 precond='',
    #                                 effect=''),
    #                          Action('',
    #                                 precond='',
    #                                 effect='')])
    # END_YOUR_CODE

    return linearize(GraphPlan(planning_problem).execute())


a = blocksWorldModPlan()
print(a)
