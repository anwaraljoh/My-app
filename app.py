import streamlit as st
import pandas as pd
import plotly.express as px

# 1. إعداد الصفحة لتعطي مساحة كاملة
st.set_page_config(page_title="منصة بلدية محافظة ينبع", layout="wide")

# 2. تصميم CSS احترافي (Dark Theme - متكامل)
st.markdown("""
    <style>
    .stApp {background-color: #0b1120;}
    /* تنسيق الكروت */
    .metric-card {background: linear-gradient(145deg, #1e293b, #0f172a); padding: 20px; border-radius: 15px; border: 1px solid #334155; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.3);}
    /* تنسيق النصوص */
    h1 {color: #ffffff; text-align: center; font-weight: 700; margin-bottom: 30px;}
    .stSelectbox, .stMultiSelect {background-color: #1e293b;}
    </style>
""", unsafe_allow_html=True)

# العنوان
st.markdown("<h1>🏛️ منصة بلدية محافظة ينبع لتصنيف البلاغات وتحليلها</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

df = load_data()

# 3. الفلتر الذكي (Sidebar) - دمج التحكم في البيانات
st.sidebar.header("⚙️ خيارات التصفية")
selected_dept = st.sidebar.multiselect("اختر الإدارات المطلوبة:", df['department'].unique(), default=df['department'].unique())
df_filtered = df[df['department'].isin(selected_dept)]

# 4. العدادات (KPIs) - المعلومات الأساسية
cols = st.columns(4)
stats = [("إجمالي البلاغات", len(df_filtered)), ("البلاغات الحرجة", len(df_filtered[df_filtered['priority']=='عالية'])), 
         ("عدد الإدارات", df_filtered['department'].nunique()), ("معدل الإنجاز", "92%")]

for i, col in enumerate(cols):
    with col:
        st.markdown(f'''<div class="metric-card">
            <h2 style="color:#34d399; margin:0;">{stats[i][1]}</h2>
            <p style="color:#94a3b8; font-size:14px; margin-top:5px;">{stats[i][0]}</p>
        </div>''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. الرسوم البيانية - دمج التحليل البصري
c1, c2 = st.columns([2, 1])

with c1:
    fig_bar = px.bar(df_filtered['department'].value_counts().reset_index(), x='department', y='count',
                     title="📊 توزيع البلاغات حسب الإدارة", color='count', color_continuous_scale='Greens')
    fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    fig_pie = px.pie(df_filtered, names='priority', title="📈 حالة الأولويات", hole=0.6,
                     color_discrete_sequence=['#ef4444', '#fbbf24', '#10b981'])
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig_pie, use_container_width=True)

# 6. الجدول التفصيلي - دمج التفاصيل
st.subheader("📋 سجل البيانات التفصيلي")
st.dataframe(df_filtered[['complaint', 'category', 'priority', 'department']], use_container_width=True, hide_index=True)
