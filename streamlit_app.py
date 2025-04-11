import streamlit as st

# Lista de municípios do estado do Rio de Janeiro
municipios_rj = [
    "Angra dos Reis", "Aperibé", "Araruama", "Areal", "Armação dos Búzios", "Arraial do Cabo", 
    "Barra do Piraí", "Barra Mansa", "Belford Roxo", "Bom Jardim", "Bom Jesus do Itabapoana", 
    "Cabo Frio", "Cachoeiras de Macacu", "Cambuci", "Campos dos Goytacazes", "Cantagalo", 
    "Carapebus", "Cardoso Moreira", "Carmo", "Casimiro de Abreu", "Comendador Levy Gasparian", 
    "Conceição de Macabu", "Cordeiro", "Duas Barras", "Duque de Caxias", "Engenheiro Paulo de Frontin", 
    "Guapimirim", "Iguaba Grande", "Itaboraí", "Itaguaí", "Italva", "Itaocara", "Itaperuna", 
    "Itatiaia", "Japeri", "Laje do Muriaé", "Macaé", "Macuco", "Magé", "Mangaratiba", "Maricá", 
    "Mendes", "Mesquita", "Miguel Pereira", "Miracema", "Natividade", "Nilópolis", "Niterói", 
    "Nova Friburgo", "Nova Iguaçu", "Paracambi", "Paraíba do Sul", "Paraty", "Paty do Alferes", 
    "Petrópolis", "Pinheiral", "Piraí", "Porciúncula", "Porto Real", "Quatis", "Queimados", 
    "Quissamã", "Resende", "Rio Bonito", "Rio Claro", "Rio das Flores", "Rio das Ostras", 
    "Rio de Janeiro", "Santa Maria Madalena", "Santo Antônio de Pádua", "São Fidélis", 
    "São Francisco de Itabapoana", "São Gonçalo", "São João da Barra", "São João de Meriti", 
    "São José de Ubá", "São José do Vale do Rio Preto", "São Pedro da Aldeia", "São Sebastião do Alto", 
    "Sapucaia", "Saquarema", "Seropédica", "Silva Jardim", "Sumidouro", "Tanguá", 
    "Teresópolis", "Trajano de Moraes", "Três Rios", "Valença", "Varre-Sai", "Vassouras", 
    "Volta Redonda"
]

# Título do Formulário
st.title("Formulário de Agendamento de Veículos")

# Campos do Solicitante
st.header("Dados do Solicitante")
matricula = st.text_input("Matrícula do Solicitante")
nome = st.text_input("Nome do Solicitante")
telefone = st.text_input("Telefone do Solicitante")
email_logado = st.text_input("E-mail Logado (Office)")
email_solicitante = st.text_input("E-mail do Solicitante")
orgao_logado = st.text_input("Órgão Usuário Logado")

# Campos de Partida
st.header("Dados da Partida")
municipio_partida = st.selectbox("Município de Partida", municipios_rj)
bairro_partida = st.text_input("Bairro de Partida")
rua_partida = st.text_input("Rua (Endereço de Partida)")
numero_partida = st.text_input("Número (Endereço de Partida)")

# Campos de Destino
st.header("Dados do Destino")
numero_destinos = st.number_input("Quantos destinos deseja adicionar?", min_value=1, max_value=5, step=1)
destinos = []
for i in range(numero_destinos):
    st.subheader(f"Destino {i + 1}")
    municipio_destino = st.selectbox(f"Município de Destino {i + 1}", municipios_rj, key=f"municipio_destino_{i}")
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
