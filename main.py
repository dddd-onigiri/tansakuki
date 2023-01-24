import streamlit as st
import numpy as np
import time

st.title("2分探索と線形探索の違い")

# Generate array of integers
N = 21
arr = np.arange(1, N, 1).tolist()

# 2分探索
st.markdown("## 2分探索")
number_2 = st.number_input("2分探索する数字を入力してください", key='number_2')

low = 0
high = N - 1

st.write("2分探索中....")
start_2 = time.time()
while low <= high:
    mid = int((low + high) / 2)
    if arr[mid] == number_2:
        ans_2 = mid
        break
    elif arr[mid] > number_2:
        high = mid - 1
    else:
        low = mid + 1

end_2 = time.time()
st.write("2分探索完了！")
total_time_2 = end_2 - start_2
st.write("探索にかかった時間：", total_time_2)

if number_2 in arr:
    st.markdown(f'数字{number_2}はarr[{ans_2}]にあります。')

# Solution
st.markdown("## 線形探索")
number_1 = st.number_input("線形探索する数字を入力してください", key='number_1')

start_1 = time.time()
for i, x in enumerate(arr):
    if x == number_1:
        ans_1 = i

end_1 = time.time()
st.write("線形探索完了！")
total_time_1 = end_1 - start_1

st.write("探索にかかった時間：", total_time_1)
if number_1 in arr:
    st.markdown(f'数字{number_1}はarr[{ans_1}]にあります。')

st.markdown("### 比較結果")
st.markdown(f'2分探索時間：{total_time_2} 線形探索時間：{total_time_1}')
if total_time_2 < total_time_1:
    st.markdown("2分探索の方が早い！")
elif total_time_2 > total_time_1:
    st.markdown("線形探索の方が早い！")
else:
    st.markdown("両者の探索時間は同じ")
