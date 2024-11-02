import collections, sys, os
from logic import *
from planning import *

############################################################
# Problem: Planning 

# Blocks world modification
def blocksWorldModPlan():
    # BEGIN_YOUR_CODE (make modifications to the initial and goal states)
    initial_state = 'On(A, B) & Clear(A) & OnTable(B) & On(C, D) & Clear(C) & OnTable(D)'
    goal_state = 'On(B, A) & On(C, B) & On(D, C)'
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
    initial_state = 'At(R1, D1) & In(C1, R1) & At(C2, D1) & At(C3, D2)'
    # goal_state = 'At(C1, D3) & At(C2, D3) & At(C3, D3)'
    # goal_state = 'At(C1, D2)'
    # goal_state = 'At(C1, D1) & At(R1, D2)'
    goal_state = 'At(C1, D1) & At(R1, D2) & In(C3, R1)'
    # goal_state = 'At(C1, D1)'
    planning_problem = \
    PlanningProblem(initial=initial_state,
                    goals=goal_state,
                    actions=
                    [
                    Action('Move(x, y)',
                        precond='At(R1, x)',
                        effect='~At(R1, x) & At(R1, y)'),
                    Action('Load(c, x)',
                        precond='At(R1, x) & At(c, x) & Clear(R1)',
                        effect='In(c, R1) & ~At(c, x) & ~Clear(R1)'),
                    Action('Unload(c, x)',
                        precond='In(c, R1) & At(R1, x)',
                        effect='At(c, x) & ~In(c, R1) & Clear(R1)')
                    ])
    # END_YOUR_CODE

    solution = GraphPlan(planning_problem).execute()
    
    if solution is None:
        print("No solution found by GraphPlan.")
        return None
    
    return linearize(solution)

def logisticsPlanWithTime():
    initial_state = 'At(R1, D1) & In(C1, R1) & At(C2, D1) & At(C3, D2)'
    # goal_state = 'At(C1, D3) & At(C2, D3) & At(C3, D3)'
    # goal_state = 'At(C1, D2)'
    # goal_state = 'At(C1, D1) & At(R1, D2)'
    # goal_state = 'At(C1, D1) & At(R1, D2) & In(C3, R1)'
    goal_state = 'At(C1, D1)'
    planning_problem = \
    PlanningProblem(initial=initial_state,
                    goals=goal_state,
                    actions=
                    [
                    Action('Move(D1, D2)',
                        precond='At(R1, D1) & Time(t)',
                        effect='~At(R1, D1) & At(R1, D2)'),
                    Action('Move(D2, D1)',
                        precond='At(R1, D2)',
                        effect='~At(R1, D2) & At(R1, D1)'),
                    Action('Move(D2, D3)',
                        precond='At(R1, D2)',
                        effect='~At(R1, D2) & At(R1, D3)'),
                    Action('Move(D3, D2)',
                        precond='At(R1, D3)',
                        effect='~At(R1, D3) & At(R1, D2)'),
                    Action('Move(D1, D3)',
                        precond='At(R1, D1)',
                        effect='~At(R1, D1) & At(R1, D3)'),
                    Action('Move(D3, D1)',
                        precond='At(R1, D3)',
                        effect='~At(R1, D3) & At(R1, D1)'),
                    Action('Load(c, x)',
                        precond='At(R1, x) & At(c, x) & Clear(R1)',
                        effect='In(c, R1) & ~At(c, x) & ~Clear(R1)'),
                    Action('Unload(c, x)',
                        precond='In(c, R1) & At(R1, x)',
                        effect='At(c, x) & ~In(c, R1) & Clear(R1)')
                    ])
    # END_YOUR_CODE

    solution = GraphPlan(planning_problem).execute()
    
    if solution is None:
        return ([], 0)
    
    # Get the linearized plan
    plan = linearize(solution)
    
    s = str(plan)
    total_time = 0
    move12 = s.count('Move(D1, D2)')
    move21 = s.count('Move(D2, D1)')
    move23 = s.count('Move(D2, D3)')
    move32 = s.count('Move(D3, D2)')
    move13 = s.count('Move(D1, D3)')
    move31 = s.count('Move(D3, D1)')
    l = s.count('Load')
    unl = s.count('Unload')
    total_time = 1 * l + 1 * unl + 3 * (move12 + move21) + 5 * (move23 + move32) + 10 * (move13 + move31)
    return (plan, total_time)

if __name__ == "__main__":
    blocks_solution = blocksWorldModPlan()
    print("Blocks World Solution:", blocks_solution)
    
    logistics_solution = logisticsPlan()
    print(f"Logistics Solution:", logistics_solution)
    
    timed_solution, time = logisticsPlanWithTime()
    print("Timed Logistics Solution:", timed_solution)
    print("Time:", time)
