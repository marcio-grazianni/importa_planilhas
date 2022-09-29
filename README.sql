
data
usuario - usar o código 1
plano de contas *
complemento
valor
301


CREATE TABLE public.lancamento_tesouraria (
  numero_controle SERIAL,
  data DATE DEFAULT 'now'::text::date NOT NULL,
  hora TIMESTAMP(0) WITHOUT TIME ZONE DEFAULT now() NOT NULL,
  codigo_plano_conta_tesouraria INTEGER,
  codigo_historico INTEGER NOT NULL,
  complemento TEXT,
  valor NUMERIC(18,2) NOT NULL,
  origem INTEGER DEFAULT 1 NOT NULL,
  codigo_usuario INTEGER NOT NULL,
  data_cadastro TIMESTAMP(0) WITHOUT TIME ZONE DEFAULT now() NOT NULL,
  CONSTRAINT pk_lancamento_tes_numctl PRIMARY KEY(numero_controle),
  CONSTRAINT ck_lancamento_tes_vallan CHECK (valor > (0)::numeric),
  CONSTRAINT fk_lancamento_tes_codhis FOREIGN KEY (codigo_historico) REFERENCES public.historico(codigo),
  CONSTRAINT fk_lancamento_tes_codusu FOREIGN KEY (codigo_usuario) REFERENCES maker.fr_usuario(usr_codigo),
  CONSTRAINT fk_lancamento_tes_placon FOREIGN KEY (codigo_plano_conta_tesouraria) REFERENCES public.plano_conta_tesouraria(codigo)
);

CREATE TABLE public.lancamento_tesouraria_composicao (
  numero_controle INTEGER NOT NULL,
  numero_ordem_composicao INTEGER NOT NULL,
  codigo_forma_pagamento INTEGER NOT NULL,
  valor NUMERIC(18,2) NOT NULL,
  codigo_usuario INTEGER NOT NULL,
  data_cadastro TIMESTAMP(0) WITHOUT TIME ZONE DEFAULT now() NOT NULL,
  CONSTRAINT pk_lancamento_tes_comp_ctlfor PRIMARY KEY(numero_controle, numero_ordem_composicao),
  CONSTRAINT ck_lancamento_tes_comp_vallan CHECK (valor > (0)::numeric),
  CONSTRAINT fk_lancamento_tes_comp_codfor FOREIGN KEY (codigo_forma_pagamento) REFERENCES public.forma_pagamento(codigo),
  CONSTRAINT fk_lancamento_tes_comp_codusu FOREIGN KEY (codigo_usuario) REFERENCES maker.fr_usuario(usr_codigo),
  CONSTRAINT fk_lancamento_tes_comp_numctl FOREIGN KEY (numero_controle) REFERENCES public.lancamento_tesouraria(numero_controle)
);
