interface SidenavDataProps {
  domainCode: string;
  domainName: string;
  industryCode: string;
  industryName: string;
  className: string;
  classCode: string;
  classLevel: number;
}

// type ClassInfo = {
//   className: string;
//   classCode: string;
//   childClass: Map<string, ClassInfo>;
// };

// type IndustryInfo = {
//   industryCode: string;
//   industryName: string;
//   childClass: Map<string, ClassInfo>;
// };

// type DomainInfo = {
//   domainCode: string;
//   domainName: string;
//   childIndustry: Map<string, IndustryInfo>;
// };

// export type ResultType = Map<string, DomainInfo>;

// export const buildHierarchy = (datas: SidenavDataProps[]) => {
//   const result = new Map();
//   datas = datas.sort((a, b) => a.classLevel - b.classLevel);
//   datas.forEach((item) => {
//     const {
//       domainCode,
//       domainName,
//       industryCode,
//       industryName,
//       className,
//       classCode,
//       classLevel,
//     } = item;

//     if (!result.has(domainCode)) {
//       result.set(domainCode, {
//         domainCode,
//         domainName,
//         childIndustry: new Map(),
//       });
//     }

//     const domain = result.get(domainCode);
//     if (!domain.childIndustry.has(industryCode)) {
//       domain.childIndustry.set(industryCode, {
//         industryCode,
//         industryName,
//         childClass: new Map(),
//       });
//     }

//     const industry = domain.childIndustry.get(industryCode);
//     if (classLevel === 1) {
//       industry.childClass.set(classCode, {
//         className,
//         classCode,
//         childClass: new Map(),
//       });
//     } else if (classLevel === 2) {
//       const levelOneClassCode = classCode.substring(0, 1);
//       const levelOneClass = industry.childClass.get(levelOneClassCode);
//       levelOneClass.childClass.set(classCode, {
//         className,
//         classCode,
//         childClass: new Map(),
//       });
//     } else if (classLevel === 3) {
//       const levelTwoClassCode = classCode.substring(0, 1);
//       const levelTwoClass = industry.childClass.get(levelTwoClassCode);
//       levelTwoClass.childClass.set(classCode, {
//         className,
//         classCode,
//         childClass: new Map(),
//       });
//     }
//   });

//   return result;
// };
