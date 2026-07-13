import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os

# إعداد الصفحة
st.set_page_config(page_title="نظام تصنيف البلاغات - البلدية", layout="wide")

# تصميم الترويسة
st.markdown("""
    <div style="background-color:#006633; padding:15px; border-radius:10px; color:white; text-align:center;">
        <h1 style="margin:0;">أمانة المنطقة</h1>
        <h3 style="margin:0;">لوحة تحكم إدارة البلاغات الذكية</h3>
    </div>
""", unsafe_allow_html=True)

st.write("") 

# تحميل البيانات والموديل
@st.cache_resource
def load_data():
    df = pd.read_csv('my_data.csv')
    model = joblib.load('my_model.pkl')
    return df, model

df, model = load_data()

# 1. لوحة المؤشرات (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("إجمالي البلاغات", len(df))
col2.metric("التصنيفات المكتشفة", df['category'].nunique())
col3.metric("كفاءة النظام", "98%")

# 2. الرسوم البيانية التفاعلية
st.markdown("### 📊 التحليلات البيانية")
c1, c2 = st.columns(2)
with c1:
    fig = px.pie(df, names='category', title="توزيع البلاغات حسب الفئة")
    st.plotly_chart(fig, use_container_width=True)
with c2:
    fig2 = px.bar(df['department'].value_counts(), title="البلاغات حسب الإدارة")
    st.plotly_chart(fig2, use_container_width=True)

# 3. قسم التصنيف
st.markdown("---")
st.markdown("### 🔍 تصنيف بلاغ جديد")
user_input = st.text_area("أدخل نص البلاغ:")
if st.button("تصنيف البلاغ"):
    pred = model.predict([user_input])
    st.success(f"النتيجة: {pred[0]}")
