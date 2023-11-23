'use client';

import React from 'react';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';

interface SearchBoxProps {
  onSearchCategoryChange: (value: string) => void;
  onSearchKeywordChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  searchCategory: string;
  searchKeyword: string;
  handleSearch: (category: string, keyword: string) => void;
}

const SearchBox = ({
  onSearchCategoryChange,
  onSearchKeywordChange,
  searchCategory,
  searchKeyword,
  handleSearch,
}: SearchBoxProps) => {
  return (
    <div className="flex gap-2">
      <Select onValueChange={onSearchCategoryChange} value={searchCategory}>
        <SelectTrigger className="w-[200px]">
          <SelectValue placeholder="회사명" defaultValue="firmName" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="firmName">회사명</SelectItem>
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
