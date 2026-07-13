import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="منصة بلدية ينبع الرقمية", layout="wide")

# تصميم احترافي (خلفية هادئة وخطوط واضحة)
st.markdown("""
    <style>
    /* تغيير لون الخلفية بالكامل إلى رمادي فاتح جداً */
    .stApp {background-color: #f8f9fa;}
    
    /* تنسيق الكروت لتكون بيضاء ونظيفة */
    div[data-testid="stMetricValue"] {
        color: #006633;
        font-weight: bold;
    }
    
    /* العنوان */
    h1 {color: #006633; text-align: center; padding-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ منصة إدارة وتصنيف البلاغات - بلدية محافظة ينبع")

# تحميل البيانات
@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

df = load_data()

# 1. شريط المؤشرات (KPIs) - استخدام الأعمدة الموجودة في ملفك
col1, col2, col3 = st.columns(3)
col1.metric("إجمالي البلاغات", len(df))
col2.metric("عدد الإدارات المعنية", df['department'].nunique())
col3.metric("البلاغات عالية الأهمية", len(df[df['priority'] == 'عالية']))

st.markdown("<br>", unsafe_allow_html=True)

# 2. الرسوم البيانية
c1, c2 = st.columns([2, 1])

with c1:
    # مخطط توزيع البلاغات حسب الإدارة
    fig_bar = px.bar(df['department'].value_counts().reset_index(), 
                     x='department', y='count', title="📊 توزيع البلاغات حسب الإدارة",
                     color='count', color_continuous_scale='Greens')
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    # مخطط دائري للأولويات
    fig_pie = px.pie(df, names='priority', title="📈 تصنيف البلاغات حسب الأولوية", 
                     hole=0.4, color_discrete_sequence=['#006633', '#8fbc8f', '#d3d3d3'])
    st.plotly_chart(fig_pie, use_container_width=True)

# 3. جدول البيانات
st.subheader("📋 سجل البيانات التفصيلي")
st.dataframe(df[['complaint', 'category', 'priority', 'department']], use_container_width=True)

# تذييل الصفحة
st.markdown("---")
st.markdown("<center>نظام مراقبة الأداء - بلدية محافظة ينبع © 2026</center>", unsafe_allow_html=True)
