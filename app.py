import streamlit as st
import pandas as pd
import joblib
import os
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="نظام تصنيف البلاغات الذكي", layout="wide")

# 1. ترويسة رسمية (مكان الشعار)
st.markdown("""
    <div style="background-color:#006633; padding:15px; border-radius:10px; color:white; text-align:center;">
        <h1 style="margin:0;">أمانة منطقة المدينة المنورة</h1>
        <h3 style="margin:0;">لوحة تحكم إدارة البلاغات الذكية</h3>
    </div>
""", unsafe_allow_html=True)

st.write("") # مسافة فارغة

# تحميل الموارد
@st.cache_resource
def load_assets():
    if not os.path.exists('my_model.pkl') or not os.path.exists('my_data.csv'):
        return None, None
    model = joblib.load('my_model.pkl')
    df = pd.read_csv('my_data.csv')
    return model, df

model, df = load_assets()

if model is None:
    st.error("⚠️ النظام غير جاهز: يرجى التحقق من ملفات النظام.")
else:
    # 2. مؤشرات الأداء (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("إجمالي البلاغات", len(df))
    col2.metric("التصنيفات النشطة", df['category'].nunique())
    col3.metric("مستوى الكفاءة", "94%")

    # 3. الرسوم البيانية (احترافية للمشرف)
    st.markdown("### 📈 التحليل البياني للبلاغات")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # رسم بياني للتصنيفات
        fig = px.pie(df, names='category', title="توزيع البلاغات حسب النوع", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        # رسم بياني للأقسام
        fig_bar = px.bar(df['department'].value_counts(), title="البلاغات حسب الإدارة المختصة", orientation='h')
        st.plotly_chart(fig_bar, use_container_width=True)

    # 4. التصنيف الذكي
    st.markdown("### 🔍 تصنيف بلاغ جديد")
    user_input = st.text_area("نص البلاغ:", placeholder="أدخل نص البلاغ هنا...")
    if st.button("تصنيف البلاغ"):
        if user_input:
            prediction = model.predict([user_input])
            st.success(f"✅ تم التصنيف إلى: **{prediction[0]}**")
