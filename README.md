# Zomato Data Analysis and Visualization #

Zomato is a leading global platform for restaurant discovery and food delivery. This project aims to perform in-depth data analysis on Zomato's operational data to uncover insights into consumer behavior, preferences, and emerging trends in the restaurant industry. Leveraging Python, Pandas for data manipulation, and Plotly for interactive visualizations, this analysis will assist stakeholders like restaurateurs and investors in making informed decisions.

## Skills Developed
- Python scripting
- Data manipulation using Pandas
- Data visualization with Plotly
- Interactive dashboard creation using Streamlit Cloud Platform

## Domain
Data Analysis and Visualization

## Data Sources
- Zomato dataset: [zomato.csv](https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/zomato.csv)
- Country ISO codes: [Country-Code.xlsx](https://github.com/nethajinirmal13/Training-datasets/blob/main/zomato/Country-Code.xlsx)

## Problem Statement
The food industry continuously evolves, driven by changing consumer preferences and competitive dynamics. Analyzing Zomato's comprehensive data set provides insights into customer preferences, popular and costly cuisines, and geographical trends in food delivery and dining habits. These insights are crucial for strategic decisions in menu planning, pricing strategies, and marketing for stakeholders across the food industry.

## Project Approach
This project is structured into three main tasks, each designed to progressively build upon the previous to create a comprehensive and interactive analysis of Zomato's extensive dataset. The tasks are defined as follows:

The initial phase of the project focuses on preparing and enhancing the data to facilitate in-depth analysis:
- **Currency Normalization**: Add a new column to the dataset that converts various global currencies to Indian Rupees based on the latest exchange rates. This normalization allows for consistent and comparative cost analysis across different countries.
- **Data Cleaning**: Identify and correct anomalies in the data, such as missing values, duplicate records, and incorrect entries, to ensure accuracy in the analysis.
- **Feature Engineering**: Develop new features that could provide additional insights, such as calculating the average cost per meal, or categorizing restaurants by price range.
- **Comparative Analysis**: Create visualizations to compare the economic value of currencies and pricing strategies across different countries where Zomato operates.

The second task involves creating an interactive dashboard to visually represent the data insights:
- **Country Selection Dropdown**: Implement a dropdown menu in the dashboard that allows users to filter the dataset for a specific country's data.
- **Interactive Charts**: Develop various interactive charts, including bar charts for cuisine popularity, line graphs for price trends over time, and scatter plots for user ratings versus restaurant prices.
- **City-Specific Filters**: Add options to filter data by cities within the selected country, enabling more localized analysis.
- **Cuisine Analysis**: Provide insights into which cuisines are most popular and most expensive in selected cities or countries.
- **Performance Metrics Visualization**: Use pie charts and histograms to show the distribution of online orders versus dine-in preferences, and compare these across different regions or cities.

The final phase of the project focuses on making the dashboard accessible to users:
- **Web Hosting**: Deploy the dashboard to a web server using a platform like streamlit cloud platform. Ensure the server can handle expected user traffic and data load.

## Conclusion
Upon completion, this project will not only demonstrate a proficient use of data analysis and visualization techniques but will also provide actionable insights through a dynamic and interactive platform. These insights will be invaluable for stakeholders aiming to understand market trends, optimize operations, and tailor strategic decisions within the restaurant and food delivery industry.

## Acknowledgements
- Data provided by Zomato
- Dataset links provided by [Nethaji Nirmal](https://github.com/nethajinirmal13)

