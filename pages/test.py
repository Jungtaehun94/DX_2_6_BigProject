import streamlit as st
st.markdown("""
<head>
<style>
.myDiv {
  border: 5px outset red;
  background-color: lightblue;
  text-align: center;
}
</style>
</head>
<script>$('#target-div').load('http://www.example.com/portfolio.php #portfolio-sports');</script>
<body>

<div class="myDiv">
  <h2>This is a heading in a div element</h2>
  <p>This is some text in a div element.</p>
</div>

</body>
""", unsafe_allow_html = True)
