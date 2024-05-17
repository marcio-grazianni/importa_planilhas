# Formato da planilha
# Data, Tipo, Descrição, Valor

import pandas as pd
import psycopg2
import psycopg2.extras
import funcoes as fn
import pyinputplus as inp
from pathlib import Path

codigo_forma_pagamento: str = "2"
texto2: str = "nubank.xlsx"
quantidade_importacoes: int = 0
linha_separadora: str = "-" * 90

fn.limpa_tela()

print("Formato da planilha")
print("Data, Valor, Tipo, Descrição")
print("")
print("A = 55 = ALIMENTACAO")
print("F = 49 = FILHAS")
print("T = 51 = TRANSPORTE")
print("R = 54 = REMEDIOS")
print("N = 44 = ANA")
print("O = 52 = OUTRAS")
print("C = 48 = CASA")
print("U = 43 = CASA MATERIAL DE CONSTRUÇÃO")
print("P1 = 64 = JUCIARA LIMPEZA")
print("P2 = 35 = CLARO")
# print("P3 = 36 = NETFLIX")
print("P4 = 37 = DISNEY+")
print("P5 = 38 = COELBA")
print("P6 = 42 = SEGURO DE VIDA FILHAS")
print("P7 = 32 = ESCOLA LILIAN")
# print("P8 = 46 = PLANO DE SAUDE FILHAS")
print("P9 = 41 = INTERNET")
print("P10 = 47 = ALIMENTACAO DAS FILHAS")
print("P11 = 62 = ALUGUEL")
print("P12 = 58 = AMAZON PRIME (BRADESCO)")
print("P13 = 65 = HIGIENE PESSOAL")
# print("P14 = 63 = PLANOS DE SAUDE LUCAS")
# print("P15 = 44 = AJUDA DE CUSTO A ANA")
print("P16 = 66 = GAS")
# print("P17 = 67 = AMAZON KINDLE UNLIMITED")
print("P18 = 70 = COMBUSTÍVEL")
print("P19 = 71 = FILHA LÍLIAN")
print("P20 = 72 = FILHA LETÍCIA")
print("P21 = 73 = FILHA LAURA")
print("P22 = 68 = ROUPAS")
print("P23 = 69 = CALÇADOS")
print("")

codigo_forma_pagamento = inp.inputInt(prompt="Código da forma de pagamento: ", min=2, max=3, blank=True)
caminho_planilha = inp.inputFilename(prompt="Nome da planilha para importar: ", blank=True)
# codigo_forma_pagamento = 2
# caminho_planilha = "./nubank.xlsx"
print(linha_separadora)

if ((codigo_forma_pagamento == "" and caminho_planilha == "") or not Path(caminho_planilha).is_file()):
    print("Dados inválidos.")
else:
    ls = "-" * 60
    sql01 = ""
    consulta01 = None

    # 1 = Marcio
    codigo_usuario = 1
    # 2 = nubank   3 = inter
    planilha = pd.read_excel(caminho_planilha).to_dict(orient="records")
    conexao = psycopg2.connect(host="127.0.0.1", port="5436", database="simplesvarejo", user="postgres", password="Mpvpr@8@8282@1@RCPNMGPOVP")
    cursor = conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    for linha in planilha:
        # if (linha["Tipo"] != "P" or len(linha["Tipo"]) != 1):
        if (linha["Tipo"] != "P"):
            sql01 = """
                INSERT INTO
                    lancamento_tesouraria
                (
                    data, codigo_plano_conta_tesouraria, codigo_historico,
                    complemento, valor, codigo_usuario
                )
                VALUES
                (
                    %s, %s, %s, %s, %s, %s
                );
            """
            cursor.execute(sql01, (fn.converte_data_sql(linha["Data"]), fn.retorna_plano_conta(linha["Tipo"]), 1, linha["Descrição"].encode('latin-1','ignore').decode("latin-1"), linha["Valor"], codigo_usuario))
            quantidade_importacoes = quantidade_importacoes + 1
            print(linha["Data"], "|", fn.retorna_plano_conta(linha["Tipo"]), "|", linha["Tipo"], "|", linha["Valor"], "|", linha["Descrição"].encode('latin-1','ignore').decode("latin-1"))
            print(linha_separadora)

            sql01 = "SELECT max(numero_controle) as ultimo FROM lancamento_tesouraria;"
            cursor.execute(sql01)
            consulta01 = cursor.fetchone()
            numero_controle = consulta01["ultimo"]

            sql01 = """
                INSERT INTO
                    lancamento_tesouraria_composicao
                (
                    numero_controle, numero_ordem_composicao, codigo_forma_pagamento,
                    valor, codigo_usuario
                )
                VALUES
                (
                    %s, %s, %s, %s, %s
                );
            """
            cursor.execute(sql01, (numero_controle, 1, codigo_forma_pagamento, linha["Valor"], codigo_usuario))

    conexao.commit()

    cursor.close()
    conexao.close()
    print("Quantidade de importações:", quantidade_importacoes)
