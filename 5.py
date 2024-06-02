# Entrada do usuário
prompt_usuario = input()

# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt):
    # Verifica se o prompt contém palavras-chave relevantes
    palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia" ]
    
    # TODO: Aplique a condição necessária para verificar se o prompt está ou não adequado de acordo com o enunciado

# Avaliar o prompt do usuário
feedback_usuario = avaliar_prompt(prompt_usuario)

if (avaliar_prompt == "Por favor, explique os conceitos de" + palavras_chave):
    print('O prompt está adequado')
elif (avaliar_prompt == "Crie" + palavras_chave):
    print("O prompt está adequado")
else(avaliar_prompt == "Qual é a coisa mais bonita do mundo?"):
    print("O prompt não está adequado. Inclua palavras-chave relevantes.")
  

# Exibir feedback
print(feedback_usuario)