import streamlit as st

# Título do Formulário
st.title("Formulário de Agendamento de Veículos")

# Dados do Solicitante
st.header("Dados do Solicitante")
matricula = st.text_input("Matrícula do Solicitante")
nome = st.text_input("Nome do Solicitante")
telefone = st.text_input("Telefone do Solicitante")
email_solicitante = st.text_input("E-mail do Solicitante")
orgao_solicitante = st.text_input("Órgão solicitante")

# Dados da Partida
st.header("Dados da Partida")
municipio_partida = st.text_input("Município de Partida")
bairro_partida = st.text_input("Bairro de Partida")
rua_partida = st.text_input("Rua (Endereço de Partida)")
numero_partida = st.text_input("Número (Endereço de Partida)")

# Dados do Destino
st.header("Dados do Destino")
destinos = []
numero_destinos = st.number_input("Quantos destinos deseja adicionar?", min_value=1, max_value=5, step=1)
for i in range(numero_destinos):
    st.subheader(f"Destino {i + 1}")
    municipio_destino = st.text_input(f"Município de Destino {i + 1}", key=f"municipio_destino_{i}")
    bairro_destino = st.text_input(f"Bairro de Destino {i + 1}", key=f"bairro_destino_{i}")
    rua_destino = st.text_input(f"Rua (Endereço de Destino {i + 1})", key=f"rua_destino_{i}")
    numero_destino = st.text_input(f"Número (Endereço de Destino {i + 1})", key=f"numero_destino_{i}")
    destinos.append({
        "municipio": municipio_destino,
        "bairro": bairro_destino,
        "rua": rua_destino,
        "numero": numero_destino
    })

# Informações Adicionais
st.header("Informações Adicionais")
existe_pernoite = st.selectbox("Existe Pernoite?", ["Sim", "Não"])
qtd_pernoite = st.number_input("Quantidade de Pernoites", min_value=0, step=1)
data_retorno = st.date_input("Data de Retorno do Pernoite")
tipo_veiculo = st.text_input("Tipo de Veículo")

# Dados do Responsável
st.header("Dados do Responsável")
nome_responsavel = st.text_input("Nome do Responsável")
matricula_responsavel = st.text_input("Matrícula do Responsável")
email_responsavel = st.text_input("E-mail do Responsável")

# Botão para Enviar
if st.button("Enviar"):
    # Validação básica (pode ser expandida conforme necessário)
    if not matricula or not nome or not telefone or not email_logado or not orgao_logado:
        st.error("Por favor, preencha todos os campos obrigatórios!")
    else:
        # Exibe os dados inseridos (simula o envio)
        st.success("Formulário enviado com sucesso!")
        st.write("### Dados do Formulário:")
        st.json({
            "Solicitante": {
                "Matrícula": matricula,
                "Nome": nome,
                "Telefone": telefone,
                "E-mail Logado": email_logado,
                "E-mail": email_solicitante,
                "Órgão Logado": orgao_logado
            },
            "Partida": {
                "Município": municipio_partida,
                "Bairro": bairro_partida,
                "Rua": rua_partida,
                "Número": numero_partida
            },
            "Destinos": destinos,
            "Informações Adicionais": {
                "Existe Pernoite": existe_pernoite,
                "Quantidade de Pernoites": qtd_pernoite,
                "Data de Retorno": data_retorno,
                "Tipo de Veículo": tipo_veiculo
            },
            "Responsável": {
                "Nome": nome_responsavel,
                "Matrícula": matricula_responsavel,
                "E-mail": email_responsavel
            }
        })
