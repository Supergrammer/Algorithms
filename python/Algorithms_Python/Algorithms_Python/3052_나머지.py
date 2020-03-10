st = []
li = []

for i in range(10):
    li.append(int(input()))

for i in range(10):
    st.append(li[i] % 42)

st = set(st)
print(len(st))