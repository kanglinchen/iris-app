import streamlit as st
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 创建简单的Streamlit界面
st.title('鸢尾花种类预测')
st.write("输入参数以预测鸢尾花的种类")

# 用户输入特征值
sepal_length = st.slider('Sepal Length', 4.0, 8.0, 5.4)
sepal_width = st.slider('Sepal Width', 2.0, 4.0, 3.4)
petal_length = st.slider('Petal Length', 1.0, 6.0, 1.3)
petal_width = st.slider('Petal Width', 0.1, 2.5, 0.2)

# 预测按钮
if st.button('预测'):
    # 构建模型并预测
    classifier = DecisionTreeClassifier()
    classifier.fit(X, y)
    prediction = classifier.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.write('预测的鸢尾花种类是: ', iris.target_names[prediction][0])