import streamlit as st
import pandas as pd
import joblib

# إعداد الصفحة
st.set_page_config(page_title="لوحة تحكم البلاغات", layout="wide")

st.title("📊 لوحة تحكم تصنيف البلاغات")

# تحميل الموارد
@st.cache_resource
def load_assets():
    model = joblib.load('my_model.pkl')
    df = pd.read_csv('my_data.csv')
    return model, df

model, df = load_assets()

# 1. إظهار ملخص للمشرف بدلاً من الجدول الخام
st.subheader("ملخص البلاغات")
col1, col2, col3 = st.columns(3)
col1.metric("إجمالي البلاغات", len(df))
col2.metric("التصنيفات المكتشفة", df['category'].nunique())
col3.metric("عدد الأقسام", df['department'].nunique())

# 2. عرض البيانات داخل Expander (مخفية افتراضياً)
with st.expander("عرض تفاصيل البلاغات (للأرشيف)"):
    st.dataframe(df, use_container_width=True)

# 3. قسم التنبؤ المخصص للمشرف
st.divider()
st.subheader("تصنيف بلاغ جديد")
user_input = st.text_input("أدخل نص البلاغ للتحليل:")

if st.button("تصنيف البلاغ"):
    if user_input:
        prediction = model.predict([user_input])
        st.success(f"النتيجة المتوقعة: {prediction[0]}")
    else:
        st.warning("يرجى كتابة نص البلاغ أولاً.")
