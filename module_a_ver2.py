import matplotlib.pyplot as plt

def Graph_Drawing(x_values, male_scorers, female_scorers, name,year):
    plt.figure(figsize=(10, 6))
    
    # 산점도 그리기
    plt.scatter(x_values, male_scorers, label='남자', alpha=0.7)  # 남자 데이터 산점도
    plt.scatter(x_values, female_scorers, label='여자', alpha=0.7, color='orange')  # 여자 데이터 산점도
    
    plt.title(f'{year}학년도 수능 {name} 과목 분포')
    plt.xlabel('표준점수')
    plt.ylabel('학생 수')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()




