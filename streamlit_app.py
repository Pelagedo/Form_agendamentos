import streamlit as st
import sqlite3

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect('agendamento.db')

# Função para buscar todos os registros do banco
def buscar_dados():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agendamentos")
    dados = cursor.fetchall()
    conn.close()
    return dados

# Função para atualizar um campo específico no banco de dados
def atualizar_dados(id, campo, novo_valor):
    conn = conectar_banco()
    cursor = conn.cursor()
    consulta = f"UPDATE agendamentos SET {campo} = ? WHERE id = ?"
    cursor.execute(consulta, (novo_valor, id))
    conn.commit()
    conn.close()

# Função para exibir os registros em formato de tabela
def exibir_dados():
    dados = buscar_dados()
    if dados:
        st.write("### Registros Salvos")
        st.write("Abaixo estão os registros salvos no banco de dados:")
        colunas = [
            "ID", "Matrícula", "Nome", "Telefone", "Email Logado", "Email Solicitante",
            "Órgão", "Município Partida", "Bairro Partida", "Rua Partida", "Número Partida",
            "Município Destino", "Bairro Destino", "Rua Destino", "Número Destino",
            "Existe Pernoite", "Qtd Pernoite", "Data Retorno", "Tipo Veículo",
            "Nome Responsável", "Matrícula Responsável", "Email Responsável"
        ]
        st.dataframe(
            [{col: valor for col, valor in zip(colunas, linha)} for linha in dados],
            use_container_width=True
        )
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

# Função para editar um registro
def editar_dados():
    dados = buscar_dados()
    if dados:
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
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

# Função principal para o menu
def main():
    st.title("Menu de Consulta e Edição de Dados")

    # Menu lateral
    menu = st.sidebar.radio("Menu", ["Consultar Dados", "Editar Dados", "Enviar Novo Formulário"])

    if menu == "Consultar Dados":
        st.subheader("Consultar Dados")
        exibir_dados()

    elif menu == "Editar Dados":
        st.subheader("Editar Dados")
        editar_dados()

    elif menu == "Enviar Novo Formulário":
        st.subheader("Enviar Novo Formulário")
        # Aqui você pode reutilizar o código do formulário original
        st.write("Formulário será implementado aqui.")

# Executa o app
if __name__ == "__main__":
    main()
