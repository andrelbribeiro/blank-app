import streamlit as st
from database import *

#st.write("Testando o CRUD ETEPD")

#st.set_page_config(page_title="CRUD Cliente", layout="centered")
criar_tabela()

st.title("Cadastro de Clientes")

menu = ["Cadastrar", "Listar / Editar / Excluir"]
escolha = st.sidebar.selectbox("Menu", menu)

# CADASTRAR
if escolha == "Cadastrar":
    st.subheader("Novo Cliente")

    with st.form(key="form_cliente"):
        nome = st.text_input("Nome", max_chars=100)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        email = st.text_input("Email")
        data_nascimento = st.date_input("Data de Nascimento")
        status = st.selectbox("Status", ["Ativo", "Inativo"])
        submit = st.form_submit_button("Cadastrar")

        if submit:
            inserir_cliente(nome, sexo, email, data_nascimento.isoformat(), status)
            st.success(f"Cliente {nome} cadastrado com sucesso!")

# LISTAR / EDITAR / EXCLUIR
elif escolha == "Listar / Editar / Excluir":
    st.subheader("Clientes Cadastrados")

    clientes = listar_clientes()
    if not clientes:
        st.info("Nenhum cliente cadastrado.")
    else:
        for c in clientes:
            with st.expander(f"{c[1]} - {c[2]}"):
                novo_nome = st.text_input(f"Nome - ID {c[0]}", value=c[1], key=f"nome{c[0]}")
                novo_sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"], index=["Masculino", "Feminino", "Outro"].index(c[2]), key=f"sexo{c[0]}")
                novo_email = st.text_input("Email", value=c[3], key=f"email{c[0]}")
                nova_data = st.date_input("Data de Nascimento", value=c[4], key=f"data{c[0]}")
                novo_status = st.selectbox("Status", ["Ativo", "Inativo"], index=["Ativo", "Inativo"].index(c[5]), key=f"status{c[0]}")

                col1, col2 = st.columns(2)
                if col1.button("Atualizar", key=f"update{c[0]}"):
                    atualizar_cliente(c[0], novo_nome, novo_sexo, novo_email, nova_data.isoformat(), novo_status)
                    st.success("Atualizado com sucesso.")
                    st.rerun()

                if col2.button("Excluir", key=f"delete{c[0]}"):
                    deletar_cliente(c[0])
                    st.warning("Cliente excluído.")
                    st.rerun()

