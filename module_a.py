import matplotlib.pyplot as plt

#그래프 출력 함수
def Graph_Drawing(x_values,male_scores,female_scores):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, male_scores, label='남자')
    plt.plot(x_values, female_scores, label='여자')
    plt.title('남자와 여자 국어 성적의 표준점수 분포')
    plt.xlabel('표준점수')
    plt.ylabel('학생 수')
    plt.legend()
    plt.grid(True)
    plt.show()
