import streamlit as st
from datetime import datetime

# Настройки страницы
st.set_page_config(
    page_title="Моё приложение",
    page_icon="🚀",
    layout="centered"
)

# Заголовок
st.title("Мой первый веб-приложение 🌐")

# --- Конвертер валют (используем фиктивный курс) ---
st.header("💰 Конвертер валют")
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Сумма", min_value=0.0, value=100.0, step=10.0)
with col2:
    currency = st.selectbox("Валюта", ["USD → RUB", "EUR → RUB", "RUB → USD"])

# Фиктивные курсы
rates = {
    "USD → RUB": 90.25,
    "EUR → RUB": 98.50,
    "RUB → USD": 1/90.25
}

if st.button("Конвертировать"):
    result = amount * rates[currency]
    st.success(f"Результат: **{result:.2f}**")

# --- Трекер задач ---
st.header("📝 Мои задачи")

# Инициализация списка задач в session_state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Форма для добавления задачи
with st.form("task_form"):
    new_task = st.text_input("Новая задача")
    due_date = st.date_input("Срок выполнения")
    submitted = st.form_submit_button("Добавить задачу")

    if submitted and new_task:
        task = {
            "text": new_task,
            "due_date": due_date,
            "created_at": datetime.now()
        }
        st.session_state.tasks.append(task)
        st.rerun()

# Отображение задач
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        with st.expander(f"Задача {i+1}: {task['text']}"):
            st.write(f"📅 Срок: {task['due_date']}")
            st.write(f"🕒 Создано: {task['created_at'].strftime('%H:%M %d.%m.%Y')}")
            if st.button(f"Удалить задачу {i+1}", key=f"delete_{i}"):
                del st.session_state.tasks[i]
                st.rerun()
else:
    st.info("Пока задач нет. Добавьте первую!")

# --- Инструкция ---
st.markdown("---")
st.caption("ℹ️ Чтобы запустить приложение, выполните в терминале: `streamlit run app.py`")
