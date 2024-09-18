
import streamlit as st
import pandas as pd
from streamlit_navigation_bar import st_navbar

page = st_navbar(["User Overview Analysis", "User Engagement Analysis", "Experience Analytics"])
st.write(page)
st.sidebar.title("User Analytics in the Telecommunication Industry")
st.sidebar.write("In this project we have to provide a report to analyze opportunities for growth and make a recommendation on whether TellCo is worth buying or selling. we will do this by analyzing a telecommunication dataset that contains useful information about the customers & their activities on the network. We will deliver insights you managed to extract to employer through an easy-to-use web-based dashboard and a written report.")

container = st.container()
container.title("Task 1 - User Overview analysis")

status = st.radio(
    'Select any option to view result',
    ('Top 10 handsets used by the customers', 'Top 3 handset manufacturers', 'top 5 handsets per top 3 handset manufacturer')
)

if status is "Top 10 handsets used by the customers":
    st.image("top 10 handset.png")
    st.write("frequency of different handset types: The most common handset type is Huawei B5285-23A, followed by Apple iPhone 6S (A1688) and Apple iPhone 6 (A1586). The least common handset type is Apple iPhone X (A1901)")

elif status is 'Top 3 handset manufacturers':
    st.image("top 3 manufacture.png")
    st.write("Focus on Apple Users: Since Apple leads in terms of handset users, ensure compatibility with Apple devices, iOS updates, and specific support for Apple services (iCloud, FaceTime, etc.")
    st.write("Strong Support for Samsung: Samsung devices are also prominent, meaning ensuring Android compatibility, especially with Samsung's custom features and software versions, is crucial.")
    st.write("Consider Huawei Users: Given Huawei’s unique software ecosystem (especially post-Google services restrictions), it’s important to provide dedicated support and updates for these devices.")

elif status is 'top 5 handsets per top 3 handset manufacturer':
    st.image("top 5 handset.png")
    st.write("Product development: Marketing teams can use this data to identify which handsets are most popular with consumers and focus on developing new products or features that meet those needs.")
    st.write("Marketing campaigns: This data can also be used to target marketing campaigns more effectively. For example, if a company is promoting a new smartphone, they could target their ads to users of the most popular handsets.")
    st.write("Sales and distribution: By understanding which handsets are in high demand, marketing teams can better manage their sales and distribution channels.")

else:
    st.warning("Please Select any option")

st.markdown(" ### ->> Click Checkbox to view Total Data Usage For Each App")
datausage = st.checkbox("Total Data Usage For Each App")

if datausage:
    
    st.image("total data usage each app.png")
    st.write("This bar chart shows the total data usage for different applications. The largest data usage is for gaming, followed by other_data, youtube, netflix, google, email, and social_media. The amount of data used by gaming is significantly higher than other applications. This graph shows that gaming and other_data usage contribute significantly to the total data usage.")
 
st.markdown(" ### ->> Compute a correlation matrix For Each App")
correlation = st.checkbox("Compute a correlation matrix")

if correlation:
    
    st.image("Application Data Correlation.png")
    st.write("Since users of services like YouTube, Netflix, and gaming tend to have higher overall data usage, promote premium plans with higher data caps to users who frequently engage with these services.")
  
st.markdown(" ### ->> Aggregate user total traffic per application")  
traffic = st.toggle("Compute a correlation matrix")

if traffic:
    
    st.image("top 10 most engaged users per application.png")
    st.write("This bar chart comparing the amount of data consumed by different internet services. It shows that the largest amount of data was consumed through Google services, followed by other data, email, and social media. The smallest amount of data was consumed by Netflix services.")

st.markdown(" ### --> Compute & list 10 of the top, bottom, and most frequent:")
option = st.selectbox(
    "Compute & list 10 of the top, bottom, and most frequent:",
    ("TCP values in the dataset", "RTT values in the dataset", "Throughput values in the dataset"),
    index=None,
    placeholder="Select to view values in the dataset...",
)
if option is "TCP values in the dataset":
    st.image("TCP values in the dataset..png")
    st.write("The top values are a list of the highest 10 TCP values, while the bottom values are the lowest 10. The most frequent values show the count of each unique TCP value, with the most frequent TCP values at the top of the chart.")

elif option is 'RTT values in the dataset':
    st.image("RTT values in the dataset..png")
    st.write("These charts provide insights into the distribution of RTT values in the dataset. For example, the 'RTT Top 10' chart highlights the outliers with the highest RTT values, while the 'RTT Most 10' chart shows the values that occur most frequently. This information can be useful for identifying potential issues or trends related to network performance.")
   
elif option is 'Throughput values in the dataset':
    st.image("Throughput values in the dataset..png")
    st.write("The leftmost plot shows the top 10 values, with the highest value being around 750k. The rightmost plot shows the most frequent values, with the highest frequency being around 7,500. The middle plot shows the last 10 values, with the values being very low.")
 
else:
    st.warning("Please Select any option")



st.markdown("""
<style>
    .stApp {
        background-color: #f0f0f0;
    }
    .st-emotion-cache-12fmjuu {
        background : none;
    }
    .st-emotion-cache-1gwvy71 {
    padding: 0px 3.5rem 6rem;
}
.st-emotion-cache-m78myu h1{
    color: #262730;
}
    .stHeader {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

