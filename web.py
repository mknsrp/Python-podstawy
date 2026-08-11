# Final web-app feature: checking a checkbox MARKS the todo complete
# (removes it from todos.txt and from the UI).
#
# Steps in the loop:
#   1. Iterate with enumerate() so we have the index of each todo.
#   2. Give each checkbox a unique key — the todo string itself works
#      (each line in todos.txt is unique anyway). That makes it show
#      up in st.session_state.
#   3. The variable `st.checkbox(...)` returns is True when checked,
#      False otherwise.
#   4. If True: pop by index, save the file, delete the key from
#      session_state (otherwise the next rerun would still "remember"
#      it as checked), and force a rerun so the UI refreshes
#      immediately.
#
# `st.experimental_rerun()` (renamed to `st.rerun()` in newer Streamlit
# versions) stops the current run and starts a fresh one with the
# updated todos.

import functions
import streamlit as st


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
