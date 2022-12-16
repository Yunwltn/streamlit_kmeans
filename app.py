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
        df = pd.read_csv(file)
        st.dataframe(df)

        # 비어있는 데이터 확인하고 있으면 제거하기
        st.subheader('')
        st.subheader('데이터 확인하기 :memo:')
        st.dataframe(df.describe())

        if st.checkbox('0 데이터로 채워져 있는 값을 nan값으로 변경하기') :
            column_list1 = df.columns
            selected_column1 = st.multiselect('원하는 컬럼을 선택하세요', column_list1)
            df = df[selected_column1] = df[selected_column1].replace(0, np.nan)
            if len(selected_column1) != 0 :
                st.dataframe(df.isna().sum())

        if st.checkbox('nan값 확인하기') :
            st.dataframe(df.isna().sum())
            if st.checkbox(':warning: nan값 모두 제거하기 :warning:') :
                df = df.dropna()
                st.dataframe(df.isna().sum())

        # KMeans 클러스터링을 하기 위해 X로 사용할 컬럼을 설정
        st.subheader('')
        st.subheader('X로 사용할 컬럼 설정 :pushpin:')
        column_list2 = df.columns
        selected_column2 = st.multiselect('X로 사용할 컬럼을 선택하세요', column_list2)

        if len(selected_column2) != 0 :
            X = df[selected_column2]
            st.dataframe(X)
        # X의 컬럼 데이터가 문자가 있는지 확인
            X_object_column = X.columns.values[X.dtypes == 'object']
            
            if X[X_object_column].nunique().values <= 2 :
                # label 실행
                encoder = LabelEncoder()
                X[X_object_column] = pd.DataFrame(encoder.fit_transform( X[X_object_column] ))
                st.write(':arrow_forward: 문자열 데이터 컬럼 Label Encoding 실행')
                st.dataframe(X)
            elif X[X_object_column].nunique().values > 2:
                # one-hot 실행
                X_list = X.columns.values.tolist()
                X_list_index = X_list.index(X_object_column)
                ct = ColumnTransformer( [ ( 'encoder', OneHotEncoder() , [X_list_index]  ) ], remainder= 'passthrough' )
                X = ct.fit_transform(X)
                st.write(':arrow_forward: 문자열 데이터 컬럼 One-Hot Encoding 실행')
                st.dataframe(X)

        # WCSS를 확인하기 위한 그룹의 갯수 정하기
        st.subheader('')
        st.subheader('클러스터링 갯수 선택 :pushpin:')
        if st.checkbox('WCSS로 추천받기'):
            max_number = st.slider('WCSS를 확인하기 위한 최대 그룹 갯수 선택', 2, 20, value=10)
            if len(selected_column2) == 0 :
                st.write('')
            else :
                wcss = []
                for k in np.arange(1, max_number+1) :
                    kmeans = KMeans(n_clusters= k, random_state= 5)
                    kmeans.fit(X)
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
            y_pred = kmeans.fit_predict(X)
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

if __name__ == '__main__' :
    main()