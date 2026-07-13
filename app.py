import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد الصفحة لتكون بوضع "واسع"
st.set_page_config(page_title="منصة رصد البلاغات - بلدية ينبع", layout="wide")

# تصميم الهوية (ألوان رسمية)
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1 {color: #006633; text-align: center;}
    </style>
""", unsafe_allow_html=True)

st.title("🚧 لوحة المؤشرات الاستراتيجية - بلدية محافظة ينبع")
st.markdown("---")

# تحميل البيانات
@st.cache_data
def load_data():
    return pd.read_csv('my_data.csv')

try:
    df = load_data()

    # 1. شريط المؤشرات (KPIs)
    col1, col2, col3 = st.columns(3)
    
    # حساب الإحصائيات
    total_reports = len(df)
    # تأكد أن اسم العمود هو 'status' في ملف CSV الخاص بك
    done_reports = len(df[df['status'] == 'Done']) if 'status' in df.columns else 0
    unique_cats = df['category'].nunique()

    col1.metric("إجمالي البلاغات", total_reports)
    col2.metric("البلاغات المنجزة", done_reports)
    col3.metric("عدد الفئات المصنفة", unique_cats)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. قسم الرسوم البيانية
    c1, c2 = st.columns([2, 1])

    with c1:
        # مخطط توزيع البلاغات حسب الفئة
        fig_bar = px.bar(df, x='category', title="توزيع البلاغات حسب الفئة", color='category')
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        # مخطط دائري للحالة
        if 'status' in df.columns:
            fig_pie = px.pie(df, names='status', title="حالة المعالجة", hole=0.4)
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.write("عمود 'status' غير موجود في البيانات.")

    # 3. جدول البيانات التفصيلي
    st.subheader("📋 سجل البلاغات التفصيلي")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل البيانات: {e}")
    st.info("تأكد أن ملف `my_data.csv` موجود في المستودع ويحتوي على الأعمدة المطلوبة.")
