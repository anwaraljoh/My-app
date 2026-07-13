import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="منصة بلدية ينبع الرقمية", layout="wide")

# تصميم الألوان المطور (CSS)
st.markdown("""
    <style>
    /* تغيير لون الخلفية بالكامل */
    .stApp {background-color: #f4f7f6;}
    
    /* تنسيق الكروت (المؤشرات) */
    div[data-testid="stMetricValue"] {
        color: #006633; /* الأخضر الغامق */
        font-weight: bold;
    }
    
    /* تنسيق الحاويات */
    .css-1r6slb0 {background-color: #ffffff; padding: 20px; border-radius: 15px;}
    
    /* تنسيق العنوان */
    h1 {color: #006633; text-align: center; border-bottom: 2px solid #006633; padding-bottom: 10px;}
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ منصة إدارة البلاغات - بلدية محافظة ينبع")

# تحميل البيانات
@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

df = load_data()

# 1. المؤشرات (استخدام أعمدة ملفك الحقيقي)
col1, col2, col3 = st.columns(3)
col1.metric("إجمالي البلاغات", len(df))
col2.metric("عدد الإدارات المعنية", df['department'].nunique())
col3.metric("البلاغات عالية الأولوية", len(df[df['priority'] == 'عالية']))

st.markdown("<br>", unsafe_allow_html=True)

# 2. الرسوم البيانية
c1, c2 = st.columns([2, 1])

with c1:
    # توزيع البلاغات حسب الإدارة
    fig_bar = px.bar(df, x='department', title="توزيع البلاغات حسب الإدارة المختصة", 
                     color='department', color_discrete_sequence=px.colors.qualitative.Greens)
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    # توزيع حسب الأولوية
    fig_pie = px.pie(df, names='priority', title="حسب درجة الأهمية", 
                     hole=0.4, color_discrete_sequence=['#006633', '#8fbc8f', '#d3d3d3'])
    st.plotly_chart(fig_pie, use_container_width=True)

# 3. جدول البيانات
st.subheader("📋 تفاصيل البلاغات المسجلة")
st.dataframe(df, use_container_width=True)
