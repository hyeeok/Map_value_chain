import { ChevronsUpDown } from 'lucide-react';
import React from 'react';

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

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
interface SidenavProps {
  domainTab: Domain[];
  industryTab: Industry[];
}

const Sidenav = ({ sidenav }: { sidenav: SidenavProps }) => {
  return (
    <aside className="sticky block top-14 z-30 h-[calc(100vh-3.5rem)] w-[240px]">
      <Tabs
        defaultValue="typeOne"
        className="flex flex-col w-full h-full py-6 box-border"
      >
        <TabsList className="grid w-full grid-cols-2">
          <TabsTrigger value="typeOne">전체산업</TabsTrigger>
          <TabsTrigger value="typeTwo">산업별</TabsTrigger>
        </TabsList>
        <div className="flex-1 p-4 bg-muted overflow-hidden mt-4 rounded-md">
          <TabsContent value="typeOne">
            {sidenav.domainTab.map((domain, i) => (
              <Collapsible key={i}>
                <CollapsibleTrigger className="w-full text-left">
                  <div className="flex justify-between items-center h-9 rounded-md px-3 py-2">
                    <span className="text-sm">{domain.domainName}</span>
                    <ChevronsUpDown className="h-3 w-3 text-muted-foreground" />
                  </div>
                </CollapsibleTrigger>
                <CollapsibleContent>
                  <ul className="pl-4">
                    {domain.industryList.map((industry, j) => (
                      <li key={j}>
                        <Collapsible>
                          <CollapsibleTrigger className="w-full text-left">
                            <div className="flex justify-between items-center h-9 rounded-md px-3 py-2">
                              <span className="text-sm">
                                {industry.industryName}
                              </span>
                              <ChevronsUpDown className="h-3 w-3 text-muted-foreground" />
                            </div>
                          </CollapsibleTrigger>
                          <CollapsibleContent>
                            <ul className="pl-4">
                              <li>
                                <div className="flex justify-between items-center h-9 rounded-md px-3 py-2">
                                  <span className="text-sm">대분류..</span>
                                  <ChevronsUpDown className="h-3 w-3 text-muted-foreground" />
                                </div>
                              </li>
                            </ul>
                          </CollapsibleContent>
                        </Collapsible>
                      </li>
                    ))}
                  </ul>
                </CollapsibleContent>
              </Collapsible>
            ))}
          </TabsContent>
          <TabsContent value="typeTwo" className="p-4"></TabsContent>
        </div>
      </Tabs>
    </aside>
  );
};

export default Sidenav;
