import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write('プログレスバーの表示')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!!'
expander1 = st.expander('アニメ一覧')
url1 = "https://www.hmv.co.jp/news/article/230808501/"
expander1.write("五等分の花嫁 [link](%s)"%url1)
expander1.markdown("五等分の花嫁 [link](%s)"%url1)



""" if st.checkbox('Show Image'):
    img = Image.open('nino25.jpg')
    st.image(img, caption='Nino nakano', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

text = st.text_input(
    'あなたの趣味を教えてください'
)
'あなたの趣味:', text

condition = st.slider(
    '今日のあなたのコンディションを教えてください',
    0,
    100,
    60
)
 """
#'今日のコンディションは',condition,'%です。'
"""df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [33.694249473877484, 130.43757056725767],
   columns=['lat', 'lon']
    )
df
"""
#bar,area,line(棒,領域,線)
#st.bar_chart(df)

#lat,lon(緯度,軽度)
#st.map(df)
#st.table(df.style.highlight_max(axis=0))
#tableはクリックしても並び替えはできない
#dataframe,writeだと動的(クリックで並び替え可能)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""