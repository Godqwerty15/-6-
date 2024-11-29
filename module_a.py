import matplotlib.pyplot as plt

def Graph_Drawing(x_values,male_scores,female_scores,name):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, male_scores, label='남자')
    plt.plot(x_values, female_scores, label='여자')
    plt.title('2024학년도 수능 %s 과목분포'%name)
    plt.xlabel('표준점수')
    plt.ylabel('학생 수')
    plt.legend()
    plt.grid(True)
    plt.show()
