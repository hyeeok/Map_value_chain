import { ChevronRightIcon } from '@radix-ui/react-icons';
import React from 'react';

import { Button } from '@/components/ui/button';
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
      <section>
        <div className="flex justify-between">
          <h2 className="scroll-m-20 text-3xl font-bold tracking-tight">
            회사명
          </h2>
          <Button variant={'outline'}>목록</Button>
        </div>

        <div className="mt-2 flex items-center space-x-1 text-sm text-muted-foreground">
          <div className="overflow-hidden text-ellipsis whitespace-nowrap">
            KOSPI
          </div>
          <ChevronRightIcon className="h-4 w-4" />
          <div className="overflow-hidden text-ellipsis whitespace-nowrap">
            종목코드
          </div>
        </div>
      </section>

      <section className="border rounded-md">
        <Table>
          <TableBody>
            <TableRow>
              <TableHead>사업자등록번호</TableHead>
              <TableCell>0000000</TableCell>
              <TableHead>법인등록번호</TableHead>
              <TableCell>0000000</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>사업자등록번호</TableHead>
              <TableCell>0000000</TableCell>
              <TableHead>법인등록번호</TableHead>
              <TableCell>0000000</TableCell>
            </TableRow>
            <TableRow>
              <TableHead>사업자등록번호</TableHead>
              <TableCell>0000000</TableCell>
              <TableHead>법인등록번호</TableHead>
              <TableCell>0000000</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </section>

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
          </TableBody>
        </Table>
      </section>
    </div>
  );
};

export default IndustryInfo;
