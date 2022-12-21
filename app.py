from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import streamlit as st
import pandas as pd
import numpy as np


def main() :
    st.title('K-Means Clustering')
    st.write('K-means clustering은 주어진 데이터를 k개의 클러스터로 묶는 알고리즘입니다')
    st.write('')

    # csv 파일 업로드
    st.subheader(':cloud: CSV 파일 업로드 :cloud:')
    file = st.file_uploader('CSV 파일 업로드', type=['csv'])
        
    # 업로드한 csv 파일을 데이터프레임으로 읽기
    if file is not None :
        if st.checkbox('불러온 파일이 Unnamed: 0일 경우 클릭 해주세요') :
            df = pd.read_csv(file, index_col=0)
            st.success('CSV파일이 업로드 되었습니다')
            st.dataframe(df)
        else :
            df = pd.read_csv(file)
            st.success('CSV파일이 업로드 되었습니다')
            st.dataframe(df)

        # 비어있는 데이터 확인하고 있으면 제거하기
        st.subheader('')
        st.subheader('수치 데이터 확인하기 :memo:')
        st.dataframe(df.describe())

        if st.checkbox('0 데이터로 채워져 있는 값을 nan값으로 변경하기') :
            column_list1 = df.columns
            selected_column1 = st.multiselect('원하는 컬럼을 선택하세요', column_list1)
            df = df[selected_column1] = df[selected_column1].replace(0, np.nan)
            if len(selected_column1) != 0 :
                st.dataframe(df.isna().sum())
                st.success('0 데이터가 nan값으로 변경 되었습니다')

        if st.checkbox('nan값 확인하기') :
            st.dataframe(df.isna().sum())
            if st.checkbox(':warning: nan값 모두 제거하기 :warning:') :
                df = df.dropna()
                st.dataframe(df.isna().sum())
                st.success('nan값이 모두 제거되었습니다')

        # KMeans 클러스터링을 하기 위해 X로 사용할 컬럼을 설정
        st.subheader('')
        st.subheader('X로 사용할 컬럼 설정 :pushpin:')
        column_list2 = df.columns
        selected_column2 = st.multiselect('X로 사용할 컬럼을 선택하세요', column_list2)

        if len(selected_column2) != 0 :
            X = df[selected_column2]
            st.dataframe(X)

            # 문자열 컬럼 처리
            X_new = pd.DataFrame()

            for name in X.columns : 
                data = X[name]
            if data.dtype == object :
                if data.nunique() <= 2 :
                    label_encoder = LabelEncoder()
                    X_new[name] = label_encoder.fit_transform(data)
                else :
                    ct = ColumnTransformer( [('encoder', OneHotEncoder(), [0])], remainder= 'passthrough' )
                    col_names = sorted( data.unique() )
                    X_new[ col_names ] = ct.fit_transform( data.to_frame() )
            else :
                X_new[name] = data

            # X값 피처스케일링
        if st.checkbox('Data Feature Scaling') :  
            m_scaler_x = MinMaxScaler()
            X_new = m_scaler_x.fit_transform(X_new)

        # WCSS를 확인하기 위한 그룹의 갯수 정하기
        st.subheader('')
        st.subheader('클러스터링 갯수 선택 :pushpin:')
        st.info('WCSS로 그룹 갯수를 추천받아보세요!')
        if st.checkbox('WCSS로 추천받기'):
            max_number = st.slider('WCSS를 확인하기 위한 최대 그룹 갯수 선택', 2, 20, value=10)
            if len(selected_column2) == 0 :
                st.write('')
            else :
                wcss = []
                for k in np.arange(1, max_number+1) :
                    kmeans = KMeans(n_clusters= k, random_state= 5)
                    kmeans.fit(X_new)
                    wcss.append( kmeans.inertia_ )

            x = np.arange(1, max_number+1)
            fig1 = plt.figure()
            plt.plot(x, wcss)
            plt.title('The Elbow Method')
            plt.xlabel('Number of Clusters')
            plt.ylabel('WCSS')
            st.pyplot(fig1)

        # 실제로 그룹핑할 갯수 선택
        if len(selected_column2) != 0 :
            k = st.number_input('그룹갯수 결정', 1, 20)

            kmeans = KMeans(n_clusters= k, random_state= 5)
            y_pred = kmeans.fit_predict(X_new)
            df['Group'] = y_pred
            df = df.sort_values('Group')
            st.dataframe(df)

            # 그룹한 데이터별로 조회
            st.subheader('')
            st.subheader('그룹별로 조회하기 :mag:')
            if len(selected_column2) != 0 :
                column_list3 = df['Group'].unique().tolist()
                selected_column3 = st.selectbox('그룹 번호를 선택하세요', column_list3)
                dfgroup = df.loc[ df['Group'] == selected_column3 ]
                st.dataframe(dfgroup)

                if st.checkbox('해당 그룹 통계 데이터 보기'):
                    st.dataframe(dfgroup.describe())

                #데이터 저장하기
                st.subheader('')
                st.subheader('데이터 저장하기 :file_folder:')
                csvfile_name = st.text_input('저장할 파일명을 입력하세요 ex)csvfile.csv')
                if len(csvfile_name) != 0 :
                    df.to_csv(csvfile_name)
                    st.success(csvfile_name + '파일이 저장되었습니다')

if __name__ == '__main__' :
    main()