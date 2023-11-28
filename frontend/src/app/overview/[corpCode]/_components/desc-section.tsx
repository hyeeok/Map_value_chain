'use client';

import { ChevronRightIcon } from 'lucide-react';
import { useRouter } from 'next/navigation';

import { OverviewDescType } from '@/app/overview/[corpCode]/_types/types';
import { Button } from '@/components/ui/button';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
} from '@/components/ui/table';

const DescSection = ({ data }: { data: OverviewDescType }) => {
  const router = useRouter();

  return (
    <div className="flex flex-col gap-6">
      <section>
        <div className="flex justify-between">
          <h2 className="scroll-m-20 text-3xl font-bold tracking-tight">
            {data.stockName}
          </h2>
          <Button variant={'outline'} onClick={() => router.back()}>
            이전 페이지
          </Button>
        </div>

        <div className="mt-2 flex items-center space-x-1 text-sm text-muted-foreground">
          <div className="overflow-hidden text-ellipsis whitespace-nowrap">
            {data.corpClass}
          </div>
          <ChevronRightIcon className="h-4 w-4" />
          <div className="overflow-hidden text-ellipsis whitespace-nowrap">
            {data.stockCode}
          </div>
        </div>
      </section>

      <section className="border rounded-md">
        <Table>
          <TableBody>
            <TableRow>
              <TableHead>사업자등록번호</TableHead>
              <TableCell>{data.bizrNo}</TableCell>
              <TableHead>법인등록번호</TableHead>
              <TableCell>{data.jurirNo}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>정식회사명</TableHead>
              <TableCell>{data.corpName}</TableCell>
              <TableHead>회사영문명</TableHead>
              <TableCell>{data.corpNameEng}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>설립일</TableHead>
              <TableCell>{data.establishDate}</TableCell>
              <TableHead>상장일</TableHead>
              <TableCell>{data.listDate}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>홈페이지</TableHead>
              <TableCell>{data.homepageUrl}</TableCell>
              <TableHead>전화번호</TableHead>
              <TableCell>{data.phoneNum}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>지역</TableHead>
              <TableCell>{data.adress}</TableCell>
              <TableHead>소재지</TableHead>
              <TableCell>{data.adress}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>대표자명</TableHead>
              <TableCell>{data.ceoName}</TableCell>
              <TableHead>계열사수</TableHead>
              <TableCell>{data.affiliateList.length}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>중소기업여부</TableHead>
              <TableCell>{data.isSMCorp}</TableCell>
              <TableHead>벤처기업여부</TableHead>
              <TableCell>{data.isVenture}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>종속회사수</TableHead>
              <TableCell>{data.subCorpList.length}</TableCell>
              <TableHead>주주수</TableHead>
              <TableCell>{data.shareholderNum}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>기업종업원수</TableHead>
              <TableCell>{data.employeeNum}</TableCell>
              <TableHead>기업1인평균급여급액</TableHead>
              <TableCell>{data.avgSalary}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>회계감사인명</TableHead>
              <TableCell>-</TableCell>
              <TableHead>감사보고서의견내용</TableHead>
              <TableCell>{data.auditorReportOpinion}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>결산월</TableHead>
              <TableCell>{data.settleMonth}</TableCell>
              <TableHead>신용평가등급</TableHead>
              <TableCell>{data.issuerRate}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>주요사업</TableHead>
              <TableCell>{data.mainBiz}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>사업분류</TableHead>
              <TableCell>{data.classList.length}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </section>
    </div>
  );
};

export default DescSection;
