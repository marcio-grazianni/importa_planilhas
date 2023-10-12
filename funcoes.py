import platform
import os


def retorna_os():
    return platform.system().upper()


def limpa_tela():
    if retorna_os() == "WINDOWS":
        os.system("cls")
    else:
        os.system("clear")


def converte_data_sql(data: str):
    # 19/09/2022
    retorno = data[6:10] + "-" + data[3:5] + "-" + data[0:2]

    return retorno


def retorna_plano_conta(texto: str):
    # A = 55 = ALIMENTACAO
    # F = 49 = FILHAS
    # T = 51 = TRANSPORTE
    # R = 54 = REMEDIOS
    # N = 44 = ANA
    # O = 52 = OUTRAS
    # C = 48 = CASA
    # U = 43 = CASA MATERIAL DE CONSTRUÇÃO

    retorno = None
    if (texto.upper() == "A"):
        retorno = 55
    elif (texto.upper() == "F"):
        retorno = 49
    elif (texto.upper() == "T"):
        retorno = 51
    elif (texto.upper() == "R"):
        retorno = 54
    elif (texto.upper() == "N"):
        retorno = 44
    elif (texto.upper() == "O"):
        retorno = 52
    elif (texto.upper() == "C"):
        retorno = 48
    elif (texto.upper() == "U"):
        retorno = 43
    elif (texto.upper() == "P1"):
        retorno = 64
    elif (texto.upper() == "P2"):
        retorno = 35
    elif (texto.upper() == "P3"):
        retorno = 36
    elif (texto.upper() == "P4"):
        retorno = 37
    elif (texto.upper() == "P5"):
        retorno = 38
    elif (texto.upper() == "P6"):
        retorno = 42
    elif (texto.upper() == "P7"):
        retorno = 32
    elif (texto.upper() == "P8"):
        retorno = 46
    elif (texto.upper() == "P9"):
        retorno = 41
    elif (texto.upper() == "P10"):
        retorno = 47
    elif (texto.upper() == "P11"):
        retorno = 62
    elif (texto.upper() == "P12"):
        retorno = 58
    elif (texto.upper() == "P13"):
        retorno = 65
    elif (texto.upper() == "P14"):
        retorno = 63
    elif (texto.upper() == "P15"):
        retorno = 44
    elif (texto.upper() == "P16"):
        retorno = 66
    elif (texto.upper() == "P17"):
        retorno = 67

    return retorno
