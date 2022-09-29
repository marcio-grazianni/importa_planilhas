def converte_data_sql(data: str):
    # 19/09/2022
    retorno = data[6:10] + "-" + data[3:5] + "-" + data[0:2]

    return retorno


def retorna_plano_conta(texto: str):
    # A = 55 = ALIMENTACAO
    # F = 49 = FILHAS
    # T = 51 = TRANSPORTE
    # R = 54 = REMEDIOS
    retorno = 0
    if (texto.upper() == "A"):
        retorno = 55
    elif (texto.upper() == "F"):
        retorno = 49
    elif (texto.upper() == "T"):
        retorno = 51
    elif (texto.upper() == "R"):
        retorno = 54

    return retorno