import streamlit as st
import pandas as pd
import plotly.express as px

# 1. إعداد الصفحة
st.set_page_config(page_title="منصة ينبع المركزية", layout="wide")

# 2. تصميم "Glassmorphism" إبداعي
st.markdown("""
    <style>
    .stApp {background: radial-gradient(circle at top right, #1e293b, #0f172a);}
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    h1 {color: #ffffff; text-align: center; font-weight: 900; letter-spacing: -1px; text-transform: uppercase;}
    .stMetricValue {color: #38bdf8 !important;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏛️ احصائيات بلدية محافظة ينبع لتصنيف البلاغات وتحليلها</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

df = load_data()

# 3. توزيع العناصر (Grid System)
c1, c2, c3 = st.columns([1, 2, 1])

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("إجمالي البلاغات", len(df))
    st.metric("الحرجة", len(df[df['priority']=='عالية']))
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    fig = px.bar(df['department'].value_counts().reset_index(), x='department', y='count',
                 color='count', color_continuous_scale='Bluered')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
    st.plotly_chart(fig, use_container_width=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### 🔍 فلترة سريعة")
    category = st.selectbox("اختر الفئة:", df['category'].unique())
    st.success(f"البلاغات في هذه الفئة: {len(df[df['category']==category])}")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. قسم الجدول (Modern Data Grid)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📋 سجل العمليات المباشر")
st.dataframe(df, use_container_width=True, hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)
