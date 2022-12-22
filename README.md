<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=K-Means_Clustering_App&fontSize=60" />
</div>

<div align=center>
	<h3> 📌프로젝트 명📌 <h3>
	<h4> K-Means Clustering Web dashboard 개발 <h4>
	<h6> CSV 파일을 업로드하면 해당 CSV 데이터를 바탕으로 데이터를 n개의 클러스터로 묶는 알고리즘 K-Means,<h6>
	<h6> K-Means로 묶은 데이터를 그룹별로 분석, 저장할 수 있는 웹 대시보드 개발 <h6>
	<br>
	<h4>
	
👉웹대시보드 주소 <http://ec2-3-38-117-95.ap-northeast-2.compute.amazonaws.com:8502/>

</div>	
<div align=center> 
	<br>
	<br>
	<h3> 프로젝트 구성📋 <h3>
	<h4> CSV파일 업로드 : CSV파일을 업로드할 수 있는 기능 설정
	<h4> 데이터 확인 : 수치로 되어있는 데이터를 한번에 확인 할 수 있으며, nan값을 확인하여 제거할 수 있다
	<h4> X컬럼 설정 : X로 사용할 컬럼을 지정하면 문자열컬럼은 자동으로 인코딩된다, 피처스케일링을 할수도 있다
	<h4> 클러스터링 갯수 선택 : WCSS의 엘보우메소드 차트를 보고 그룹갯수를 선택할 수 있다
	<h4> 그룹별로 조회 : K-Means Clustering 완료된 그룹별로 데이터를 조회하거나 통계할 수 있다
	<h4> 데이터 저장 : K-Means Clustering 완료된 데이터를 새로운 CSV파일로 저장할 수 있다
	<br>
	<br>
	<br>
	<h3> 사용한 라이브러리✏️ <h3>	
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white" />
	<img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=NumPy&logoColor=white" />
	<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white" />
	<br>
	<img src="https://img.shields.io/badge/MinMaxScaler-000000?style=flat&logo=&logoColor=white" />
	<img src="https://img.shields.io/badge/LabelEncoder-000000?style=flat&logo=&logoColor=white" />
	<img src="https://img.shields.io/badge/OneHotEncoder-000000?style=flat&logo=&logoColor=white" />
	<img src="https://img.shields.io/badge/ColumnTransformer-000000?style=flat&logo=&logoColor=white" />
	<img src="https://img.shields.io/badge/KMeans-000000?style=flat&logo=&logoColor=white" />
	<h3> 사용한 Tools🔨 <h3>
	<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=Jupyter&logoColor=white" />
	<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=Visual Studio Code&logoColor=white" />
	<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white" />
	<br>
	<br>
</div>	

		
---


<h3>진행과정💬<h3>

<h4>Jupyter Notebook에서 데이터 분석<h4>
	
<h5>  <h5>

- 샘플 데이터 파일을 가져와서 Nan데이터 값이 있으면 예측이 안되므로 Nan값 제거
- X로 사용할 컬럼의 데이터 타입 파악해서 문자열 데이터가 있는지 확인
- 문자열 데이터가 있으면 예측이 잘 되지않으므로 반복문을 사용해 카테고리컬 데이터 갯수조건을 걸어 레이블, 원핫 인코딩 실행
- 정확한 분류를 위해 인코딩 실행한 데이터 피처스케일링
- KMeans에 예측시키고 결과값 저장해서 새로운 컬럼 생성
- 예측한 새로운 컬럼을 활용해 데이터 엑세스
- 몇개의 그룹으로 묶을지 추천받기 위해 WCSS엘보우 멧소드 차트 추가

<h4>Visual Studio Code에서 Streamlit 라이브러리로 작업<h4>

<h5>메인 앱 화면 생성<h5>
	
- CSV 파일을 업로드할 수 있게 file uploader 기능 설정 (업로드하지 않을 경우 기본 테스트 파일로 보여주기 설정)
- 불러온 CSV파일이 Unnamed: 0일 경우 처리하는 기능 설정
- 불러온 파일의 수치데이터를 확인할 수 있는 데이터프레임 표시
- 수치데이터를 확인하고 0으로 채워져있는 데이터를 컬럼별로 nan값으로 변경하는 기능 설정
- nan값 확인해서 제거하는 기능 설정
- 불러온 데이터의 컬럼들 중 X로 지정할 컬럼 선택 기능 설정
- X로 지정한 데이터 중 문자열 데이터가 있을 경우 자동으로 레이블, 또는 원핫 인코딩 실행
- X데이터 피처스케일링 기능 설정
- 몇개의 그룹으로 묶을지 파악하기 위해 WCSS 엘보우메소드 차트 추가
- 원하는 그룹 갯수 지정 기능 설정
- 지정한 그룹별로 새로운 컬럼 Group 추가
- Group 컬럼으로 각 그룹의 데이터 조회 기능 설정
- K-Means Clustering이 완료된 데이터를 새로운 CSV파일로 저장할 수 있다


	
---
	
	
![1](https://user-images.githubusercontent.com/120348555/208817728-37a32c71-b7e5-4a11-8d31-d0f534581a15.PNG)
![2](https://user-images.githubusercontent.com/120348555/208817771-5730fbe8-3586-41cf-beef-d266171143e3.PNG)
![3](https://user-images.githubusercontent.com/120348555/208817791-524fd50d-5d28-40ed-ac13-8d790894850f.PNG)
