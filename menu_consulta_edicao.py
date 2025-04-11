import streamlit as st
import sqlite3

# Função para criar a conexão com o banco de dados
def conectar_banco():
    return sqlite3.connect('agendamento.db')

# Função para buscar todos os registros do banco de dados
def buscar_dados():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agendamentos")
    dados = cursor.fetchall()
    conn.close()
    return dados

# Função para atualizar um registro no banco de dados
def atualizar_dados(id, campo, novo_valor):
    conn = conectar_banco()
    cursor = conn.cursor()
    consulta = f"UPDATE agendamentos SET {campo} = ? WHERE id = ?"
    cursor.execute(consulta, (novo_valor, id))
    conn.commit()
    conn.close()

# Função para exibir os dados em formato de tabela
def exibir_tabela(dados):
    st.write("### Dados Salvos")
    st.write("Clique no botão abaixo para recarregar os dados.")
    colunas = [
        "ID", "Matrícula", "Nome", "Telefone", "Email Logado", "Email Solicitante",
        "Órgão", "Município Partida", "Bairro Partida", "Rua Partida", "Número Partida",
        "Município Destino", "Bairro Destino", "Rua Destino", "Número Destino",
        "Existe Pernoite", "Qtd Pernoite", "Data Retorno", "Tipo Veículo",
        "Nome Responsável", "Matrícula Responsável", "Email Responsável"
    ]

    # Renderizar os dados na tabela
    st.dataframe(
        [{col: valor for col, valor in zip(colunas, linha)} for linha in dados],
        use_container_width=True
    )

# Função para editar os dados de um registro específico
def editar_dados(dados):
    st.write("### Editar Registro")
    ids = [linha[0] for linha in dados]
    id_selecionado = st.selectbox("Selecione o ID do registro para editar", ids)

    if id_selecionado:
        registro = next((linha for linha in dados if linha[0] == id_selecionado), None)
        if registro:
            campo_selecionado = st.selectbox(
                "Selecione o campo para editar",
                [
                    "matricula", "nome", "telefone", "email_logado", "email_solicitante",
                    "orgao_logado", "municipio_partida", "bairro_partida", "rua_partida",
                    "numero_partida", "municipio_destino", "bairro_destino", "rua_destino",
                    "numero_destino", "existe_pernoite", "qtd_pernoite", "data_retorno",
                    "tipo_veiculo", "nome_responsavel", "matricula_responsavel", "email_responsavel"
                ]
            )
            novo_valor = st.text_input(f"Novo valor para {campo_selecionado}")
            if st.button("Salvar Alteração"):
                atualizar_dados(id_selecionado, campo_selecionado, novo_valor)
                st.success("Registro atualizado com sucesso!")

# Menu principal
st.title("Consulta e Edição de Dados")

menu = st.sidebar.radio("Menu", ["Consultar Dados", "Editar Dados"])

if menu == "Consultar Dados":
    st.subheader("Consultar Dados")
    if st.button("Carregar Dados"):
        dados = buscar_dados()
        exibir_tabela(dados)

elif menu == "Editar Dados":
    st.subheader("Editar Dados")
    dados = buscar_dados()
    if dados:
        editar_dados(dados)
    else:
        st.warning("Nenhum dado disponível para editar!")
