This is a final project developped for NYU's course CSCI-GA-2565: Machine Learning.

Team members: Gary (Yu Yao) Hsu and Tina (Ting-Hsuan) Yuan

How to run:
1. Run "dataClean.py" on raw Billboard and Song Attributes data to generate input data (billboard_input1.csv).
2. Run "getYahooSP500.py" to obtain S&P 500 closing index values from 1999-2020 (sp500_1999_2020.csv).
3. Run "getLabel.py" on outputs from 1 and 2 to obtain "yLabel.csv".
4. Run "billboardLSTM.py" on "billboard_input1.csv" and "yLabel.csv" to generate outputs.

The maximum accuracy achieved by using tanh or ReLu activation functions with different regularizers is around 60%. Please see "2565_ML_Project.pdf" for complete project report.
