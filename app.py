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

fn.limpa_tela()

print("Formato da planilha")
print("Data, Tipo, Descrição, Valor")
print("")
print("A = 55 = ALIMENTACAO")
print("F = 49 = FILHAS")
print("T = 51 = TRANSPORTE")
print("R = 54 = REMEDIOS")
print("N = 50 = ANA")
print("O = 52 = OUTRAS")
print("C = 48 = CASA")
print("U = 43 = CASA MATERIAL DE CONSTRUÇÃO")
print("")

codigo_forma_pagamento = inp.inputInt(prompt="Código da forma de pagamento: ", min=2, max=3, blank=True)
caminho_planilha = inp.inputFilename(prompt="Nome da planilha para importar: ", blank=True)

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
        if (linha["Tipo"] != "P" or len(linha["Tipo"]) != 1):
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
