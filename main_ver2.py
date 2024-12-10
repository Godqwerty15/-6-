import module_a_ver2
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
year = int(input("남녀 표준점수 산점도를 확인할 년도를 고르시오 : "))
if(year > 2024 or year < 2021):
    print(f"{year}년도 수능 표준점수 데이터가 없습니다.")
    exit()
data = pd.read_csv(f'과제\과제 6. 팀프로젝트 (Ver 2.0)\{year-1}1231.CSV', encoding = 'EUC-KR')
subjects = data['유형']
unique_subjects = subjects.unique().tolist()
print("표준점수를 볼 수 있는 과목 목록 : ",end='')
print(unique_subjects)
name = input("표준점수 분포를 볼 과목을 선택하세요 : ")
korean_data = data[data['유형'] == name]
module_a_ver2.Graph_Drawing(korean_data['표준점수'],korean_data['남자'],korean_data['여자'],name,year)
