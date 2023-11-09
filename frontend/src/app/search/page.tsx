import React from 'react';

import SearchResult from '@/app/search/_components/search-result';

const SearchPage = ({
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

export default SearchPage;
