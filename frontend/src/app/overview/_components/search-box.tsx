'use client';

import Link from 'next/link';
import React, { useEffect, useState } from 'react';

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
  const [searchCategory, setSearchCategory] = useState('corpName');
  const [searchKeyword, setSearchKeyword] = useState('');

  const handleSearchCategory = (value: string) => {
    setSearchCategory(value);
  };
  const handleSearchKeyword = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchKeyword(event.target.value);
  };

  useEffect(() => {
    console.log(searchCategory, searchKeyword);
  }, [searchCategory, searchKeyword]);

  return (
    <div className="flex gap-2">
      <Select onValueChange={handleSearchCategory} value={searchCategory}>
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="회사명" defaultValue="corpName" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="corpName">회사명</SelectItem>
          <SelectItem value="corpCode">사업자등록번호</SelectItem>
          <SelectItem value="regCode">법인등록번호</SelectItem>
          <SelectItem value="stockCode">증권종목코드</SelectItem>
        </SelectContent>
      </Select>
      <Input
        value={searchKeyword}
        placeholder="검색어를 입력해주세요."
        onChange={handleSearchKeyword}
      />
      <Button asChild>
        <Link
          href={{
            pathname: '/overview/search',
            query: {
              category: searchCategory,
              query: searchKeyword,
            },
          }}
          className="w-[200px]"
        >
          검색
        </Link>
      </Button>
    </div>
  );
};

export default SearchBox;
