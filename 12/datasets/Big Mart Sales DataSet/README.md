## Big Mart Sales Data

### Introduction
The data scientists at BigMart have collected 2013 sales data for 1559 products across 10 stores in different cities. Also, certain attributes of each product and store have been defined. The aim is to build a predictive model and find out the sales of each product at a particular store. Using this model, BigMart will try to understand the properties of products and stores which play a key role in increasing sales. 

Please note that the data may have missing values as some stores might not report all the data due to technical glitches. Hence, it will be required to treat them accordingly.

### Data Dictionary

Column Position | Atrribute Name | Definition | Data Type | Example | % Null Ratios
 --- | --- | --- | --- | --- | ---
1 | Item_Identifier | It is a unique product ID assigned to every distinct item. It consists of an alphanumeric string of length 5 | Alphanumeric | FDN15 | 0
2 | Item_Weight | This field includes the wieght of the product | Numeric (float) | 17.5 | 17.16531738
3 | Item_Fat_Content | This attribute is categorical and describes whether the product is low fat or not. There are 2 categories of this attribute: ['Low Fat', 'Regular']. However, it is important to note that 'Low Fat' has also been written as 'low fat' and 'LF' in dataset, whereas, 'Regular' has been referred as 'reg' as well | Alpha | Low Fat | 0
4 | Item_Visibility | This field mentions the percentage of total display area of all products in a store allocated to the particular product | Numeric (float) | 0.01676 | 0
5 | Item_Type | This is a categorical attribute and describes the food category to which the item belongs. There are 16 different categories listed as follows: ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household', 'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 'Health and Hygiene', 'Hard Drinks', 'Canned', 'Breads', 'Starchy Foods', 'Others', 'Seafood'] | Alpha | Meat | 0
6 | Item_MRP | This is the Maximum Retail Price (list price) of the product | Numeric (float) | 141.618 | 0
7 | Outlet_Identifier | It is a unique store ID assigned. It consists of an alphanumeric string of length 6 | Alphanumeric | OUT049 | 0
8 | Outlet_Establishment_Year | This attribute mentions the year in which store was established | Numeric (Integer) | 1998 | 0
9 | Outlet_Size | The attribute tells the size of the store in terms of ground area covered. It is a categorical value and described in 3 categories: ['High', 'Medium', 'Small'] | Alpha | Medium | 28.27642849
10 | Outlet_Location_Type | This field has categorical data and tells about the size of the city in which the store is located through 3 categories: ['Tier 1', 'Tier 2', 'Tier 3'] | Alpha | Tier 3 | 0
11 | Outlet_Type | This field contains categorical value and tells whether the outlet is just a grocery store or some sort of supermarket. Following are the 4 categories in which the data is divided: ['Supermarket Type1', 'Supermarket Type2', 'Grocery Store','Supermarket Type3'] | Alpha | Supermarket Type2 | 0
12 | Item_Outlet_Sales | This is the outcome variable to be predicted. It contains the sales of the product in the particulat store | Numeric (float) | 2097.27 | 0


### Source:
https://datahack.analyticsvidhya.com/contest/practice-problem-big-mart-sales-iii/