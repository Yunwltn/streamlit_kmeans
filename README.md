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
	<h3> 프로젝트 메뉴 구성📋 <h3>
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
	
- 데이터 파일을 가져와서 사용할 컬럼만 엑세스한 후 컬럼명 변경
- Nan데이터 값이 있으면 지도를 만들 때 에러가 발생하므로 Nan값 제거
- 차트로 보여줄 데이터 분석(월, 연령, 지역별 데이터)
- 입력받은 값으로 지도를 표시할 수 있게 데이터 엑세스

<h4>Visual Studio Code에서 Streamlit 라이브러리로 작업<h4>

<h5>1. 메인 앱 화면 생성<h5>
		
<h5>2. 파일을 새로 만들어 분석한 독서량 파일 작업<h5>
		
- 데이터 분석한 도서관 평균 독서율을 월별, 연령대별 평균으로 streamlit차트로 표시
- 각 월별로 해당 월의 연령대 독서율을 볼 수 있게 plotly차트로 표시	
- 전국 연령대별 회원수와 대출건수를 비교하여 볼 수 있게 plotly차트로 표시	
- 지역별 평균독서량, 회원수, 대출건수를 한번에 볼 수 있게 plotly차트로 표시	
- 지역별로 세부데이터(연령, 회원수, 대출건수)를 볼 수 있게 입력받은 지역의 데이터프레임 표시

<h5>3. 파일을 새로 만들어 분석한 도서관정보 파일로 작업<h5>
		
- 전국에 위치한 도서관의 갯수를 plotly bar차트와 데이터프레임으로 표시	
- 도서관명으로 검색할 수 있는 검색기능 설정(검색시 데이터프레임으로 표시)	
- 지역과 세부지역을 선택하여 그 지역의 도서관 정보를 볼 수 있는 지도와	
- 선택한 지역에 있는 도서관의 총 갯수를 나타낸 plotly bar차트 표시

	
---
	
	
![1](https://user-images.githubusercontent.com/120348555/208594875-455afcf5-4d5c-43d1-98f7-456af492d932.PNG)
![2](https://user-images.githubusercontent.com/120348555/208594950-50b6cb16-e6ad-462f-9f06-9fd2fa1ba4b0.PNG)
