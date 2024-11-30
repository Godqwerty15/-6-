import module_a
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_csv('20231231.CSV', encoding = 'EUC-KR')
subjects = data['유형']
unique_subjects = subjects.unique().tolist()
print("표준점수를 볼 수 있는 과목 목록 : ",end='')
print(unique_subjects)
name = input("표준점수 분포를 볼 과목을 선택하세요 : ")
korean_data = data[data['유형'] == name]
module_a.Graph_Drawing(korean_data['표준점수'],korean_data['남자'],korean_data['여자'],name)
print(korean_data['남자'])
