export interface OverviewData {
  id?: number;
  corpCode: string;
  stockName: string;
  bizrNo: string;
  corpClass: string | null;
  stockCode: string | null;
  affiliateList: string[];
  ceoName: string | null;
  establishDate: string | null;
  adress: string | null;
  homepageUrl?: string | null;
}
export interface OverviewListData {
  length: number;
  data: OverviewData[];
}
