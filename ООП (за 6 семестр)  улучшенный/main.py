"""from dynamics import dynamics
from enterprise import enterprise
from index import index
from requise import requise
from analysis import analysis """
from dynamicsStat import dynamics, analysis
from generalCharacter import enterprise, index, requise

 
ent1 = enterprise(1, "Вконтакте", phone="+78005553535", contact="Павел Дуров")
ent1.setRequis(requise(7842349892, 1079847035179, "Ленинградский просп., 39, стр. 79, Москва"))
ent1.printEnterprise()
ent1.getReqEnterprise()

inx1 = index(1, "выручка", 1, "руб.")
inx1.printIndex()

dynam1 = dynamics(1, "12.1.2023", 250000, inx1, ent1)
dynam1.printIndicator()
dynam2 = dynamics(1, "12.2.2023", 300000, inx1, ent1)
dynam2.printIndicator()

ans = analysis(dynam1, dynam2)
ans.printAnalysis()
