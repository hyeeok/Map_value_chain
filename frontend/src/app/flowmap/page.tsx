'use client';

import { useAtom } from 'jotai';
import React, { useState } from 'react';

import { initialEdges, initialNodes } from '@/app/flowmap/test';
import Flow from '@/components/feature/reactflow/flow';
import { Switch } from '@/components/ui/switch';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { showThemeAtom } from '@/lib/atoms/base';

const testFlowmapData = { node: initialNodes, edge: initialEdges };

const FlowmapPage = () => {
  const [flowmapData, setFlowmapData] = useState(testFlowmapData);
  const [showTheme, setShowTheme] = useAtom(showThemeAtom);
  const toggleShowSidebar = () => {
    setShowTheme(!showTheme);
  };

  return (
    <div className="container h-full flex flex-col">
      <section>
        <h2>flowmap</h2>
      </section>

      <section className="flex-1">
        <Tabs defaultValue="map" className="h-full">
          <TabsList>
            <TabsTrigger value="map">Map</TabsTrigger>
            <TabsTrigger value="list">List</TabsTrigger>
          </TabsList>
          <Switch checked={showTheme} onCheckedChange={toggleShowSidebar} />
          <TabsContent value="map" className="h-full">
            {flowmapData ? (
              <Flow
                initialNodes={flowmapData.node}
                initialEdges={flowmapData.edge}
              />
            ) : (
              <span>No data.</span>
            )}
          </TabsContent>
          <TabsContent value="list"></TabsContent>
        </Tabs>
      </section>
    </div>
  );
};

export default FlowmapPage;
