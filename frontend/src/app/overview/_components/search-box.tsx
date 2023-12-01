'use client';

import { useRouter } from 'next/navigation';
import React, { useState } from 'react';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';

const SearchBox = () => {
  const router = useRouter();
  const [searchCategory, setSearchCategory] = useState('stockName');
  const [searchKeyword, setSearchKeyword] = useState('');

  const onSearchCategoryChange = (value: string) => {
    setSearchCategory(value);
  };
  const onSearchKeywordChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setSearchKeyword(event.target.value);
  };
  const handleSearch = (category: string, keyword: string) => {
    let url = `/overview`;
    if (keyword) {
      url = `/overview/search?category=${category}&keyword=${keyword}`;
    }
    router.push(url);
  };

  return (
    <div className="flex gap-2">
      <Select onValueChange={onSearchCategoryChange} value={searchCategory}>
        <SelectTrigger className="w-[220px]">
          <SelectValue placeholder="회사명" defaultValue="stockName" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="stockName">회사명</SelectItem>
          <SelectItem value="corpCode">사업자등록번호</SelectItem>
          <SelectItem value="regCode">법인등록번호</SelectItem>
          <SelectItem value="stockCode">증권종목코드</SelectItem>
        </SelectContent>
      </Select>
      <Input
        placeholder="검색어를 입력해주세요."
        value={searchKeyword}
        onChange={(event) => onSearchKeywordChange(event)}
      />
      <Button
        onClick={() => handleSearch(searchCategory, searchKeyword)}
        className="w-[200px]"
      >
        검색
      </Button>
    </div>
  );
};

export default SearchBox;
