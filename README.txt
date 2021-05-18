1. Run "dataClean.py" on raw Billboard and Song Attributes data to generate input data (billboard_input1.csv).
2. Run "getYahooSP500.py" to obtain S&P 500 closing index values from 1999-2020 (sp500_1999_2020.csv).
3. Run "getLabel.py" on outputs from 1 and 2 to obtain "yLabel.csv".
4. Run "billboardLSTM.py" on "billboard_input1.csv" and "yLabel.csv" to generate outputs.

The maximum accuracy achieved by using tanh or ReLu activation functions with different regularizers is around 60%.
