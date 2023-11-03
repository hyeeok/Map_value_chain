import React from 'react';

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

const SideNav = () => {
  return (
    <aside className="w-[240px]">
      <Tabs
        defaultValue="typeOne"
        className="w-full h-[calc(100vh-3.5rem)] py-4 box-border"
      >
        <TabsList className="grid w-full grid-cols-2">
          <TabsTrigger value="typeOne">전체산업</TabsTrigger>
          <TabsTrigger value="typeTwo">산업별</TabsTrigger>
        </TabsList>
        <div className="p-4 bg-muted h-[calc(100vh-8rem)] overflow-hidden mt-4 rounded-md">
          <TabsContent value="typeOne">
            <Collapsible>
              <CollapsibleTrigger>
                <div>
                  <span>도메인</span>
                </div>
              </CollapsibleTrigger>
              <CollapsibleContent>
                <ul>
                  <li className="pl-4">
                    <Collapsible>
                      <CollapsibleTrigger>
                        <div>
                          <span>산업</span>
                        </div>
                      </CollapsibleTrigger>
                      <CollapsibleContent>
                        <ul>
                          <li className="pl-4">산업</li>
                        </ul>
                      </CollapsibleContent>
                    </Collapsible>
                  </li>
                </ul>
              </CollapsibleContent>
            </Collapsible>
          </TabsContent>
          <TabsContent value="typeTwo" className="p-4"></TabsContent>
        </div>
      </Tabs>
    </aside>
  );
};

export default SideNav;
