import streamlit as st
import pandas as pd
import joblib
import os

# إعداد الصفحة (نظام بلدي رسمي)
st.set_page_config(page_title="نظام تصنيف البلاغات - البلدية", layout="wide")

# تنسيق CSS لتعزيز المظهر الاحترافي
st.markdown("""
    <style>
    .main {background-color: #f5f7f9;}
    .stButton>button {width: 100%; border-radius: 5px; background-color: #006633; color: white;}
    </style>
""", unsafe_allow_html=True)

# ترويسة الصفحة
st.title("🏛️ لوحة تحكم تصنيف البلاغات")
st.subheader("إدارة العمليات - بلدية المنطقة")
st.markdown("---")

# تحميل الموارد
@st.cache_resource
def load_assets():
    # تأكد من أن الملفات موجودة في GitHub
    if not os.path.exists('my_model.pkl') or not os.path.exists('my_data.csv'):
        return None, None
    model = joblib.load('my_model.pkl')
    df = pd.read_csv('my_data.csv')
    return model, df

model, df = load_assets()

if model is None:
    st.error("⚠️ النظام غير جاهز: يرجى التأكد من وجود ملفات النموذج والبيانات.")
else:
    # 1. قسم المؤشرات (KPIs)
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("إجمالي البلاغات", len(df))
    kpi2.metric("التصنيفات الحالية", df['category'].nunique())
    kpi3.metric("مستوى الأداء", "89%")

    # 2. قسم التصنيف الذكي (النموذج)
    st.markdown("### 🔍 معالجة البلاغات الذكية")
    with st.container():
        user_input = st.text_area("أدخل نص البلاغ للتحليل الآلي:", placeholder="مثال: تراكم نفايات في شارع...")
        if st.button("تحليل وتصنيف البلاغ"):
            if user_input:
                try:
                    prediction = model.predict([user_input])
                    st.success(f"✅ فئة البلاغ: {prediction[0]}")
                except Exception as e:
                    st.error("خطأ في معالجة النص، يرجى التأكد من تدريب النموذج جيداً.")
            else:
                st.warning("يرجى كتابة نص البلاغ.")

    # 3. قسم البيانات (مع إمكانية إخفاءها)
    with st.expander("📂 استعراض سجل البلاغات التاريخي"):
        st.dataframe(df, use_container_width=True)
