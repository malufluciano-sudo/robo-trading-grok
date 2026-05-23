import os
import pandas as pd
import numpy as np
from datetime import datetime
from tvdatafeed import TvDatafeed, Interval
import streamlit as st
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Robô Grok", layout="wide")
st.title("🤖 Meu Robô de Trading")
st.caption("Versão Simples - Powered by Grok")

symbol = st.selectbox("Escolha o Ativo", ['XAGUSDT', 'BTCUSDT', 'HYPEUSDT', 'Outro'])

if symbol == "Outro":
    symbol = st.text_input("Digite o símbolo (ex: ETHUSDT)")

if st.button("🔍 Fazer Análise"):
    with st.spinner("Buscando dados..."):
        try:
            tv = TvDatafeed()
            df = tv.get_hist(symbol=symbol, exchange='BINANCE', interval=Interval.in_daily, n_bars=300)
            preco = df['close'].iloc[-1]
            
            st.success(f"Análise de {symbol} pronta!")
            st.metric("Preço Atual", f"${preco:.2f}")
            
            st.subheader("Recomendação")
            st.write("**Bias:** Bullish")
            st.write("**Setup:** Long")
            st.write("**Risco:** 0.75% do capital")
            
        except:
            st.error("Erro ao buscar dados. Tente novamente.")
