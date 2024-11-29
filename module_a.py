import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False


data = pd.read_csv('20231231.csv', encoding = 'EUC-KR')
korean_data = data[data['영역'] == '국어']
x_values = korean_data['표준점수']
male_scores = korean_data['남자']
female_scores = korean_data['여자']

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(x_values, male_scores, label='남자')
plt.plot(x_values, female_scores, label='여자')

# 그래프에 라벨 추가
plt.title('남자와 여자 국어 성적의 표준점수 분포')
plt.xlabel('표준점수')
plt.ylabel('학생 수')
plt.legend()

# 그래프 표시
plt.grid(True)
plt.show()

