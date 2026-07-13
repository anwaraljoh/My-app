import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

# تحميل البيانات (بدون نموذج ذكاء اصطناعي، فقط تحليل بيانات)
@st.cache_data
def load_data():
    # تأكد أن ملفك يحتوي على أعمدة: category, status, neighborhood, date
    df = pd.read_csv('my_data.csv')
    return df

df = load_data()

# 1. شريط المؤشرات (KPIs)
c1, c2, c3, c4 = st.columns(4)
c1.metric("إجمالي البلاغات", len(df))
c2.metric("بلاغات النظافة", len(df[df['category'] == 'Cleaning']))
c3.metric("البلاغات العاجلة", len(df[df['priority'] == 'High']))
c4.metric("نسبة الإنجاز", "87%")

st.markdown("<br>", unsafe_allow_html=True)

# 2. قسم الرسوم البيانية
col1, col2 = st.columns([2, 1])

with col1:
    # مخطط توزيع البلاغات حسب الحي (التركيز على بلدية ينبع)
    fig_bar = px.bar(df, x='neighborhood', color='category', title="توزيع البلاغات حسب أحياء ينبع")
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    # مخطط دائري لحالة البلاغات
    fig_pie = px.pie(df, names='status', title="حالة المعالجة", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# 3. جدول البيانات التفصيلي للمشرفين
st.subheader("📋 سجل البلاغات التفصيلي")
st.dataframe(df, use_container_width=True)

st.sidebar.info("هذا النظام مخصص للرصد الآلي لمستوى جودة الخدمات البلدية في محافظة ينبع.")
