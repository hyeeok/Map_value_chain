export interface OverviewIndex {
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

export interface SubClassInfo {
  subClassId: number;
  subClassName: string;
  subClassCode: string;
  childClass?: {
    [key: string]: SubClassInfo;
  };
}

export interface IndustryClassInfo {
  industryClassId: number;
  industryClassName: string;
  industryClassCode: string;
  childClass: {
    [key: string]: SubClassInfo;
  };
}

export interface DomainInfo {
  domainId: number;
  domainName: string;
  domainCode: string;
  childIndustryClass: {
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
        childIndustryClass: {},
      };
    }

    const domain = result[domainCode];
    if (!domain.childIndustryClass[industryClassCode]) {
      domain.childIndustryClass[industryClassCode] = {
        industryClassId,
        industryClassName,
        industryClassCode,
        childClass: {},
      };
    }

    const industry = domain.childIndustryClass[industryClassCode];
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

export const isIndustryClassInfo = (item: any): item is IndustryClassInfo => {
  return (item as IndustryClassInfo).industryClassCode !== undefined;
};
export const isSubClassInfo = (item: any): item is SubClassInfo => {
  return (item as SubClassInfo).subClassCode !== undefined;
};
