import streamlit as st
import pandas as pd
import plotly.express as px

# 1. إعداد الصفحة
st.set_page_config(page_title="منصة بلدية محافظة ينبع", layout="wide")

# 2. تصميم CSS "مُعزز" (إضاءة احترافية وخلفية فخمة)
st.markdown("""
    <style>
    .stApp {background-color: #0b1120;}
    .metric-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px;
        border: 1px solid #334155;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    h1 {color: #ffffff; text-align: center; font-size: 2.5em; padding-bottom: 20px;}
    .stDataFrame {border-radius: 15px; overflow: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. العنوان
st.markdown("<h1>🏛️ منصة بلدية محافظة ينبع لتصنيف البلاغات وتحليلها</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

df = load_data()

# 4. العدادات المتحركة (KPIs)
cols = st.columns(4)
stats = [("إجمالي البلاغات", len(df)), ("بلاغات حرجة", len(df[df['priority']=='عالية'])), 
         ("الإدارات المعنية", df['department'].nunique()), ("مستوى المعالجة", "92%")]

for i, col in enumerate(cols):
    with col:
        st.markdown(f'''<div class="metric-card">
            <h2 style="color:#34d399; margin:0;">{stats[i][1]}</h2>
            <p style="color:#94a3b8; margin:5px 0 0 0;">{stats[i][0]}</p>
        </div>''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. رسوم بيانية (شفافة واحترافية)
c1, c2 = st.columns([1.8, 1.2])

with c1:
    fig_bar = px.bar(df['department'].value_counts().reset_index(), x='department', y='count',
                     title="توزيع البلاغات حسب الإدارة", color='count', color_continuous_scale='Greens')
    fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    fig_pie = px.pie(df, names='priority', title="حالة الأولويات", hole=0.6,
                     color_discrete_sequence=['#ef4444', '#fbbf24', '#10b981'])
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_pie, use_container_width=True)

# 6. الجدول
st.subheader("📋 سجل البلاغات التفصيلي")
st.dataframe(df, use_container_width=True, hide_index=True)
