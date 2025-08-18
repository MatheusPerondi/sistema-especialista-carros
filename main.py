# -----------------------------
# Base de conhecimento
# -----------------------------

perguntas = {
    "bateria": {
        "opcoes": {
            "descarregada": "A bateria está descarregada?",
            "ok": "A bateria está funcionando corretamente?"
        }
    },
    "carro_nao_liga": {
        "pergunta": "O carro não liga?"
    },
    "luz_painel": {
        "pergunta": "A luz do painel está acesa?"
    }
}

regras = [
    {
        "condicoes": ["bateria_descarregada", "carro_nao_liga"],
        "conclusao": "Problema na bateria"
    },
    {
        "condicoes": ["luz_painel"],
        "conclusao": "Verificar sistema elétrico"
    }
]

# -----------------------------
# Probabilidades para Rede Bayesiana completa
# -----------------------------
# Agora cada hipótese tem P(H) e P(E|H) para todos os sintomas
# Isso permite calcular a probabilidade posterior completa
hipoteses = {
    "Problema na bateria": {
        "P(H)": 0.3,
        "P(carro_nao_liga|H)": 0.9,
        "P(luz_painel|H)": 0.2,
        "P(bateria_descarregada|H)": 0.95
    },
    "Verificar sistema elétrico": {
        "P(H)": 0.2,
        "P(carro_nao_liga|H)": 0.5,
        "P(luz_painel|H)": 0.8,
        "P(bateria_descarregada|H)": 0.1
    }
}

# -----------------------------
# Funções utilitárias
# -----------------------------
def perguntar(texto):
    resposta = input(texto + " (s/n): ").strip().lower()
    while resposta not in ("s", "n"):
        resposta = input("Resposta inválida! Digite 's' ou 'n': ").strip().lower()
    return resposta == "s"

# -----------------------------
# Coleta de fatos (Forward)
# -----------------------------
def coletar_fatos(perguntas):
    fatos_positivos = set()
    fatos_negativos = set()
    perguntas_restantes = perguntas.copy()

    while perguntas_restantes:
        nova_rodada = False
        remover_chaves = []

        for chave, dados in perguntas_restantes.items():
            if "opcoes" not in dados:
                if chave not in fatos_positivos and chave not in fatos_negativos:
                    resposta = perguntar(dados["pergunta"])
                    if resposta:
                        fatos_positivos.add(chave)
                    else:
                        fatos_negativos.add(chave)
                    remover_chaves.append(chave)
                    nova_rodada = True
                    break
            else:
                for sub_chave, texto_pergunta in dados["opcoes"].items():
                    chave_completa = f"{chave}_{sub_chave}"
                    if chave_completa not in fatos_positivos and chave_completa not in fatos_negativos:
                        resposta = perguntar(texto_pergunta)
                        if resposta:
                            fatos_positivos.add(chave_completa)
                        else:
                            fatos_negativos.add(chave_completa)
                        remover_chaves.append(chave)
                        nova_rodada = True
                        break
                if nova_rodada:
                    break

        for chave in remover_chaves:
            perguntas_restantes.pop(chave, None)

        if not nova_rodada:
            break

    return fatos_positivos, fatos_negativos

# -----------------------------
# Motor de Inferência (Forward)
# -----------------------------
def motor_inferencia(fatos):
    conclusoes = []
    explicacoes = []
    for regra in regras:
        if all(cond in fatos for cond in regra["condicoes"]):
            conclusoes.append(regra["conclusao"])
            explicacoes.append(f"Porque foram observados: {', '.join(regra['condicoes'])}")
    return conclusoes, explicacoes

# -----------------------------
# Backward Chaining
# -----------------------------
def backward_chaining(hipotese, fatos_pos, fatos_neg, regras):
    for regra in regras:
        if regra["conclusao"] == hipotese:
            faltando = [cond for cond in regra["condicoes"] if cond not in fatos_pos and cond not in fatos_neg]
            if not faltando:
                return all(cond in fatos_pos for cond in regra["condicoes"])
            for cond in faltando:
                resposta = perguntar(f"É verdade que {cond}?")
                if resposta:
                    fatos_pos.add(cond)
                else:
                    fatos_neg.add(cond)
                    return False
            return backward_chaining(hipotese, fatos_pos, fatos_neg, regras)
    return False

# -----------------------------
# Rede Bayesiana completa
# -----------------------------
def rede_bayesiana(hipoteses, fatos_positivos, fatos_negativos):
    resultados = {}
    for h, dados in hipoteses.items():
        p_h = dados["P(H)"]
        prob = p_h
        for sintoma in fatos_positivos:
            key = f"P({sintoma}|H)"
            if key in dados:
                prob *= dados[key] # multiplica probabilidade do sintoma positivo
        for sintoma in fatos_negativos:
            key = f"P({sintoma}|H)"
            if key in dados:
                prob *= (1 - dados[key]) # multiplica probabilidade de sintoma negativo
        resultados[h] = prob

    # normaliza para somar 1
    soma = sum(resultados.values())
    if soma > 0:
        for h in resultados:
            resultados[h] /= soma

    return resultados

# -----------------------------
# Execução Híbrida com Rede Bayesiana Completa
# -----------------------------
print(">>> SISTEMA ESPECIALISTA - DIAGNÓSTICO AUTOMOTIVO (Rede Bayesiana Completa) <<<\n")

# 1. Coleta de fatos via Forward Chaining
fatos_pos, fatos_neg = coletar_fatos(perguntas)

# 2. Conclusões via Forward Chaining
conclusoes, explicacoes = motor_inferencia(fatos_pos)

# 3. Backward Chaining
for hipotese in [r["conclusao"] for r in regras]:
    if backward_chaining(hipotese, fatos_pos, fatos_neg, regras):
        if hipotese not in conclusoes:
            conclusoes.append(hipotese)
            explicacoes.append(f"Hipótese '{hipotese}' confirmada via backward chaining.")

# 4. Probabilidades via Rede Bayesiana completa
probabilidades = rede_bayesiana(hipoteses, fatos_pos, fatos_neg)

# -----------------------------
# Resultados
# -----------------------------
if conclusoes:
    print("\nPossíveis conclusões:")
    for c, e in zip(conclusoes, explicacoes):
        print(f"- {c} ({e})")
else:
    print("\nNenhuma conclusão encontrada.")

print("\nProbabilidades Bayesianas (grau de certeza):")
for h, p in probabilidades.items():
    print(f"- {h}: {p:.2%}")
