import module_a
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
name = input("표준점수 분포를 볼 과목을 선택하세요 : ")
data = pd.read_csv('20231231.CSV', encoding = 'EUC-KR')
korean_data = data[data['유형'] == name]
module_a.Graph_Drawing(korean_data['표준점수'],korean_data['남자'],korean_data['여자'],name)
