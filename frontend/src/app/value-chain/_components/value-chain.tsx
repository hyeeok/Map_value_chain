'use client';

import { useAtom } from 'jotai';
import React from 'react';

import ValueChainMap from '@/app/value-chain/_components/value-chain-map';
import { IndustryType } from '@/app/value-chain/_lib/format-operations';
import { Switch } from '@/components/ui/switch';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { showThemeAtom } from '@/lib/atoms/base';

const ValueChain = ({
  data,
}: {
  data: { length: number; data: IndustryType[] };
}) => {
  const [showTheme, setShowTheme] = useAtom(showThemeAtom);
  const toggleShowTheme = () => {
    setShowTheme(!showTheme);
  };

  return (
    <Tabs defaultValue="map" className="h-full overflow-x-hidden py-4">
      <div className="container flex gap-4 items-center mb-4">
        <TabsList>
          <TabsTrigger value="map">Map</TabsTrigger>
          <TabsTrigger value="list">List</TabsTrigger>
        </TabsList>
        <div className="flex items-center">
          <Switch checked={showTheme} onCheckedChange={toggleShowTheme} />
          <span className="text-sm ml-2">Show themes</span>
        </div>
      </div>
      <TabsContent
        value="map"
        className="h-[90%] md:w-screen md:mx-[calc(50%-50vw)]"
      >
        <div className="h-full w-full rounded-md md:rounded-none">
          <ValueChainMap data={data.data} />
        </div>
      </TabsContent>
      <TabsContent value="list" className="container h-[68vh] overflow-y-auto">
        {/* <DomainList industryClassListData={data} /> */}
      </TabsContent>
    </Tabs>
  );
};

export default ValueChain;
