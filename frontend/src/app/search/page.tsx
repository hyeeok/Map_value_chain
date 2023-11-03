import React from 'react';

import IndustryInfo from '@/app/search/_components/industry-info';
import SideNav from '@/app/search/_components/sidenav';
// import SearchResult from '@/app/search/_components/search-result';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';

const SearchPage = () => {
  return (
    <div className="h-[calc(100vh-45px)] flex flex-col px-8">
      <section className="flex flex-1 gap-6">
        <SideNav />
        <div className="flex-1">
          <section className="py-4">
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
              <Input />
              <Button className="w-[200px]">검색</Button>
            </div>
          </section>
          <div className="flex-1">
            {/* <SearchResult /> */}
            <IndustryInfo />
          </div>
        </div>
      </section>
    </div>
  );
};

export default SearchPage;
