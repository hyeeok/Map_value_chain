'use client';

import Link from 'next/link';
import { useSearchParams } from 'next/navigation';
import React, { useEffect, useState } from 'react';

import { getOverviewhList } from '@/api/overview/api';
import Pagination from '@/app/overview/_components/pagination';
import SearchBox from '@/app/overview/_components/search-box';
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

const OverviewList = () => {
  const limit = 20;
  const searchParams = useSearchParams();
  const params = {
    category: searchParams.get('category') || null,
    keyword: searchParams.get('keyword') || null,
  };

  const [searchCategory, setSearchCategory] = useState('firmName');
  const [searchKeyword, setSearchKeyword] = useState('');
  const [overviewData, setOverviewData] = useState<OverviewListData>();
  const [currentPage, setCurrentPage] = useState(1);
  const [pageNum, setPageNum] = useState(0);

  useEffect(() => {
    getOverviewhList({ limit: limit })
      .then((response) => {
        setOverviewData(response);
        setPageNum(Math.ceil(response.length / limit));
      })
      .catch();
  }, []);

  const handleSearch = (category: string, keyword: string) => {
    getOverviewhList({
      category: category,
      keyword: keyword,
      limit: limit,
    })
      .then((response) => {
        setOverviewData(response);
        setPageNum(Math.ceil(response.length / limit));
        setCurrentPage(1);
      })
      .catch();
  };

  const onSearchCategoryChange = (value: string) => {
    setSearchCategory(value);
  };
  const onSearchKeywordChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setSearchKeyword(event.target.value);
  };
  const handlePageClick = (targetPage: number) => {
    getOverviewhList({
      category: params.category,
      keyword: params.keyword,
      limit: limit,
      page: targetPage,
    })
      .then((response) => {
        setOverviewData(response);
        setCurrentPage(targetPage);
      })
      .catch();
  };

  return (
    <>
      <section className="pt-6 pb-4">
        <SearchBox
          onSearchCategoryChange={onSearchCategoryChange}
          onSearchKeywordChange={onSearchKeywordChange}
          searchCategory={searchCategory}
          searchKeyword={searchKeyword}
          handleSearch={handleSearch}
        />
      </section>
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
                {overviewData &&
                  overviewData.data.map((data, i) => (
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
                            href={data.homepage}
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
              currentPage={currentPage}
              pageNum={pageNum}
            />
          </div>
        </div>
      </section>
    </>
  );
};

export default OverviewList;
