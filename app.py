import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# إعدادات الصفحة
st.set_page_config(page_title="نظام تصنيف البلاغات", layout="wide")

# ترويسة
st.markdown("<h1 style='text-align: center; color: #006633;'>🏛️ لوحة تحكم إدارة البلاغات</h1>", unsafe_allow_html=True)

# تحميل البيانات والموديل (هنا استخدمنا الاسم الذي طلبتَه)
@st.cache_resource
def load_assets():
    df = pd.read_csv('my_data.csv')
    # قمنا بتغيير الاسم هنا ليتطابق مع الملف الموجود عندك
    model = joblib.load('my_model (1).pkl') 
    return df, model

df, model = load_assets()

# عرض الرسوم البيانية
col1, col2 = st.columns(2)
with col1:
    fig = px.pie(df, names='category', title="توزيع البلاغات حسب الفئة")
    st.plotly_chart(fig, use_container_width=True)

# منطقة التصنيف
st.divider()
st.subheader("🔍 تصنيف بلاغ جديد")
text = st.text_input("أدخل نص البلاغ للتحليل:")

if st.button("تصنيف البلاغ"):
    if text:
        # التنبؤ
        pred = model.predict([text])
        st.success(f"✅ فئة البلاغ هي: **{pred[0]}**")
    else:
        st.warning("يرجى كتابة نص البلاغ.")ed[0]}")
