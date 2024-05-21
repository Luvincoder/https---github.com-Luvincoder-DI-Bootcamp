import pandas as pd


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')


print("First 10 rows of 'chipo':")
print(chipo.head(10))


total_rows = chipo.shape[0]
print("\nTotal number of entries in 'chipo':", total_rows)


total_columns = chipo.shape[1]
print("\nTotal number of columns in 'chipo':", total_columns)


print("\nColumn names in 'chipo':")
print(chipo.columns)


print("\nIndex of 'chipo':")
print(chipo.index)


most_ordered_item = chipo['item_name'].value_counts().idxmax()
print("\nMost ordered item:", most_ordered_item)


total_items_ordered = chipo['quantity'].sum()
print("\nTotal number of items ordered:", total_items_ordered)


most_ordered_choice = chipo['choice_description'].value_counts().idxmax()
print("\nMost ordered choice description:", most_ordered_choice)


chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x.replace('$', '')))


total_revenue = chipo['item_price'].sum()
print("\nTotal revenue:", total_revenue)


total_orders = chipo['order_id'].nunique()
print("\nTotal number of orders:", total_orders)


average_order_value = total_revenue / total_orders
print("\nAverage order value:", average_order_value)


unique_items_sold = chipo['item_name'].nunique()
print("\nTotal number of unique items sold:", unique_items_sold)