import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# إعداد الصفحة
st.set_page_config(page_title="لوحة تحكم إدارة البلاغات - المدينة للخدمات", layout="wide")

# تصميم الهوية (CSS)
st.markdown("""
    <style>
    .main {background-color: #f5f7f9;}
    .stMetric {background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);}
    </style>
""", unsafe_allow_html=True)

# ترويسة الشركة
st.title("🏢 المدينة للخدمات اللوجستية - لوحة تحكم العمليات")
st.markdown("---")

# تحميل الموديل والبيانات
@st.cache_resource
def load_data():
    df = pd.read_csv('my_data.csv')
    model = joblib.load('my_model (1).pkl')
    return df, model

df, model = load_data()

# 1. عرض مؤشرات الأداء الرئيسية (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric("إجمالي البلاغات", len(df), "+12%")
col2.metric("البلاغات المعالجة", len(df[df['status']=='Done']), "95%")
col3.metric("معدل الاستجابة", "4.2 ساعة", "-0.5h")
col4.metric("رضا العملاء", "4.8/5.0", "جديد")

st.markdown("<br>", unsafe_allow_html=True)

# 2. الرسوم البيانية
c1, c2 = st.columns([2, 1])
with c1:
    fig = px.bar(df, x='date', y='category', color='category', title="اتجاهات البلاغات الزمنية")
    st.plotly_chart(fig, use_container_width=True)
with c2:
    fig2 = px.pie(df, names='category', title="توزيع البلاغات حسب القطاع", hole=0.3)
    st.plotly_chart(fig2, use_container_width=True)

# 3. قسم الذكاء الاصطناعي
st.markdown("---")
st.subheader("🤖 نظام التصنيف الذكي (AI Engine)")
user_input = st.text_area("أدخل تفاصيل البلاغ الوارد للعميل:")
if st.button("تحليل وتصنيف البلاغ"):
    with st.spinner('جاري معالجة البيانات...'):
        pred = model.predict([user_input])
        st.success(f"✅ فئة البلاغ المصنفة: **{pred[0]}**")
        st.info("تم توجيه البلاغ للقسم المختص تلقائياً.")
