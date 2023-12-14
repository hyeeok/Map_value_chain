export type IndustryType = {
  domainCode: string;
  domainName: string;
  domainDivision: string;
  industryClassCode: string;
  industryClassName: string;
  industryClassType: string;
};

export type IndustryClassType = {
  industryClassCode: string;
  industryClassName: string;
  industryClassType: string;
};

export type DomainType = {
  domainCode: string;
  domainName: string;
  domainDivision: string;
  industryClassList: IndustryClassType[];
};

export const buildICHierarchy = (data: IndustryType[]) => {
  const industryMap = <{ [key: string]: DomainType }>{};
  data.forEach((item) => {
    const {
      domainCode,
      domainName,
      domainDivision,
      industryClassCode,
      industryClassName,
      industryClassType,
    } = item;

    if (!industryMap[domainCode]) {
      industryMap[domainCode] = {
        domainName,
        domainCode,
        domainDivision,
        industryClassList: [],
      };
    }

    industryMap[domainCode].industryClassList.push({
      industryClassCode,
      industryClassName,
      industryClassType,
    });
  });

  const result = Object.values(industryMap);
  // const result = industryMap;
  return result;
};
