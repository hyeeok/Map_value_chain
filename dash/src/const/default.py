import numpy as np

company_col = ["red", "blue"]

data_source_color = {
    "재무상태": "Olive",
    "손익계산": "DarkGreen",
    "현금흐름": "DarkSlateBlue",
    "주식": "Gray",
    "거래소": "Brown",
    "PerShare": "Aqua",
    "Multiple": "CadetBlue",
    "안정성": "Crimson",
    "수익성": "DeepPink",
}
data_source = data_source_color.keys()

log_currency_dict = {  # 기본 1백만원 단위
    "tickvals": np.log(np.array([1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9])),
    "ticktext": [
        "10만",
        "100만",
        "1000만",
        "1억",
        "10억",
        "100억",
        "1000억",
        "1조",
        "10조",
        "100조",
    ],
}
currency_dict = {  # 기본 1백만원 단위
    "tickvals": [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9],
    "ticktext": [
        "10만",
        "100만",
        "1000만",
        "1억",
        "10억",
        "100억",
        "1000억",
        "1조",
        "10조",
        "100조",
    ],
}

data_years = ["2018", "2019", "2020", "2021", "2022"]

# make default variable
column_dict = {
    "거래소": ["주가(보통주)", "주가(우선주)", "시가총액", "EV ", "EBITDA", "현금흐름"],
    "손익계산": [
        "매출액",
        "매출원가",
        "판관비",
        "영업이익",
        "세전순이익",
        "세금",
        "당기순이익",
        "당기순이익(지배)",
        "당기순이익(비지배)",
    ],
    "재무상태": [
        "자산총계",
        "유동자산",
        "현금및현금성자산",
        "매출채권",
        "단기금융상품",
        "단기금융자산(상각후원가)",
        "단기금융자산(당기손익)",
        "재고자산",
        "유형자산",
        "무형자산",
        "부채총계",
        "유동부채",
        "매입채무",
        "단기차입금",
        "유동성장기부채",
        "비유동부채",
        "사채",
        "장기차입금",
        "자본총계",
        "지배기업주주지분",
        "자본금",
        "자본금(우선주)",
        "자본금(보통주)",
        "비지배주주지분",
    ],
    "주식": ["액면가", "발행주식수(보통주)", "발행주식수(우선주)", "자기수식수"],
    "현금흐름": [
        "영업활동현금흐름",
        "감가상각비(현금흐름)",
        "무형자산상각비(현금흐름)",
        "투자활동현금흐름",
        "CAPEX",
        "재무활동현금흐름",
    ],
}
columns = [col for columns in column_dict.values() for col in columns]

# ratio values which is calculated from above values
column_ratio_dict = {
    "PerShare": ["SPS", "EBITDAPS", "EPS", "BPS", "CFPS"],
    "Multiple": ["PSR", "PER", "PBR", "PCR", "EV/Sales", "EV/EBITDA"],
    "안정성": ["자기자본비율", "부채비율", "유동부채비율", "비유동부채비율", "순차입금비율", "유동비율", "자본유보율"],
    "수익성": [
        "영업이익률",
        "EBITDA마진율",
        "순이익율",
        "매출액증가율",
        "영업이익증가율",
        "EBITDA증가율",
        "EPS증가율",
        "BPS증가율",
    ],
}
columns_ratio = [col for columns in column_ratio_dict.values() for col in columns]
