'use client';

import { useRouter } from 'next/navigation';
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
  const router = useRouter();

  const [searchKeyword, setSearchKeyword] = useState('');

  const handleSearchKeyword = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchKeyword(event.target.value);
  };

  useEffect(() => {
    console.log(searchKeyword);
  }, [searchKeyword]);

  return (
    <div className="flex gap-2">
      <Select>
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="회사명" defaultValue="corpName" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="corpName">회사명</SelectItem>
          <SelectItem value="copCode">사업자등록번호</SelectItem>
          <SelectItem value="regCode">법인등록번호</SelectItem>
          <SelectItem value="stockCode">증권종목코드</SelectItem>
        </SelectContent>
      </Select>
      <Input value={searchKeyword} onChange={handleSearchKeyword} />
      <Button
        onClick={() => router.push(`/overview?query=${searchKeyword || ''}`)}
        className="w-[200px]"
      >
        검색
      </Button>
    </div>
  );
};

export default SearchBox;
