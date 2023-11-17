'use client';

import React from 'react';

import SidenavTree from '@/app/overview/_components/sidenav-tree';
import { ResultType } from '@/app/overview/_lib/sidenav-lib';
import { Collapsible } from '@/components/ui/collapsible';

const Sidenav = ({ sidenav }: { sidenav: ResultType }) => {
  return (
    <aside className="sticky block top-14 z-30 h-[calc(100vh-3.5rem)] w-[240px]">
      <div className="flex flex-col w-full h-full py-6 box-border">
        <div className="flex-1 p-4 bg-muted overflow-hidden rounded-md">
          <div className="h-full overflow-auto">
            {Object.values(sidenav).map((domainInfo) => (
              <Collapsible key={domainInfo.domainId}>
                <SidenavTree
                  parentName={domainInfo.domainName}
                  childItems={Object.values(
                    domainInfo.childIndustryClass || {}
                  )}
                />
              </Collapsible>
            ))}
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidenav;
