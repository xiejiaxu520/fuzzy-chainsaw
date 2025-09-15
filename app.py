import streamlit as st
import pandas as pd
import numpy as np
import requests
import random

st.set_page_config(page_title="趣味数据探索屋", page_icon="🎉", layout="wide")

st.title("🎉 趣味数据探索屋")
st.write("""
欢迎来到趣味数据探索屋！这里你可以：
- 探索实时天气数据
- 玩一个AI生成的猜数字小游戏
- 可视化模拟股票走势
- 体验AI智能问答
""")

# 1. 实时天气数据展示
st.header("🌦️ 实时天气查询")
city = st.text_input("输入城市（如 Beijing）:", "Beijing")
if st.button("查询天气"):
    url = f"https://wttr.in/{city}?format=%C+%t"
    try:
        weather = requests.get(url).text
        st.success(f"{city} 当前天气: {weather}")
    except Exception:
        st.error("天气查询失败，请检查城市名称或网络连接。")

st.divider()

# 2. AI生成猜数字小游戏
st.header("🎲 猜数字小游戏")
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if "tries" not in st.session_state:
    st.session_state.tries = 0

guess = st.number_input("猜一个 1 到 100 的数字：", min_value=1, max_value=100, step=1)
if st.button("提交猜测"):
    st.session_state.tries += 1
    if guess == st.session_state.secret_number:
        st.success(f"恭喜你猜对了！答案是 {guess}，共尝试了 {st.session_state.tries} 次。")
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0
    elif guess < st.session_state.secret_number:
        st.info("再大一点试试！")
    else:
        st.info("再小一点试试！")

st.divider()

# 3. 股票走势模拟与可视化
st.header("📈 股票模拟走势")
days = st.slider("模拟天数", 30, 180, 60)
price = 100
np.random.seed(42)
returns = np.random.normal(loc=0.001, scale=0.02, size=days)
prices = price * np.cumprod(1 + returns)
df = pd.DataFrame({"Day": np.arange(days), "Price": prices})
st.line_chart(df.set_index("Day"), use_container_width=True)

st.divider()

# 4. AI智能问答（本地示例，仅演示界面）
st.header("💡 AI智能问答体验")
question = st.text_input("输入你的问题：", "")
if st.button("AI回答"):
    if question:
        answers = [
            "这是个很棒的问题！",
            "AI正在努力思考中……",
            "答案可能在你心中。",
            f"关于“{question}”，我认为你可以进一步探索！"
        ]
        st.write(random.choice(answers))
    else:
        st.info("请先输入一个问题。")

st.divider()
st.caption("由 Streamlit 强力驱动，为你带来数据的乐趣与实用价值。")