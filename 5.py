# Entrada do usuário
prompt_usuario = input()

# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt):
    # Lista de palavras-chave relevantes
    palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia"]
    
    # Verifica se o prompt contém pelo menos uma das palavras-chave
    for palavra in palavras_chave:
        if palavra in prompt:
            return "adequado"
    return "não adequado"

# Avaliar o prompt do usuário
feedback_usuario = avaliar_prompt(prompt_usuario)

# Verificar o feedback e fornecer a resposta adequada
if feedback_usuario == "adequado":
    print("O prompt está adequado.")
else:
    print("O prompt não está adequado. Inclua palavras-chave relevantes.")