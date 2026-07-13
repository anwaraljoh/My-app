import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="منصة رصد البلاغات - بلدية ينبع", layout="wide")

# تنسيق الألوان (هوية بلدية)
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1 {color: #006633; text-align: center;}
    </style>
""", unsafe_allow_html=True)

st.title("🚧 لوحة المؤشرات الاستراتيجية - بلدية محافظة ينبع")
st.markdown("---")

# تحميل البيانات ومعالجتها
@st.cache_data
def load_data():
    df = pd.read_csv('my_data.csv')
    
    # إضافة عمود حالة افتراضي إذا لم يكن موجوداً
    if 'status' not in df.columns:
        df['status'] = 'قيد المعالجة'
    
    return df

try:
    df = load_data()

    # 1. شريط المؤشرات (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("إجمالي البلاغات", len(df))
    col2.metric("الحالة العامة", "نشط")
    col3.metric("عدد الفئات المصنفة", df['category'].nunique())

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. قسم الرسوم البيانية
    # بما أننا نركز على 'category'، سنعرض توزيع البلاغات حسب الفئة
    fig_bar = px.bar(df, x='category', title="توزيع البلاغات حسب الفئة", 
                     color='category', template="plotly_white")
    st.plotly_chart(fig_bar, use_container_width=True)

    # 3. جدول البيانات
    st.subheader("📋 سجل البلاغات")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"حدث خطأ: {e}")
    st.info("تأكد أن ملف `my_data.csv` موجود في المستودع.")
