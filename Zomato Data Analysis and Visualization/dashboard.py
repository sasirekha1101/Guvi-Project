import pandas as pd
import streamlit as st
import plotly.express as px

# Load Zomato dataset
zomato_url = "https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/zomato.csv"
zomato_data = pd.read_csv(zomato_url)

# Load Country Code data
country_code_url = "https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/Country-Code.xlsx"
country_codes = pd.read_excel(country_code_url)

# Merge zomato data with country codes to get full country names
zomato_full = pd.merge(zomato_data, country_codes, on='Country Code')

# Define currency conversion rates
conversion_rates = {
    'Dollar($)': 74.85,
    'Pounds(£)': 94.50,
    'Indian Rupees(Rs.)': 1,
    'Brazilian Real(R$)': 15.76,
    'Emirati Dirham(AED)': 20.37,
    'Qatari Rial(QR)': 20.55,
    'Turkish Lira(TL)': 4.53,
    'Rand(R)': 4.90,
    'Botswana Pula(P)': 6.45,
    'Sri Lankan Rupee(LKR)': 0.37,
    'Indonesian Rupiah(IDR)': 0.0052,
    'New Zealand Dollar($)': 48.34
}

# Convert prices to Indian Rupees
zomato_full['Price in Rupees'] = zomato_full.apply(
    lambda x: x['Average Cost for two'] * conversion_rates.get(x['Currency'], 1), axis=1)
df = zomato_full
st.title('Zomato Data Analysis Dashboard')
country = st.sidebar.selectbox('Select a Country', zomato_full['Country'].unique())
filtered_data = df[df['Country'] == country]


st.header(f"Top 10 Popular Cuisines in {country}")
cuisines_count = filtered_data['Cuisines'].value_counts().nlargest(10)
fig_cuisines = px.bar(cuisines_count, x=cuisines_count.index, y=cuisines_count.values, labels={'x': 'Cuisine', 'y': 'Number of Restaurants'}, title="Top 10 Cuisines", color_discrete_sequence=px.colors.sequential.Agsunset)
st.plotly_chart(fig_cuisines, use_container_width=True)

# Display average ratings
st.header(f"Average Ratings in {country}")
average_ratings = filtered_data.groupby('Restaurant Name')['Aggregate rating'].mean().nlargest(10)
fig_ratings = px.bar(average_ratings, x=average_ratings.index, y=average_ratings.values, labels={'x': 'Restaurant', 'y': 'Average Rating'}, title="Top Rated Restaurants", color_discrete_sequence=px.colors.sequential.Magenta)
st.plotly_chart(fig_ratings, use_container_width=True)


# Additional Section for Costly Cuisines in India
if country == 'India':
    st.header("Which Cuisines are Costly in India?")
    # Filter Indian cuisine data
    indian_cuisines = df[df['Country'] == 'India']
    # Compute average cost for cuisines
    costly_cuisines = indian_cuisines.groupby('Cuisines')['Average Cost for two'].mean().nlargest(10)
    fig_costly_cuisines = px.bar(costly_cuisines, x=costly_cuisines.values, y=costly_cuisines.index, orientation='h', labels={'x': 'Average Cost for Two', 'y': 'Cuisine'}, title="Costliest Cuisines in India", color_discrete_sequence=px.colors.sequential.Tealgrn)
    st.plotly_chart(fig_costly_cuisines, use_container_width=True)


# Sidebar for city selection within the selected country
cities = filtered_data['City'].unique()
city = st.sidebar.selectbox('Select a City', cities)

city_data = filtered_data[filtered_data['City'] == city]
st.header('Filter Based on City')
# Display famous cuisine in the city
cuisines_count = city_data['Cuisines'].value_counts().nlargest(10)
fig_popular_cuisines = px.bar(cuisines_count, x=cuisines_count.values, y=cuisines_count.index, orientation='h', labels={'x': 'Number of Restaurants', 'y': 'Cuisine'}, title="Popular Cuisines in " + city, color_discrete_sequence=px.colors.sequential.Redor)
st.plotly_chart(fig_popular_cuisines, use_container_width=True)

# Display costlier cuisine
costly_cuisines = city_data.groupby('Cuisines')['Average Cost for two'].mean().nlargest(10)
fig_costly_cuisines = px.bar(costly_cuisines, x=costly_cuisines.values, y=costly_cuisines.index, orientation='h', labels={'x': 'Average Cost for Two', 'y': 'Cuisine'}, title="Costlier Cuisines in " + city, color_discrete_sequence=px.colors.sequential.Purp)
st.plotly_chart(fig_costly_cuisines, use_container_width=True)

# Rating count based on rating text
ratings_count = city_data['Rating text'].value_counts()
fig_ratings_count = px.pie(ratings_count, values=ratings_count.values, names=ratings_count.index, title="Rating count in the city", color_discrete_sequence=px.colors.sequential.GnBu)
st.plotly_chart(fig_ratings_count, use_container_width=True)

# Online delivery vs dine-in pie chart
delivery_data = city_data['Has Online delivery'].value_counts()
delivery_labels = ['Online Delivery' if x == 'Yes' else 'No Online Delivery' for x in delivery_data.index]
fig_delivery = px.pie(delivery_data, values=delivery_data.values, names=delivery_labels, title="Online Delivery vs Dine-in", color_discrete_sequence=px.colors.sequential.Pinkyl_r)
st.plotly_chart(fig_delivery, use_container_width=True)

if country == "India":
    st.header("Comparisons Among Cities in India")

    # Group data by city
    indian_cities = filtered_data[filtered_data['Country'] == 'India']
    city_group = indian_cities.groupby('City')

    # Spending on online delivery
    online_delivery_cost = city_group.apply(lambda x: x[x['Has Online delivery'] == 'Yes']['Average Cost for two'].mean())
    fig_online = px.bar(online_delivery_cost.dropna(), title="Average Spending on Online Delivery by City", color_discrete_sequence=px.colors.sequential.Mint_r)
    st.plotly_chart(fig_online, use_container_width=True)

    # Spending on dine-in
    dine_in_cost = city_group.apply(lambda x: x[x['Has Online delivery'] == 'No']['Average Cost for two'].mean())
    fig_dine_in = px.bar(dine_in_cost.dropna(), title="Average Spending on Dine-In by City", color_discrete_sequence=px.colors.sequential.Inferno)
    st.plotly_chart(fig_dine_in, use_container_width=True)

    # Living cost comparison
    average_cost = city_group['Average Cost for two'].mean()
    fig_living_cost = px.bar(average_cost, title="Average Living Cost by City", color_discrete_sequence=px.colors.sequential.Sunset)
    st.plotly_chart(fig_living_cost, use_container_width=True)