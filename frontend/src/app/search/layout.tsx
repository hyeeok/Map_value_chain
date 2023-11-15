import React from 'react';

import SearchBox from '@/app/search/_components/search-box';
import Sidenav from '@/app/search/_components/sidenav';
import { SIDENAV_DATA } from '@/app/search/_const/test';

const SearchLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="container flex flex-col px-8">
      <section className="flex flex-1 gap-6">
        <Sidenav sidenav={SIDENAV_DATA} />
        <div className="flex-1">
          <section className="pt-6 pb-4">
            <SearchBox />
          </section>
          <div className="flex-1 pb-6">{children}</div>
        </div>
      </section>
    </div>
  );
};

export default SearchLayout;
