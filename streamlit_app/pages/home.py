import streamlit as st

st.set_page_config(
    page_title="Smart Traffic Violation Analytics",
    page_icon="🚦",
    layout="wide"
)

carousel_html = """
<link rel="stylesheet"
href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
<style>
#carouselExampleIndicators,
#carouselExampleIndicators .carousel-inner,
#carouselExampleIndicators .carousel-item {
    border-radius: 20px;
    overflow: hidden;   
}
#carouselExampleIndicators .carousel-item img {
    border-radius: 20px;  
    object-fit: cover;   
    width: 100%;
    height: 520px;       
}
.carousel-caption {
    top: 50%;                
    transform: translateY(-50%);  
    bottom: initial;         
    text-align: center;      
}
.carousel-caption .caption-box {
    background: rgba(0, 0, 0, 0.4); 
    padding: 20px 20px 20px 20px;
    border-radius: 15px;
    display: inline-block;
    text-align:center;
    color: yellow;
    font-weight: bold;
    overflow: hidden;         
    text-overflow: ellipsis;
    white-space: nowrap;    
    margin-left:0;
}
.carousel-caption h2 {
    font-size: 2.5rem;
    white-space: nowrap;
    background: linear-gradient(90deg,#f50c94,white,#6047ed,white,orange);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;  
}
pre{
color:white;
font-size:1.3rem;
}
</style>

<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" data-interval="2000">
  <div class="carousel-inner">
  
    <div class="carousel-item">
        <img class="d-block w-100" src="https://plus.unsplash.com/premium_photo-1661932971080-c6ec2a91f64c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y3JvcCUyMHJlY29tbWVkYXRpb258ZW58MHx8MHx8fDA%3D" alt="Third slide">
        <div class="carousel-caption d-none d-md-block">
            <div class="caption-box">
                <h2>Crop Recommendation & Price Prediction</h2>
                <pre><i>Welcome to the Crop Recommendation & Price Prediction Dashboard. </i>
<i>Use the left sidebar to navigate across sections.</i>
</pre>
            </div>
        </div>
    </div>

    <div class="carousel-item active">
      <img class="d-block w-100" src="https://plus.unsplash.com/premium_photo-1661912366100-edf0de442ac3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGNyb3AlMjByZWNvbW1lZGF0aW9uJTIwYW5kJTIwcHJpY2UlMjBwcmVkaWN0aW9ufGVufDB8fDB8fHww" alt="First slide">
        <div class="carousel-caption d-none d-md-block">
            <div class="caption-box">
                <h2>Crop Recommendation & Price Prediction</h2>
                <pre><i>Welcome to the Crop Recommendation & Price Prediction Dashboard.  </i>
<i>Use the left sidebar to navigate across sections.</i>
</pre>
            </div>
        </div>
    </div>
  </div>
</div>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
"""

st.components.v1.html(carousel_html,height=550)

st.markdown('<h2 style="text-align:center";>About</h2>',unsafe_allow_html=True)
st.markdown('<p style="font-size:1.5rem;background: linear-gradient(90deg,#f50c94,#6047ed,orange);-webkit-background-clip: text;-webkit-text-fill-color: transparent;"><i>This system is an intelligent crop recommendation and price prediction platform designed to assist farmers and agribusinesses.It takes key soil nutrients such as Nitrogen, Phosphorus, Potassium, along with humidity as input parameters.Based on these factors, the system recommends the most suitable crop for cultivation.It also predicts the expected market price of the recommended crop using data-driven models.The goal is to improve yield, profitability, and informed decision-making in agriculture.</i> </p> ',unsafe_allow_html=True)


