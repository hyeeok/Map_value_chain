'use client';

import { ChevronsUpDown } from 'lucide-react';
import React from 'react';

import {
  IndustryClassInfo,
  ResultType,
  SubClassInfo,
} from '@/app/search/_lib/sidenav-lib';
import { Button } from '@/components/ui/button';
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible';

interface CollapsibleListProps {
  parentName: string;
  childItems?: (IndustryClassInfo | SubClassInfo)[];
}

const isIndustryClassInfo = (item: any): item is IndustryClassInfo => {
  return (item as IndustryClassInfo).industryClassCode !== undefined;
};
const isSubClassInfo = (item: any): item is SubClassInfo => {
  return (item as SubClassInfo).subClassCode !== undefined;
};

const CollapsibleList = ({ parentName, childItems }: CollapsibleListProps) => {
  if (!childItems) return null;

  return (
    <Collapsible>
      <div className="flex items-center">
        <CollapsibleTrigger asChild>
          <Button
            variant="ghost"
            size="sm"
            className={`w-9  min-w-[36px] p-0 ${
              !childItems?.length && 'invisible'
            }`}
          >
            <ChevronsUpDown className="h-3 w-3 text-muted-foreground" />
          </Button>
        </CollapsibleTrigger>
        <span className="text-xs whitespace-nowrap">{parentName}</span>
      </div>
      <CollapsibleContent>
        <ul className="pl-4">
          {childItems?.map((item, i) => (
            <li key={i}>
              {isIndustryClassInfo(item) && (
                <CollapsibleList
                  parentName={item.industryClassName}
                  childItems={Object.values(item.childClass || {})}
                />
              )}
              {isSubClassInfo(item) && (
                <CollapsibleList
                  parentName={item.subClassName}
                  childItems={Object.values(item.childClass || {})}
                />
              )}
            </li>
          ))}
        </ul>
      </CollapsibleContent>
    </Collapsible>
  );
};

const Sidenav = ({ sidenav }: { sidenav: ResultType }) => {
  console.log(sidenav);
  return (
    <aside className="sticky block top-14 z-30 h-[calc(100vh-3.5rem)] w-[240px]">
      <div className="flex flex-col w-full h-full py-6 box-border">
        <div className="flex-1 p-4 bg-muted overflow-hidden rounded-md">
          <div className="h-full overflow-auto">
            {Object.values(sidenav).map((domainInfo) => (
              <Collapsible key={domainInfo.domainId}>
                <CollapsibleList
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
