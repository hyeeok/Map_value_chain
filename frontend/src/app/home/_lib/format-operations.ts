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
};

export type DomainType = {
  domainCode: string;
  domainName: string;
  domainDivision: string;
  classList: IndustryClassType[];
  themeList: IndustryClassType[];
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
        classList: [],
        themeList: [],
      };
    }

    if (industryClassType.toLowerCase() === 'c') {
      industryMap[domainCode].classList.push({
        industryClassCode,
        industryClassName,
      });
    } else if (industryClassType.toLowerCase() === 't') {
      industryMap[domainCode].themeList.push({
        industryClassCode,
        industryClassName,
      });
    }
  });

  const result = Object.values(industryMap);
  // const result = industryMap;
  return result;
};
