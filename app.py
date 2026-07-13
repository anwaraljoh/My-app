import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# إعداد الصفحة
st.set_page_config(page_title="نظام الإدارة الذكي - ينبع", layout="wide")

# تصميم CSS متطور (خلفية داكنة احترافية للعناصر، وخلفية فاتحة للنظام)
st.markdown("""
    <style>
    .stApp {background-color: #0f172a;} /* خلفية النظام */
    .css-1r6slb0 {background-color: #1e293b; border-radius: 15px; padding: 20px;}
    h1 {color: #ffffff; text-align: center; font-family: 'Tajawal', sans-serif;}
    .metric-card {background-color: #334155; padding: 20px; border-radius: 15px; color: white; text-align: center;}
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ منصة إدارة البلاغات الذكية - محافظة ينبع")
st.markdown("<p style='text-align:center; color:#94a3b8;'>نظام متطور لتحليل وتصنيف البلاغات البلدية - إصدار 2026</p>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

df = load_data()

# 1. لوحة المؤشرات (KPIs) بشكل هندسي
cols = st.columns(4)
metrics = [
    ("إجمالي البلاغات", len(df)),
    ("عالية الأهمية", len(df[df['priority'] == 'عالية'])),
    ("الإدارات المفعلة", df['department'].nunique()),
    ("البلاغات المنجزة", "84%")
]

for i, col in enumerate(cols):
    with col:
        st.markdown(f"""
            <div class="metric-card">
                <h3 style="color:#10b981;">{metrics[i][1]}</h3>
                <p style="font-size:14px; color:#cbd5e1;">{metrics[i][0]}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 2. الرسوم البيانية المتطورة
c1, c2 = st.columns([1, 1])

with c1:
    # مخطط بار "مطور"
    fig = px.bar(df['department'].value_counts().reset_index(), x='department', y='count',
                 color='count', color_continuous_scale='Mint', title="البلاغات حسب الإدارة")
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    # مخطط دائري "مطور"
    fig2 = px.pie(df, names='priority', title="توزيع الأولوية", hole=0.6,
                  color_discrete_sequence=['#10b981', '#fbbf24', '#ef4444'])
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig2, use_container_width=True)

# 3. الجدول التفاعلي (احترافي)
st.subheader("📋 سجل البلاغات التفصيلي")
st.dataframe(df, use_container_width=True, hide_index=True)
