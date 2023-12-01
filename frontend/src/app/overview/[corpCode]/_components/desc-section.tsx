'use client';

import { ArrowLeft, ChevronRightIcon } from 'lucide-react';
import Link from 'next/link';
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

const formatDate = (inputDate: string | null) => {
  if (!inputDate) {
    return inputDate;
  }
  const year = inputDate.slice(0, 4);
  const month = parseInt(inputDate.slice(4, 6), 10);
  const day = parseInt(inputDate.slice(6), 10);
  const formattedDate = `${year}년 ${month}월 ${day}일`;
  return formattedDate;
};

const formatListDate = (inputDate: string | null) => {
  if (!inputDate) {
    return inputDate;
  }
  const parts = inputDate.split('/');
  const year =
    parseInt(parts[0]) < 23
      ? 2000 + parseInt(parts[0])
      : 1900 + parseInt(parts[0]);
  const month = parseInt(parts[1]);
  const day = parseInt(parts[2]);
  const formattedDate = `${year}년 ${month}월 ${day}일`;
  return formattedDate;
};

const DescSection = ({ data }: { data: OverviewDescType }) => {
  console.log(data);
  const router = useRouter();

  return (
    <div className="flex flex-col gap-6">
      <section>
        <div className="mb-4">
          <Button
            variant="link"
            onClick={() => router.back()}
            className="pl-0 text-muted-foreground"
          >
            <ArrowLeft className="mr-2 h-4 w-4" />
            이전 페이지
          </Button>
        </div>
        <div className="flex justify-between">
          <h2 className="scroll-m-20 text-3xl font-bold tracking-tight">
            {data.stockName}
          </h2>
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
              <TableCell>{data.bizrNo || `-`}</TableCell>
              <TableHead>법인등록번호</TableHead>
              <TableCell>{data.jurirNo || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>정식회사명</TableHead>
              <TableCell>{data.corpName || `-`}</TableCell>
              <TableHead>회사영문명</TableHead>
              <TableCell>{data.corpNameEng || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>설립일</TableHead>
              <TableCell>{formatDate(data.establishDate)}</TableCell>
              <TableHead>상장일</TableHead>
              <TableCell>{formatListDate(data.listDate)}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>홈페이지</TableHead>
              <TableCell>
                <Link
                  target="_blank"
                  rel="noopener noreferrer"
                  href={`https://${data.homepageUrl}`}
                  className="underline hover:opacity-80"
                >
                  {data.homepageUrl}
                </Link>
              </TableCell>
              <TableHead>전화번호</TableHead>
              <TableCell>{data.phoneNum || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>지역</TableHead>
              <TableCell>{data.adress.split(' ')[0] || `-`}</TableCell>
              <TableHead>소재지</TableHead>
              <TableCell>{data.adress || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>대표자명</TableHead>
              <TableCell>{data.ceoName || `-`}</TableCell>
              <TableHead>계열사수</TableHead>
              <TableCell>{data.affiliateList.length || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>중소기업여부</TableHead>
              <TableCell>{data.isSMCorp || `-`}</TableCell>
              <TableHead>벤처기업여부</TableHead>
              <TableCell>{data.isVenture || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>종속회사수</TableHead>
              <TableCell>{data.subCorpList.length || `-`}</TableCell>
              <TableHead>주주수</TableHead>
              <TableCell>{data.shareholderNum || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>기업종업원수</TableHead>
              <TableCell>{data.employeeNum.toLocaleString()}명</TableCell>
              <TableHead>기업1인평균급여급액</TableHead>
              <TableCell>{data.avgSalary.toLocaleString()}원</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>회계감사인명</TableHead>
              <TableCell>-</TableCell>
              <TableHead>감사보고서의견내용</TableHead>
              <TableCell>{data.auditorReportOpinion || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>결산월</TableHead>
              <TableCell>{data.settleMonth}월</TableCell>
              <TableHead>신용평가등급</TableHead>
              <TableCell>{data.issuerRate || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>주요사업</TableHead>
              <TableCell>{data.mainBiz || `-`}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>사업분류</TableHead>
              <TableCell>{data.classList.length || `-`}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </section>
    </div>
  );
};

export default DescSection;
