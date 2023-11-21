'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import React from 'react';

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';

interface OverviewListType {
  id?: number;
  corpCode: string;
  firmName: string;
  bizrNo: string;
  jurirNo: string;
  stockCode: string;
  conglomerateName: string | null;
  ceoName: string;
  establishDate: string;
  adress1: string;
  adress2: string;
  homepage?: string | null;
}

const OverviewList = ({ datas }: { datas: OverviewListType[] }) => {
  const router = useRouter();
  return (
    <div className="rounded-md">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>회사명</TableHead>
            <TableHead>사업자등록번호</TableHead>
            <TableHead>법인구분</TableHead>
            <TableHead>종목코드</TableHead>
            <TableHead>계열모회사</TableHead>
            <TableHead>대표자명</TableHead>
            <TableHead>설립일</TableHead>
            <TableHead>지역</TableHead>
            <TableHead>홈페이지</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {datas.map((data, i) => (
            <TableRow key={i}>
              <TableCell>
                <Link
                  href={`/overview/${data.corpCode}`}
                  className="hover:underline"
                >
                  {data.firmName}
                </Link>
              </TableCell>
              <TableCell>{data.bizrNo}</TableCell>
              <TableCell>{data.jurirNo}</TableCell>
              <TableCell>{data.stockCode}</TableCell>
              <TableCell>{data.conglomerateName || '-'}</TableCell>
              <TableCell>{data.ceoName}</TableCell>
              <TableCell>{data.establishDate}</TableCell>
              <TableCell>
                {data.adress1} {data.adress2}
              </TableCell>
              <TableCell>
                {data.homepage ? (
                  <Link href={data.homepage} className="hover:underline">
                    바로가기
                  </Link>
                ) : (
                  <>-</>
                )}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
};

export default OverviewList;
