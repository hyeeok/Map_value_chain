import React from 'react';

import { Skeleton } from '@/components/ui/skeleton';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';

const IndustryInfo = () => {
  return (
    <div className="flex flex-col gap-6">
      <section className="border rounded-md">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead colSpan={2}>사업연도</TableHead>
              <TableHead>2018</TableHead>
              <TableHead>2019</TableHead>
              <TableHead>2020</TableHead>
              <TableHead>2021</TableHead>
              <TableHead>2022</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <TableRow>
              <TableHead rowSpan={6}>주식정보</TableHead>
              <TableHead>액면가</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>자기주식수</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>발행주식수(보통가)</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>주가(보통주)</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>발행주식수(우선주)</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>주가(우선주)</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
            <TableRow>
              <TableHead rowSpan={6}>가치정보</TableHead>
              <TableHead>시가총액</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>매출액</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>영업이익</TableHead>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
              <TableCell> ↑ ?% or ↓ ?%</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </section>
      <section>
        <h3 className="scroll-m-20 text-xl font-bold tracking-tight">
          주요 거래처
        </h3>
        <div className="mt-2">
          <Skeleton className="w-full h-[200px] rounded-md" />
        </div>
      </section>
    </div>
  );
};

export default IndustryInfo;
