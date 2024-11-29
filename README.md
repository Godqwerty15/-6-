![image](https://github.com/user-attachments/assets/38ea3d05-4494-46fe-ad87-cb6fcb117b86)
![image](https://github.com/user-attachments/assets/559a5941-42d5-49ad-8037-48472edd7f24)
![image](https://github.com/user-attachments/assets/fed69302-ad8f-4a61-a050-db4d77d897b7)
![image](https://github.com/user-attachments/assets/b34a6f87-3b78-4c8c-8fb0-b1d599f46b1c)

module_a.py 코드 설명 및 실행 과정
1. 그래프를 그려야 하므로 matplotlib.pyplot 을 plt로 import한다.
2. 그래프의 크기를 가로 10, 세로 6으로 적당히 설정하고 plot으로 x축엔 표준점수, y축엔 각각 남자와 여자의 득점자 수를 담은 그래프를 따로 그리는 코드를 쓴다.
3. title은 2024학년도 수능의 name 과목의 과목분포를 쓴다.
4. 그리고 xlable과 ylabel에도 표준점수와 학생수를 달아준다.
5. plt.legend()로 각 그래프가 어떤 성별의 것인지 알 수 있도록 한 후에, plt.grid()로 격자도 추가하고 plt.show()로 최종 출력을 한다.

   
main.py 코드 설명 및 실행 과정
1. 코드 개요
이 코드는 2024학년도 수능 성적 데이터에서 특정 과목의 표준점수 분포를 시각화하는 프로그램이다. 사용자로부터 과목 이름을 입력받아 CSV 파일에서 데이터를 필터링하고, 선택된 과목의 남학생과 여학생의 분포를 비교하는 그래프를 생성한다.
2. 코드 단계별 설명
   2.1 모듈 및 라이브러리 불러오기
     1. module_a 모듈 가져오기: 
        import module_a
     2. 데이터 처리 및 시각화 라이브러리 불러오기:
        import pandas as pd
        import matplotlib.pyplot as plt
     3. 한글 폰트 설정:
        from matplotlib import rc
        rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
    2.2 데이터 처리 및 사용자 입력
      4. 사용자 입력
         name = input("표준점수 분포를 볼 과목을 선택하세요: ")
      5. CSV파일 읽기
         data = pd.read_csv('20231231.csv', encoding='EUC-KR')
      6. 선택된 과목 데이터 필터링
         korean_data = data[data['유형'] == name]
    2.3 그래프 시각화
      7. 그래프 그리기
        module_a.Graph_Drawing(korean_data['표준점수'], korean_data['남자'], korean_data['여자'], name)
3. 실행 결과
코드를 실행하면, 사용자 입력에 따라 선택한 과목의 표준점수 분포를 시각화한 그래프가 생성된다. 그래프에는 남학생과 여학생의 데이터가 각각 표시되며, 과목별 분포 차이를 시각적으로 확인할 수 있다.

4. 활용방안
이 프로그램은 선택 과목별 성적 분포를 비교하거나 분석하는 데 유용하다. 남학생과 여학생의 분포 차이를 한눈에 파악할 수 있어 데이터 분석 및 보고서 작성에 활용하기 적합하다.
