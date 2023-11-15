import { ChevronsUpDown } from 'lucide-react';
import React from 'react';

import { Button } from '@/components/ui/button';
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible';

interface Domain {
  domainName: string;
  industryList: { industryName: string }[];
}
interface Industry {
  mainCategoryName: string;
  middleCategoryList: {
    middleCategoryName: string;
    smallCategoryList: { smallCategoryName: string }[];
  }[];
}
interface SidenavProps {}
interface CollapsibleListProps {
  parentName: string;
  children?: React.ReactNode;
}

const CollapsibleList = ({ parentName, children }: CollapsibleListProps) => {
  return (
    <Collapsible>
      <div className="flex items-center">
        <CollapsibleTrigger asChild>
          <Button variant="ghost" size="sm" className="w-9 p-0">
            <ChevronsUpDown className="h-3 w-3 text-muted-foreground" />
          </Button>
        </CollapsibleTrigger>
        <span className="text-sm">{parentName}</span>
      </div>
      <CollapsibleContent>
        <ul className="pl-4">{children}</ul>
      </CollapsibleContent>
    </Collapsible>
  );
};

const Sidenav = ({ sidenav }: { sidenav: SidenavProps }) => {
  return (
    <aside className="sticky block top-14 z-30 h-[calc(100vh-3.5rem)] w-[240px]">
      <div
        defaultValue="typeOne"
        className="flex flex-col w-full h-full py-6 box-border"
      >
        <div className="flex-1 p-4 bg-muted overflow-hidden rounded-md">
          {sidenav.domainTab.map((domain, i) => (
            <CollapsibleList key={i} parentName={domain.domainName}>
              {domain.industryList.map((industry, j) => (
                <li key={j}>
                  <CollapsibleList parentName={industry.industryName}>
                    <CollapsibleList parentName={industry.industryName} />
                  </CollapsibleList>
                </li>
              ))}
            </CollapsibleList>
          ))}
        </div>
      </div>
    </aside>
  );
};

export default Sidenav;
