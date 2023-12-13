from random import randint


division_color_dict = {
    "1": "#3f3f46",
    "2": "#565584",
    "3": "#ca8a04",
    "4": "#1e3a8a",
    "5": "#831843",
    "6": "#166534",
}


def check_industry_class_type(type: str):
    type = type.lower()
    if type == "c":
        industry_type = "classList"
    elif type == "t":
        industry_type = "themeList"
    else:
        industry_type = "etc"
    return industry_type


def generate_source_data(industry_class_list: list):
    domain_dict = {}
    industry_class_dict = {}
    node_list = []

    for industry_class in industry_class_list:
        domain_code = industry_class["domain_code"]
        if not domain_dict.get(domain_code):
            domain_dict[domain_code] = {
                "code": industry_class["domain_code"],
                "name": industry_class["domain_name"],
                "division": industry_class["domain_division"],
            }

        industry_class_type = check_industry_class_type(
            industry_class["industry_class_type"]
        )
        industry_class_list = industry_class_dict.setdefault(
            domain_code, {"classList": [], "themeList": []}
        )[industry_class_type]
        industry_class_list.append(
            {
                "industryClassCode": industry_class["industry_class_code"],
                "industryClassName": industry_class["industry_class_name"],
                "industryClassType": industry_class["industry_class_type"],
            }
        )

    for domain_code in domain_dict.keys():
        industry_class_data = industry_class_dict[domain_code]
        domain_division = domain_dict[domain_code]["division"]
        node_color = division_color_dict.get(str(domain_division))
        node = {
            "classList": {
                "color": node_color if node_color else "#fff",
                "domainId": domain_code,
                "domainCode": domain_code,
                "domainName": domain_dict[domain_code]["name"],
                **industry_class_data,
            },
        }
        node_list.append(node)

    return node_list
