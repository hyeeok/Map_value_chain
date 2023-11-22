'use client';

import { ChevronDown, ChevronRight } from 'lucide-react';
import React from 'react';

import {
  IndustryClassInfo,
  isIndustryClassInfo,
  isSubClassInfo,
  SubClassInfo,
} from '@/app/overview/_lib/sidenav-lib';
import { Button } from '@/components/ui/button';
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible';

interface TreeViewProps {
  parentName: string;
  childItems?: (IndustryClassInfo | SubClassInfo)[];
}

const SidenavTree = ({ parentName, childItems }: TreeViewProps) => {
  if (!childItems) return null;

  return (
    <Collapsible>
      <div className="flex items-center">
        <CollapsibleTrigger asChild className="group">
          <Button
            variant="ghost"
            size="xs"
            className={`w-6  min-w-6 p-0 ${!childItems?.length && 'invisible'}`}
          >
            <ChevronRight className="h-3 w-3 text-muted-foreground group-data-[state=open]:hidden" />
            <ChevronDown className="h-3 w-3 text-muted-foreground group-data-[state=closed]:hidden" />
          </Button>
        </CollapsibleTrigger>
        <span className="text-xs whitespace-nowrap">{parentName}</span>
      </div>
      <CollapsibleContent>
        <ul className="pl-4">
          {childItems?.map((item, i) => (
            <li key={i}>
              {isIndustryClassInfo(item) && (
                <SidenavTree
                  parentName={item.industryClassName}
                  childItems={Object.values(item.childClass || {})}
                />
              )}
              {isSubClassInfo(item) && (
                <SidenavTree
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

export default SidenavTree;
