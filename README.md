# Derviative-Slopes

The main script generates a random data set, in this case I am simulating the daily temperature over a number of days.

The slope is calculated for a derivative using the rise over run formula, where x1,y1 are set by the fibonacci sequence, and x2,y2 are always fixed on the most recent X,Y. 

The amount of fibonacci levels is dynamically calculated based on the size of the dataset.

Then an average slope is calulated, where each slope has a unique weight. 

$$ Future plans $$

> Use a machine learning method with auto-tune to find the best weights for the average calculation.

> Import real data. 

> Test on stock market historical data.

The end goal is to have a reliable tool that can be used to add certainty to investment decisons and will use machine learning to calculate a slope for short term, mid term, and long term decions.

By using this side-by-side with statistical analysis, data visualization, and more mL, correlation can be calculated by oberserving slope change next to deviation in price. 

Further on, a trading algorithim itself could be built and tested with this functionality. Using a machine learning method to Identity buy/sell events upon changes in the short-mid-long term slopes relationships to eachother. 
