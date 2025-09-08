
# Define um dicionario, cada chave é um topico exemplo "bateria, carro_nao_liga"
# Se existir "opções", o tópico tem subperguntas: "descarregada", "ok".
# Se não houver opções a pergunta é direta

#perguntas é um dicionário em Python.

#cada chave (ex.: "bateria", "carro_nao_liga", "tanque") representa um sintoma ou componente do carro.
#O valor associado a cada chave pode ser:
#Outro dicionário com "opcoes" → quando existem diferentes alternativas para a mesma pergunta (ex.: bateria pode estar descarregada ou ok).
#Um dicionário com "pergunta" → quando a pergunta é direta (ex.: "O carro não liga?").

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
    },
    "tanque": {
        "opcoes": {
            "vazio": "O tanque está vazio?",
            "ok": "O tanque tem combustível suficiente?"
        }
    },
    "alternador": {
        "opcoes": {
            "barulho": "O alternador faz algum barulho estranho?",
            "ok": "O alternador funciona normalmente?"
        }
    },
    "fusivel": {
        "opcoes": {
            "queimado": "Algum fusível queimou recentemente?",
            "ok": "Todos os fusíveis estão intactos?"
        }
    },
    "motor_partida": {
        "opcoes": {
            "lento": "O motor de partida gira lentamente?",
            "ok": "O motor de partida funciona normalmente?"
        }
    },
    "velas": {
        "opcoes": {
            "suja": "As velas de ignição estão sujas ou desgastadas?",
            "ok": "As velas estão em bom estado?"
        }
    },
    "bomba_combustivel": {
        "opcoes": {
            "falha": "A bomba esta com problema?",
        }
    },
    "filtro_ar": {
        "opcoes": {
            "sujo": "O filtro de ar está sujo?",
            "limpo": "O filtro de ar está limpo?"
        }
    },
    "ignicao": {
        "opcoes": {
            "falha": "Há falha na ignição ao ligar?",
        }
    },
    "cabos_bateria": {
        "opcoes": {
            "oxidados": "Os cabos da bateria estão oxidados ou soltos?",
        }
    },
    "sensor_motor": {
        "opcoes": {
            "alerta": "Há alguma luz de alerta do motor acesa?",
        }
    }
}

# -----------------------------
# Regras ampliadas
# -----------------------------

# Define regras
# "condições" fatos que devem ser verdadeiros para que a regra se aplique.
# Ex: se a bateria_descarregada e carro_nao_liga forem verdadeiros a conclusao sera problema na bateria.

#regras é uma lista de dicionários em Python.
#cada elemento da lista é uma regra representada por um dicionário.
#Dentro de cada regra:
#"condicoes" → é uma lista de sintomas ou evidências necessárias.
#"conclusao" → é a hipótese ou diagnóstico associado quando as condições são satisfeitas.
regras = [
    {"condicoes": ["bateria_descarregada", "carro_nao_liga"], "conclusao": "Problema na bateria"},
    {"condicoes": ["luz_painel"], "conclusao": "Verificar sistema elétrico"},
    {"condicoes": ["alternador_barulho"], "conclusao": "Problema no alternador"},
    {"condicoes": ["fusivel_queimado"], "conclusao": "Fusível queimado"},
    {"condicoes": ["tanque_vazio"], "conclusao": "Tanque vazio"},
    {"condicoes": ["motor_partida_lento"], "conclusao": "Motor de partida fraco"},
    {"condicoes": ["velas_suja"], "conclusao": "Velas de ignição em mau estado"},
    {"condicoes": ["bomba_combustivel_falha"], "conclusao": "Problema na bomba de combustível"},
    {"condicoes": ["ignicao_falha"], "conclusao": "Problema no sistema de ignição"},
    {"condicoes": ["cabos_bateria_oxidados"], "conclusao": "Cabos da bateria danificados"},
    {"condicoes": ["filtro_ar_sujo"], "conclusao": "Filtro de ar sujo"},
    {"condicoes": ["sensor_motor_alerta"], "conclusao": "Sensor do motor indicando falha"}
]

# -----------------------------
# Hipóteses ampliadas
# -----------------------------

# Hipoteses define probabilidades para a Rede Bayesiana.
# P(H) = probabilidade inicial da hipótese
# P(E|H) = probabilidade da evidência acontecer dado a hipótese
#
# Para cada hipotese H (uma possivel causa do defeito)
# P(H) → é a chance inicial de cada hipótese acontecer, antes de olhar os sintomas.
#
# P(carro_nao_liga | H) quão provável é observar o sintoma "carro não liga" se a hipotese for verdade
# EX: se o problema for a bateria, a chance de o carro não ligar é 0,9
# é a chance do sintoma aparecer se aquela hipótese for verdadeira.

# P(luz_painel|H) → mesma ideia, mas para outro sintoma.
# Ex: se o problema for a bateria, a luz do painel quase nunca fica acesa (só em 20% dos casos).

#hipoteses é um dicionário em Python.
#As chaves são as hipóteses (ex.: "Problema na bateria", "Verificar sistema elétrico").
#Os valores são outros dicionários, que guardam as probabilidades associadas a cada hipótese (probabilidade a priori e as condicionais).
#Ou seja, é um dicionário de dicionários.

hipoteses = {
    "Problema na bateria": {"P(H)": 0.3, "P(carro_nao_liga|H)": 0.9, "P(luz_painel|H)": 0.2, "P(bateria_descarregada|H)": 0.95},
    "Verificar sistema elétrico": {"P(H)": 0.2, "P(carro_nao_liga|H)": 0.5, "P(luz_painel|H)": 0.8, "P(bateria_descarregada|H)": 0.1},
    "Problema no alternador": {"P(H)": 0.1, "P(alternador_barulho|H)": 0.9},
    "Fusível queimado": {"P(H)": 0.05, "P(fusivel_queimado|H)": 0.95},
    "Tanque vazio": {"P(H)": 0.05, "P(tanque_vazio|H)": 0.9},
    "Motor de partida fraco": {"P(H)": 0.05, "P(motor_partida_lento|H)": 0.95},
    "Velas de ignição em mau estado": {"P(H)": 0.05, "P(velas_suja|H)": 0.95},
    "Problema na bomba de combustível": {"P(H)": 0.05, "P(bomba_combustivel_falha|H)": 0.95},
    "Problema no sistema de ignição": {"P(H)": 0.05, "P(ignicao_falha|H)": 0.95},
    "Cabos da bateria danificados": {"P(H)": 0.05, "P(cabos_bateria_oxidados|H)": 0.95},
    "Filtro de ar sujo": {"P(H)": 0.05, "P(filtro_ar_sujo|H)": 0.95},
    "Sensor do motor indicando falha": {"P(H)": 0.05, "P(sensor_motor_alerta|H)": 0.95}
}

# -----------------------------
# Funções utilitárias
# -----------------------------
def perguntar(texto):
    # pega a resposta do usuario, strip remove espaços extras
    # lower deixa tudo em minusculo
    resposta = input(texto + " (s/n): ").strip().lower()
    #fazemos um loop, caso a resposta do usuario não for "s" ou "n" faz a pergunta novamente
    while resposta not in ("s", "n"):
        resposta = input("Resposta inválida! Digite 's' ou 'n': ").strip().lower()
    return resposta == "s"

# -----------------------------
# Coleta de fatos (Forward)
# -----------------------------
 #Coleta os fatos a partir das perguntas feitas
# Recebe como entrada um dicionario, vai devolver dois conuntos, fatos posisivos e negativos
def coletar_fatos(perguntas):
    fatos_positivos = set() # guarda os sintomas que o usuario desse que acontecem
    fatos_negativos = set() # guarda os sintomas que o usuario desse que nao
    perguntas_restantes = perguntas.copy()  # copia do dicionario para não perder as perguntas originais.

    # loop, enquanto gouver perguntas_restantes o programa continua
    while perguntas_restantes:
        nova_rodada = False 
        remover_chaves = [] # guarda quais perguntas foram respondidas para tirar da listsa

        #fazemos um loop nas perguntas restantes, verificamos a chave e os dados.
	    #chave é por exemplo bateria, e os dados é o que esta dentro de bateria                	
        #por exemplo opcoes.
        for chave, dados in perguntas_restantes.items(): #.items() retorna pares chave-valor do dicionário, em forma de tuplas.
            if "opcoes" not in dados:  #se o dado da chave não for opções significa que é uma pergunta direta
                
                # aqui verificamos se a chave ja foi adicionada a alguma dessas listas, se ja significa que a pergunta ja foi feita
                if chave not in fatos_positivos and chave not in fatos_negativos:
                    resposta = perguntar(dados["pergunta"]) # pergunta ao usuario. 
                    if resposta: # se resposta for true
                        fatos_positivos.add(chave) # se a resposta for positiva adiciona a fatos_positivos
                    else: # se não
                        fatos_negativos.add(chave) # se nao adiciona a fatos_negativos
                    remover_chaves.append(chave) # e por fim adicionamos a chave a lista remover_chaves
                    nova_rodada = True
                    break
            else: # se opções estiver em dados
                #fazemos um loop para verificar a subchave dentro de opções e o valor da chave que seria o texto da pergunta
                for sub_chave, texto_pergunta in dados["opcoes"].items():
                    chave_completa = f"{chave}_{sub_chave}" # pegamos a chave e concatenamos a sub_chave
                    if chave_completa not in fatos_positivos and chave_completa not in fatos_negativos: # verificamos novamente se a pergunta ja foi feita
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

        # Percorre todas as chaves das perguntas que já foram respondidas nesta rodada.
        for chave in remover_chaves:
            perguntas_restantes.pop(chave, None) #pop remove um item de um dicionário a partir da chave.
            #Aqui estamos removendo a pergunta já respondida do dicionário perguntas_restantes.

        if not nova_rodada:
            break

    return fatos_positivos, fatos_negativos # Entrega os conjuntos com as respostas: o que o usuário confirmou e o que ele negou.

# -----------------------------
#Um motor de inferência é o mecanismo de raciocínio de um sistema especialista.
#Ele usa uma base de fatos (o que já se sabe) e uma base de regras (SE... ENTÃO...) para aplicar lógica e chegar a novas conclusões automaticamente.

# Motor de Inferência (Forward) 
#O forward chaining (encadeamento progressivo) é uma forma de raciocínio usada por motores de inferência.
#Ele começa dos fatos conhecidos (“o paciente tem febre e tosse”).
#Depois, aplica as regras passo a passo para gerar novos fatos.
#Continua até chegar a uma conclusão ou até não haver mais regras aplicáveis.
# -----------------------------

# Um motor de inferência é o componente de um sistema 
# especialista que usa regras e fatos para tirar conclusões automaticamente. 
# Ele funciona como o “raciocínio” do sistema, aplicando regras lógicas para analisar 
# informações conhecidas e chegar a novas deduções ou decisões.
def motor_inferencia(fatos):
    conclusoes = [] #irá armazenar todas as hipóteses que o motor de inferência consegue deduzir.
    explicacoes = [] #irá armazenar uma explicação para cada conclusão, mostrando os fatos que levaram a ela.
    
    # Percorre todas as regras definidas na base de conhecimento (regras).
    # Cada regra é um dicionário com:
        #"condicoes" → lista de fatos necessários para a regra se aplicar.
        #"conclusao" → a hipótese que é confirmada se todas as condições forem verdadeiras.
    for regra in regras:
        
        # Verifica se todas as condições da regra estão nos fatos positivos:

        # all(cond in fatos for cond in regra["condicoes"]) → retorna True se cada condição da regra estiver presente em fatos.

        # Se a condição for verdadeira, significa que a regra pode ser aplicada.
        if all(cond in fatos for cond in regra["condicoes"]):
            conclusoes.append(regra["conclusao"]) # Adiciona a conclusão da regra à lista conclusoes.
            explicacoes.append(f"Porque foram observados: {', '.join(regra['condicoes'])}") # Cria uma explicação legível dizendo por que a conclusão foi tomada. ', '.join(regra['condicoes']) → transforma a lista de condições em uma string separada por vírgulas.
    return conclusoes, explicacoes

# -----------------------------
# Backward Chaining
#O backward chaining (encadeamento regressivo) é uma forma de raciocínio usada por motores de inferência.
#Ele começa de uma meta/hipótese (“será que o paciente tem gripe?”).
#Depois, volta para trás verificando se os fatos conhecidos e as regras sustentam essa hipótese.
#Se as condições não forem satisfeitas, a hipótese é descartada.
# -----------------------------
def backward_chaining(hipotese, fatos_pos, fatos_neg, regras):
    for regra in regras: # percorre todas as regras
        if regra["conclusao"] == hipotese: # verificamos se a regra é relevante para a hipotese. Em outras palavras, encontramos a regra relevante que poderia explicar o problema que estamos investigando.
            faltando = [cond for cond in regra["condicoes"] if cond not in fatos_pos and cond not in fatos_neg] # lista que vai armazenar as condições da regra que ainda nao foram respondidas
            #cond cada elemento da lista de condições da regra["condições"]
            #for cond in regra["condicoes"] percorre cada condição da regra.
            #Exemplo: se regra["condicoes"] = ["bateria_descarregada", "carro_nao_liga"], então cond vai valer "bateria_descarregada" na primeira iteração e "carro_nao_liga" na segunda.
            #if cond not in fatos_pos and cond not in fatos_neg, cond not in fatos_pos verifica se essa condição não foi marcada como verdadeira.
            # cond not in fatos_neg verifica se essa condição não foi marcada como falsa.
            # and → garante que a condição só entra na lista se não estiver nem em positivos nem em negativos.
            if not faltando: # se o elemento nao estiver em faltando
                return all(cond in fatos_pos for cond in regra["condicoes"]) # verifica se a condição que esta em fatos_pos ja foi confirmada como verdadeira. Essa linha verifica se todas as condições da regra estão presentes nos fatos positivos. Se todas as condições estiverem em fatos_pos → retorna True. Se faltar alguma condição → retorna False.
            # faz um loop nas condições da regra para verificar se a condicao do fatos pos foi confirmada
            for cond in faltando: # pega o elemento que esta na lista faltando e pergunta. 
                resposta = perguntar(f"É verdade que {cond}?")
                if resposta:
                    fatos_pos.add(cond)
                else:
                    fatos_neg.add(cond)
                    return False
            return backward_chaining(hipotese, fatos_pos, fatos_neg, regras) #Chama a função de novo para verificar a hipótese após atualizar os fatos; continua perguntando até confirmar ou rejeitar a hipótese.
    return False

# -----------------------------
# Rede Bayesiana completa
#Uma Rede Bayesiana é como um mapa de probabilidades que mostra como eventos estão relacionados.
#Ela ajuda a calcular a chance de algo acontecer mesmo com informações incompletas ou incertas.
# -----------------------------

#Uma rede bayesiana é um modelo probabilístico que representa variáveis e as relações de dependência 
# entre elas por meio de um grafo. Ela funciona calculando probabilidades condicionais: 
# dado um conjunto de evidências (fatos conhecidos), a rede atualiza as chances de diferentes hipóteses serem verdadeiras, ]
# ajudando na tomada de decisões sob incerteza.
def rede_bayesiana(hipoteses, fatos_positivos, fatos_negativos):
    resultados = {}  # dicionário que irá armazenar as probabilidades calculadas para cada hipótese

    # Percorre cada hipótese e seus dados na rede bayesiana
    for h, dados in hipoteses.items():
        # P(H) é a probabilidade a priori da hipótese (antes de observar os sintomas)
        p_h = dados["P(H)"]
        # Começa a probabilidade acumulada como a priori
        prob = p_h

        # Ajusta a probabilidade com os sintomas positivos observados
        for sintoma in fatos_positivos:
            key = f"P({sintoma}|H)"  # cria a chave para acessar P(sintoma|hipótese)
            if key in dados:  # verifica se a hipótese tem probabilidade definida para esse sintoma
                prob *= dados[key]  # multiplica a probabilidade acumulada pela probabilidade do sintoma positivo

        # Ajusta a probabilidade com os sintomas negativos observados
        for sintoma in fatos_negativos:
            key = f"P({sintoma}|H)"  # cria a chave para acessar P(sintoma|hipótese)
            if key in dados:  # verifica se a hipótese tem probabilidade definida para esse sintoma
                prob *= (1 - dados[key])  # multiplica pelo complemento (1 - P) para sintomas ausentes

        # Armazena a probabilidade calculada para essa hipótese
        resultados[h] = prob

    # Normaliza todas as probabilidades para que somem 1
    soma = sum(resultados.values())
    if soma > 0:
        for h in resultados:
            resultados[h] /= soma  # divide cada probabilidade pela soma total para obter distribuição válida

    # Retorna o dicionário com hipóteses e suas probabilidades normalizadas
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
# Seleciona o problema mais provável
# -----------------------------
if probabilidades:
    hipotese_principal = max(probabilidades, key=probabilidades.get)
    certeza = probabilidades[hipotese_principal]
    print(f"\nProblema mais provável: {hipotese_principal} ({certeza:.2%})")
else:
    print("Nenhum problema identificado.")

# -----------------------------
# Opcional: Mostrar relatório completo
# -----------------------------
# print("\n=== Todas as hipóteses com suas probabilidades ===")
# for h, p in sorted(probabilidades.items(), key=lambda x: -x[1]):
#     print(f"- {h}: {p:.2%}")
