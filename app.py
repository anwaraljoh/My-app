import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="منصة بلدية ينبع الرقمية", layout="wide")

# تنسيق الخلفية والألوان (نظام ألوان رسمي)
st.markdown("""
    <style>
    .stApp {background-color: #f4f7f6;}
    h1 {color: #006633; text-align: center; font-weight: bold;}
    .stMetric {background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);}
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ منصة إدارة وتصنيف البلاغات - بلدية ينبع")

# تحميل البيانات
@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

df = load_data()

# 1. شريط المؤشرات (KPIs) بناءً على أعمدة بياناتك
col1, col2, col3, col4 = st.columns(4)
col1.metric("إجمالي البلاغات", len(df))
col2.metric("عالية الأهمية", len(df[df['priority'] == 'عالية']))
col3.metric("عدد الإدارات", df['department'].nunique())
col4.metric("أكثر فئة تكراراً", df['category'].mode()[0])

st.markdown("<br>", unsafe_allow_html=True)

# 2. الرسوم البيانية التفاعلية
c1, c2 = st.columns([1, 1])

with c1:
    # توزيع البلاغات حسب الإدارة
    fig_dept = px.bar(df['department'].value_counts().reset_index(), 
                     x='department', y='count', title="البلاغات حسب الإدارة",
                     color='count', color_continuous_scale='Greens')
    st.plotly_chart(fig_dept, use_container_width=True)

with c2:
    # توزيع حسب الأولوية
    fig_pri = px.pie(df, names='priority', title="توزيع البلاغات حسب الأولوية",
                     color_discrete_sequence=['#ff4b4b', '#ffa500', '#006633'])
    st.plotly_chart(fig_pri, use_container_width=True)

# 3. سجل البيانات
st.subheader("📋 تفاصيل البلاغات")
st.dataframe(df[['complaint', 'category', 'priority', 'department']], use_container_width=True)
