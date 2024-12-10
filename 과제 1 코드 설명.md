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

1. module_a 모듈을 가져오기
사용자 정의 모듈 module_a를 import하여 그래프 생성 함수 사용한다.
2. pandas, matplotlib 가져오기
데이터 처리와 시각화를 위해 pandas와 matplotlib.pyplot을 import
3. 한글 폰트 설정
맑은 고딕 폰트를 설정하고, 음수 기호(-)가 제대로 표시되도록 설정한다.
4. 사용자 입력 받기
과목 이름을 입력 받아 name 변수에 저장한다.
5. CSV 파일 읽기
20231231.csv 파일을 읽어 데이터 프레임에 저장(EUC-KR 인코딩 사용함).
6. 데이터 필터링
입력받은 과목 이름(name)에 해당하는 데이터 필터링
7. 그래프 시각화
필터링된 데이터를 활용하여 남학생과 여학생의 표준점수 분포 그래프 생성.
