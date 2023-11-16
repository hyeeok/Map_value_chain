import React from 'react';

import SearchResult from '@/app/overview/_components/search-result';

const OverviewPage = ({
  searchParams,
}: {
  searchParams: { [key: string]: string | string[] | undefined };
}) => {
  return (
    <div className="flex flex-col">
      <SearchResult />
    </div>
  );
};

export default OverviewPage;
