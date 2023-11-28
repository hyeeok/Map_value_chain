'use client';

import Link from 'next/link';
import { useRouter, useSearchParams } from 'next/navigation';
import React from 'react';

import Pagination from '@/app/overview/_components/pagination';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';

interface OverviewData {
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
interface OverviewListData {
  length: number;
  data: OverviewData[];
}

const OverviewList = ({ data }: { data: OverviewListData }) => {
  const router = useRouter();
  const limit = 20;
  const pageNum = Math.ceil(data?.length / limit);
  const searchParams = useSearchParams();
  const params = {
    category: searchParams.get('category') || '',
    keyword: searchParams.get('keyword') || '',
    limit: searchParams.get('limit') || '',
    page: searchParams.get('page') || '1',
  };

  const handlePageClick = (targetPage: number) => {
    const url = `/overview/search?category=${params.category}&keyword=${params.keyword}&page=${targetPage}`;
    router.push(url);
  };

  return (
    <>
      <section className="flex-1 pb-6">
        <div className="flex flex-col h-full justify-between">
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
                {data &&
                  data.data.map((data, i) => (
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
                      <TableCell>{data.stockCode || '-'}</TableCell>
                      <TableCell>{data.conglomerateName || '-'}</TableCell>
                      <TableCell>{data.ceoName || '-'}</TableCell>
                      <TableCell>{data.establishDate}</TableCell>
                      <TableCell>
                        {data.adress1} {data.adress2}
                      </TableCell>
                      <TableCell>
                        {data.homepage ? (
                          <Link
                            target="_blank"
                            rel="noopener noreferrer"
                            href={`https://${data.homepage}`}
                            className="hover:underline"
                          >
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
          <div className="flex justify-center pt-6">
            <Pagination
              handlePageClick={handlePageClick}
              currentPage={parseInt(params.page)}
              pageNum={pageNum}
            />
          </div>
        </div>
      </section>
    </>
  );
};

export default OverviewList;
