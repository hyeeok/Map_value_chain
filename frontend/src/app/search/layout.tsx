import React from 'react';

import SearchBox from '@/app/search/_components/search-box';
import { SIDENAV_DATA } from '@/app/search/_const/test';
import { buildHierarchy } from '@/app/search/_lib/sidenav-lib';

const SearchLayout = ({ children }: { children: React.ReactNode }) => {
  const sidenavData = buildHierarchy(SIDENAV_DATA.data);
  // console.log(sidenavData);
  return (
    <div className="container flex flex-col px-8">
      <section className="flex flex-1 gap-6">
        {/* <Sidenav sidenav={sidenavData} /> */}
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
