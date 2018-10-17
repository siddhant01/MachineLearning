import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

q=ctrl.Antecedent(np.arange(0,11,1), 'Quality')
s=ctrl.Antecedent(np.arange(0,11,1), 'Service')
t=ctrl.Consequent(np.arange(0,26,1), 'Tip')

q['Low'] = fuzzy.trimf(q.universe, [0,0,5])
q['Medium'] = fuzzy.trimf(q.universe, [0,5,10])
q['High'] = fuzzy.trimf(q.universe, [5,10,10])

s['Low'] = fuzzy.trimf(s.universe, [0,0,5])
s['Medium'] = fuzzy.trimf(s.universe, [0,5,10])
s['High'] = fuzzy.trimf(s.universe, [5,10,10])

t['Low'] = fuzzy.trimf(t.universe, [0,0,12.5])
t['Medium'] = fuzzy.trimf(t.universe, [0,12.5,25])
t['High'] = fuzzy.trimf(t.universe, [12.5,25,25])

r1=ctrl.Rule(q['Low'] | s['Low'], t['Low'])
r2=ctrl.Rule(s['Medium'] , t['Medium'])
r3=ctrl.Rule(s['High'] | q['High'] , t['High'])

t_ctrl=ctrl.ControlSystem([r1,r2,r3])
t_cal=ctrl.ControlSystemSimulation(t_ctrl)

t_cal.input['Quality']=6.5
t_cal.input['Service']=9.5
t_cal.compute()
print(t_cal.output['Tip'])
t.view(sim=t_cal)

