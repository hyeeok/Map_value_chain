import React from 'react';

import OverviewList from '@/app/overview/_components/overview-list';
import { OVERVIEW_LIST } from '@/app/overview/search/_test/overview-list';

const datas = OVERVIEW_LIST;

const SearchPage = () => {
  // const searchParams = useSearchParams();
  // console.log(searchParams);
  return (
    <div className="flex flex-col">
      <OverviewList datas={datas} />
    </div>
  );
};

export default SearchPage;
