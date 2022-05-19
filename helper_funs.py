import streamlit as st
import sqlite3
import pandas as pd

STOP_CODE='###'

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True


def execute_sql(sql_command):
    """Excecute a SQL command on the SQLite data. Note that the database path is hard coded in the function
    Args:
        sql_command (str): SQL command to execute
    """
    conn = sqlite3.connect('census_copy.sqlite')
    try:
        df = pd.read_sql_query(sql_command, conn)
        return df
    except:
        return None
    
def gen_codex_prompt2(question):
    """Generate string to use for the OpenAI CODEX API call using new examples
    Args:
        question (str): Question which should be translated into SQL
    """
    with open("codex_prompt_v2.txt") as file:
        schema_desc = file.read()
    egs = pd.read_csv('codex_examples.csv')
    egs = egs[egs.include == 1][['text', 'sql']]
    egs['quest_sql'] = '--' + egs['text']+ '\n' + egs['sql'] + STOP_CODE + '\n\n'
    examples_str = egs['quest_sql'].str.cat(sep='')
    return schema_desc + examples_str + '--' + question + '\n'