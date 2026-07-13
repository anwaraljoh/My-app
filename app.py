import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="نظام إدارة ينبع الذكي", layout="wide")

# تصميم CSS مخصص للتأثيرات (Hover & Fade)
st.markdown("""
    <style>
    .stApp {background-color: #0f172a;}
    .metric-card {
        background: linear-gradient(135deg, #1e293b, #334155);
        padding: 20px; border-radius: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid #334155;
    }
    .metric-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(16, 185, 129, 0.2);
    }
    h1 {color: #ffffff; text-align: center; margin-bottom: 30px;}
    </style>
""", unsafe_allow_html=True)

# العنوان مع شعار افتراضي
st.markdown("<h1>🏛️ منصة بلدية محافظة ينبع الرقمية</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

df = load_data()

# 1. عدادات متحركة (Animated Metrics)
cols = st.columns(4)
metrics = [("إجمالي البلاغات", len(df)), ("عالية الأولوية", len(df[df['priority'] == 'عالية'])), 
           ("عدد الإدارات", df['department'].nunique()), ("مستوى الإنجاز", "88%")]

for i, col in enumerate(cols):
    with col:
        st.markdown(f"""
            <div class="metric-card">
                <h2 style="color:#10b981;">{metrics[i][1]}</h2>
                <p style="color:#94a3b8;">{metrics[i][0]}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 2. رسوم بيانية أكثر حيوية من Power BI
c1, c2 = st.columns([1.5, 1])

with c1:
    # مخطط بار بتنسيق مخصص
    fig = px.bar(df['department'].value_counts().reset_index(), x='department', y='count',
                 color='count', color_continuous_scale='Mint', title="📊 توزيع البلاغات حسب الإدارة")
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                      font_color="white", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    # مخطط دونات بتأثيرات hover
    fig2 = px.pie(df, names='priority', title="📈 الأولوية", hole=0.7,
                  color_discrete_sequence=['#10b981', '#f59e0b', '#ef4444'])
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white", showlegend=True)
    st.plotly_chart(fig2, use_container_width=True)

# 3. الجدول التفاعلي
st.subheader("📋 سجل البلاغات")
st.dataframe(df, use_container_width=True, hide_index=True)
