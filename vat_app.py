import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price=st.number_input("กรอกราคาสินค้า (บาท):",value=0.0)
vat=price*0.07
st.header(f"•ภาษีมูลค่าเพิ่ม (VAT 7%):**{VAT:.2f}**บาท")
net_price=price-vat
st.header(f"•ราคาบริสุทธิ:{net_price:.2f}บาท")
st.divider()
st.write("นางสาวณภษร ปฐมทิตรเมธา เลขที่9 ม.4/13")
