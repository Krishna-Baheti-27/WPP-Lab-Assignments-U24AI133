import pandas as pd

dt_a = pd.to_datetime("2012-01-15")
print("a)", dt_a)

dt_b = pd.to_datetime("2012-01-15 21:20")
print("b)", dt_b)

dt_c = pd.to_datetime("now")
print("c)", dt_c)

dt_d = dt_c.date()
print("d)", dt_d)

dt_e = pd.to_datetime("today").date()
print("e)", dt_e)

dt_f = dt_c.time()
print("f)", dt_f)

dt_g = pd.to_datetime("now").time()
print("g)", dt_g)



