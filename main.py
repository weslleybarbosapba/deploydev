import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
	page_title="Seja bem-vindo!",
	page_icon=":earth_americas:"
)


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])


col2.st.title("Bem-Vindo")
    
names = "Weslley"
usernames = "weslleybarbosa@gmail.com"
passwords = "pweslley"

    # Esta dando erro na linha abaixo quando chama o generate
    # Pesquisando dentro do stauth não achei esta função 
    

    # hashed_passwords = stauth.Hasher([passwords]).generate()    

hashed_passwords = stauth.Hasher(passwords).generate()    
    
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, cookie_name='some_cookie_name', key='some_signature_key', cookie_expiry_days=30)
name, authenticator_status, username = authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    test=authenticator.logout('Logout', 'sidebar')
    st.write(f'Bem-Vindo *{st.session_state["nome"]}*')

elif st.session_state["authentication_status"] == False:
    st.error(" Usuario ou senha invalida")
elif st.session_state["authentication_status"] == None:
    st.warning("Por favor insira Usuario e senha")