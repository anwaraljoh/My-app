import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد الصفحة
st.set_page_config(
    page_title="منصة بلدية ينبع",
    page_icon="🏛️",
    layout="wide"
)

# قراءة البيانات
df = pd.read_excel("بلاغات_بلدية_ينبع_محدث(1).xlsx")

# تنسيق CSS
st.markdown("""
<style>
.main{
    background:#f7f9f7;
}
h1{
    color:#0B6E4F;
    text-align:center;
}
.card{
    background:white;
    padding:18px;
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,.1);
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("🏛️ منصة بلدية ينبع الرقمية")

# بطاقات KPI
c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown(f"""
    <div class='card'>
    <h2>{len(df)}</h2>
    <p>إجمالي البلاغات</p>
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='card'>
    <h2>{df['category'].nunique()}</h2>
    <p>عدد التصنيفات</p>
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='card'>
    <h2>{df['department'].nunique()}</h2>
    <p>الإدارات</p>
    </div>
    """,unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class='card'>
    <h2>{df['priority'].nunique()}</h2>
    <p>مستويات الأولوية</p>
    </div>
    """,unsafe_allow_html=True)

st.divider()

# الرسوم
left,right=st.columns(2)

with left:
    fig=px.bar(
        df["category"].value_counts().reset_index(),
        x="category",
        y="count",
        color="count",
        title="البلاغات حسب التصنيف"
    )
    st.plotly_chart(fig,use_container_width=True)

with right:
    fig2=px.pie(
        df,
        names="priority",
        title="توزيع الأولوية",
        hole=.5
    )
    st.plotly_chart(fig2,use_container_width=True)

fig3=px.bar(
    df["department"].value_counts().reset_index(),
    x="department",
    y="count",
    color="count",
    title="البلاغات حسب الإدارة"
)
st.plotly_chart(fig3,use_container_width=True)

st.subheader("📋 بيانات البلاغات")
st.dataframe(df,use_container_width=True,hide_index=True)

st.success("تم تحميل لوحة المعلومات بنجاح ✅")
