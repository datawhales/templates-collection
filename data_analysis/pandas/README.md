# Pandas

## TODOs
- 실제 데이터의 분석 및 시각화 예시 추가하면 좋을 것 같음
- rolling
- cumsum
- cut
- set_index
- reset_index
- concat
- Algo-Trade 참고하여 작성
```
- df.info()
- summary(df)
- df = df[df['column_name'] != value]
- mask = (df['col1'] != 'val1') & (df['col2'] != 'val2')
    df = df[mask]
- df['column_name'] = df['column_name'].astype(float)
- cols = ['column_name1', 'column_name2', ...]
    df[cols] = df[cols].astype(float)
- df['new_col'] = df['col1'].map(lambda x: x**2)
- df.sort_values(by=['col1', 'col2'], ascending=[True, False], inplace=True)
```
