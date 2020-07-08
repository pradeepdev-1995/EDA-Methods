import pandas as pd
import sweetviz
train = pd.read_csv("house_train.csv")
test = pd.read_csv("house_test.csv")
train_report = sweetviz.analyze([train, "Train"],target_feat='SalePrice')
train_report.show_html('Report.html')

#comparing two data frames
compare_report = sweetviz.compare([train, "Train"], [test, "Test"], "SalePrice")
compare_report.show_html('Comparison Report.html')