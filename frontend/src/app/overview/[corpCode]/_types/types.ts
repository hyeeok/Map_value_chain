export interface OverviewDescType {
  stockName: string;
  stockCode: number;
  bizrNo: number;
  jurirNo: number;
  corpName: string;
  corpNameEng: string;
  corpNameHistory: { seq: number; corpName: string }[];
  establishDate: string;
  corpClass: string;
  listDate: string;
  delistDate: string;
  homepageUrl: string;
  phoneNum: string;
  adress: string;
  ceoName: string;
  ceoNameHistory: { seq: number; ceoName: string }[];
  affiliateList: { corpCode: string; corpName: string }[];
  isSMCorp: string;
  isVenture: string;
  subCorpList: { corpName: string }[];
  shareholderNum: null;
  employeeNum: number;
  avgSalary: number;
  auditorReportOpinion: string;
  settleMonth: number;
  issuerRate: string;
  mainBiz: string;
  classList: [];
}

export interface OverviewShareholderType {
  name: string;
  relate: string;
  stockKind: string;
  reportCode: string;
  basisStockCount: string;
  basisStockRate: string;
  endStockCount: string;
  endStockRate: string;
  note: string;
}
