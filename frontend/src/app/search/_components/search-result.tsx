import React from 'react';

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';

const SearchResult = () => {
  return (
    <div>
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
          <TableRow>
            <TableCell>기업마스터.공시회사명</TableCell>
            <TableCell>기업마스터.사업자등록번호</TableCell>
            <TableCell>기업마스터.법인구분 명칭</TableCell>
            <TableCell>기업마스터.종목코드</TableCell>
            <TableCell>기업마스터.계열모회사명</TableCell>
            <TableCell>기업마스터.대표자명</TableCell>
            <TableCell>기업마스터.설립일</TableCell>
            <TableCell>기업마스터.지역</TableCell>
            <TableCell>기업마스터.홈페이지</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  );
};

export default SearchResult;
