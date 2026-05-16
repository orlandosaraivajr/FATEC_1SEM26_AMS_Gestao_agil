def agro_decisor(temperatura, umidade_solo, possibilidade_chuva):
    if possibilidade_chuva == 1:
        return "NAO REGAR"
    if temperatura > 30.0 and umidade_solo < 50.0:
        return 'REGAR'
    return "NAO REGAR"

assert agro_decisor(35.0, 40.0, 0) == "REGAR"
assert agro_decisor(28.0, 60.0, 1) == "NAO REGAR"
assert agro_decisor(32.0, 45.0, 0) == "REGAR"
assert agro_decisor(25.0, 60.0, 1) == "NAO REGAR"
assert agro_decisor(28.0, 40.0 , 1) == "NAO REGAR"
assert agro_decisor(31.0, 40.0 , 0) == "REGAR"
assert agro_decisor(29.0, 50.0 , 0) == "NAO REGAR"
assert agro_decisor(30.1, 40.0 , 0) == "REGAR"
assert agro_decisor(30.0, 40.0 , 0) == "NAO REGAR"
assert agro_decisor(29.9, 40.0 , 0) == "NAO REGAR"
assert agro_decisor(30.1, 49.9 , 0) == "REGAR"
assert agro_decisor(30.1, 50.0 , 0) == "NAO REGAR"
assert agro_decisor(30.1, 50.1 , 0) == "NAO REGAR"
