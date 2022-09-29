import pandas as pd
import psycopg2
import psycopg2.extras
import funcoes as fn

ls = "-" * 60
sql01 = ""
consulta01 = None

# 1 = Marcio
codigo_usuario = 1
# 2 = nubank   3 = inter
codigo_forma_pagamento = 3 # <---------------------------------------------------- TROCAR
planilha = pd.read_excel("inter-setembro.xlsx").to_dict(orient="records") # <----- TROCAR
conexao = psycopg2.connect(host="127.0.0.1", port="5436", database="simplesvarejo", user="postgres", password="Mpvpr@8@8282@1@RCPNMGPOVP")
cursor = conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# print(planilha)
# print(ls)

for linha in planilha:
    if (linha["Tipo"] != "P" or len(linha["Tipo"]) != 1):
        # print(fn.converte_data_sql(linha["Data"]), linha["Valor"], linha["Tipo"], linha["Descrição"])
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
        cursor.execute(sql01, (fn.converte_data_sql(linha["Data"]), fn.retorna_plano_conta(linha["Tipo"]), 1, linha["Descrição"], linha["Valor"], codigo_usuario))

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
