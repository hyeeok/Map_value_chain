interface OverviewIndex {
  domainId: number;
  domainName: string;
  domainCode: string;
  industryClassId: number;
  industryClassName: string;
  industryClassCode: string;
  subClassId: number;
  subClassName: string;
  subClassCode: string;
  subClassLevel: number;
}

interface SubClassInfo {
  subClassId: number;
  subClassName: string;
  subClassCode: string;
  childClass?: {
    [key: string]: SubClassInfo;
  };
}

interface IndustryClassInfo {
  industryClassId: number;
  industryClassName: string;
  industryClassCode: string;
  childClass: {
    [key: string]: SubClassInfo;
  };
}

interface DomainInfo {
  domainId: number;
  domainName: string;
  domainCode: string;
  childIndustry: {
    [key: string]: IndustryClassInfo;
  };
}

export interface ResultType {
  [key: string]: DomainInfo;
}

export const buildHierarchy = (datas: OverviewIndex[]) => {
  const result = <ResultType>{};
  datas = datas.sort((a, b) => a.subClassLevel - b.subClassLevel);
  datas.forEach((item) => {
    const {
      domainId,
      domainName,
      domainCode,
      industryClassId,
      industryClassName,
      industryClassCode,
      subClassId,
      subClassName,
      subClassCode,
      subClassLevel,
    } = item;

    if (!result[domainCode]) {
      result[domainCode] = {
        domainId,
        domainName,
        domainCode,
        childIndustry: {},
      };
    }

    const domain = result[domainCode];
    if (!domain.childIndustry[industryClassCode]) {
      domain.childIndustry[industryClassCode] = {
        industryClassId,
        industryClassName,
        industryClassCode,
        childClass: {},
      };
    }

    const industry = domain.childIndustry[industryClassCode];
    if (subClassLevel === 1) {
      industry.childClass[subClassCode] = {
        subClassId,
        subClassName,
        subClassCode,
        childClass: {},
      };
    } else if (subClassLevel === 2) {
      const levelOneClassCode = subClassCode.substring(0, 1);
      const levelOneClass = industry.childClass[levelOneClassCode];
      levelOneClass.childClass = levelOneClass.childClass || {};
      levelOneClass.childClass[subClassCode] = {
        subClassId,
        subClassName,
        subClassCode,
        childClass: {},
      };
    } else if (subClassLevel === 3) {
      const levelOneClassCode = subClassCode.substring(0, 1);
      const levelOneClass = industry.childClass[levelOneClassCode];
      levelOneClass.childClass = levelOneClass.childClass || {};
      const levelTwoClassCode = subClassCode.substring(0, 3);
      const levelTwoClass = levelOneClass.childClass[levelTwoClassCode];
      levelTwoClass.childClass = levelTwoClass.childClass || {};
      levelTwoClass.childClass[subClassCode] = {
        subClassId,
        subClassName,
        subClassCode,
      };
    }
  });
  return result;
};
