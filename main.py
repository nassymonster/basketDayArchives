# Import needed libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
from scipy.stats import gmean
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Request data
    print(f"Step 1")
    webpage = requests.get("https://www.opec.org/basket/basketDayArchives.xml")
    data_xml = webpage.content
    # Create a BeautifulSoup object
    soup = BeautifulSoup(data_xml, 'xml')
    # Extract data and assign it to a Dataframe
    basket_lists = soup.find_all("BasketList")
    rows = []
    for basket_list in basket_lists:
        row = {
            'data': datetime.strptime(basket_list['data'], '%Y-%m-%d').date(),
            'val': float(basket_list['val'])
        }
        rows.append(row)
    basket_list_df = pd.DataFrame.from_records(rows)

    # Step 1 Save DataFrame to csv
    basket_list_df.to_csv('results/basketDayArchives.csv', encoding='utf-8', index=False)
    print(f"CSV saved to results/basketDayArchives.csv")

    # Step 2
    # Add columns 'Percentage Daily Movement' and 'Percentage Price Change'
    print(f"Step 2")
    basket_list_df.sort_values(by='data')
    basket_list_df_computed = basket_list_df.copy(deep=True)
    basket_list_df_computed['Percentage Daily Movement'] = basket_list_df_computed['val'].pct_change()
    # I use the first value in the period for the calculation 'Percentage Price Change'
    basket_list_df_computed['Percentage Price Change'] = (
            (basket_list_df_computed['val'] - basket_list_df_computed['val'].iloc[0]) /
            basket_list_df_computed['val'].iloc[0])
    # Save DataFrame to csv
    basket_list_df_computed.to_csv('results/basketDayArchivesComputed.csv', encoding='utf-8', index=False)
    print(f"CSV saved to results/basketDayArchivesComputed.csv")

    # Step 3.1 - Plot of the Percentage Price Change for the entire period
    print(f"Step 3.1")
    basket_list_df_computed['Percentage Price Change'] = basket_list_df_computed['Percentage Price Change'].apply(
        lambda row: row * 100)
    price_change_all_plot = sns.lineplot(
        x="data",
        y="Percentage Price Change",
        data=basket_list_df_computed
    ).set(xlabel='Year',
          ylabel='Percentage Price Change (%)',
          title='Plot of the Percentage Price Change for the entire period')
    plt.savefig("results/charts/plotPercentagePriceChange.png")
    plt.clf()
    print(f"Result saved to results/charts/plotPercentagePriceChange.png")

    # Step 3.2 - Plots with the percentage development of the price over the years
    print(f"Step 3.2")
    basket_list_df_computed['Year'] = pd.DatetimeIndex(basket_list_df_computed['data']).year
    years = basket_list_df_computed.drop_duplicates(subset=["Year"], keep='first')
    for index, first_row in years.iterrows():
        year_str = str(first_row["Year"])
        print(f"Working on percentage price change per year {year_str}")
        df_per_year = basket_list_df_computed[basket_list_df_computed['Year'] == first_row['Year']].copy(deep=True)
        df_per_year['Yearly Percentage Price Change'] = (df_per_year['val'] - first_row["val"]) / first_row["val"] * 100
        price_change_plot_year = sns.lineplot(
            x="data",
            y="Yearly Percentage Price Change",
            data=df_per_year
        ).set(xlabel='Dates',
              ylabel='Percentage Price Change (%)',
              title=f'Plot of the Percentage Price Change for year {year_str}')
        plt.savefig(f"results/charts/plotPercentagePriceChange_{year_str}.png")
        plt.clf()
    print(f"Results saved to results/charts/plotPercentagePriceChange_xxxx.png")

    # Step 4 - Average Percentage Daily Movement per year
    print(f"Step 4")
    gmean_df = basket_list_df_computed.copy(deep=True)
    gmean_df = gmean_df.iloc[1:, :]
    gmean_df['Percentage Daily Movement'] = gmean_df['Percentage Daily Movement'] + 1
    gmean_df_series = gmean_df.groupby('Year')['Percentage Daily Movement'].apply(gmean) - 1
    gmean_df_fin = pd.DataFrame(
        {'Year': gmean_df_series.index, 'Average Percentage Daily Movement': gmean_df_series.values})
    gmean_df_fin['Average Percentage Daily Movement'] = gmean_df_fin['Average Percentage Daily Movement'] * 100
    # Save DataFrame to csv
    gmean_df_fin.to_csv('results/basketDayArchivesGeomMean.csv', encoding='utf-8', index=False)
    print(f"Result saved to results/basketDayArchivesGeomMean.csv")

    # Step 5 - Plot of the Average Percentage Daily Movement
    print(f"Step 5")
    daily_movement_plot = sns.barplot(
        x="Year",
        y="Average Percentage Daily Movement",
        data=gmean_df_fin
    ).set(xlabel='Years',
          ylabel='Average Percentage Daily Movement (%)',
          title='Plot of the Average Percentage Daily Movement')
    plt.xticks(rotation=90)
    plt.savefig(f"results/charts/plotAveragePercentageDailyMovement.png")
    plt.clf()
    print(f"Result saved to results/charts/plotAveragePercentageDailyMovement.png")
