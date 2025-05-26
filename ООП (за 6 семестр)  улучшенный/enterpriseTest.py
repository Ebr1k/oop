from enterprise import enterprise
test1 = enterprise("Университет", "", 8917214, "Кравцов Н. А.")
test1.setInn(64645)
test1.setOgrn(555555)

print(test1.getContact())