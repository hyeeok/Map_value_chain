import { ChevronLeft, ChevronRight } from 'lucide-react';
import React from 'react';

import OverviewList from '@/app/overview/_components/overview-list';
import { OVERVIEW_LIST } from '@/app/overview/_test/overview-list';
import { Button } from '@/components/ui/button';

const datas = OVERVIEW_LIST;
const length = 120;
const page = 1;
const limit = 20;

const Pagination = ({
  currentPage,
  pageNum,
}: {
  currentPage: number;
  pageNum: number;
}) => {
  const numArray = Array.from({ length: pageNum }).map((v, i) => i + 1);
  return (
    <>
      <Button variant="link" size="sm" disabled={currentPage <= 1}>
        <ChevronLeft className="w-4 h-4" />
      </Button>
      {numArray.map((i) => (
        <Button
          variant="link"
          size="sm"
          key={i}
          className={`${
            currentPage === i ? 'bg-primary text-primary-foreground' : ''
          }`}
        >
          {i}
        </Button>
      ))}
      <Button variant="link" size="sm" disabled={currentPage >= pageNum}>
        <ChevronRight className="w-4 h-4" />
      </Button>
    </>
  );
};

const SearchPage = ({
  searchParams,
}: {
  searchParams: { [key: string]: string | string[] | undefined };
}) => {
  console.log(searchParams);

  return (
    <div className="flex flex-col h-full justify-between">
      <OverviewList datas={datas} />
      <div className="flex justify-center pt-6">
        <Pagination currentPage={page} pageNum={Math.ceil(length / limit)} />
      </div>
    </div>
  );
};

export default SearchPage;
