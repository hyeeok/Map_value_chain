'use client';

import { useAtom } from 'jotai';
import React, { useEffect, useState } from 'react';

import Flow from '@/components/feature/reactflow/flow';
import { Switch } from '@/components/ui/switch';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { showThemeAtom } from '@/lib/atoms/base';

interface FlowmapProps {
  nodes: object[];
  edges: object[];
}

const Flowmap = ({ nodes, edges }: FlowmapProps) => {
  console.log(nodes, edges);
  const [nodeData, setNodeData] = useState<object[]>(nodes);
  const [edgeData, setEdgeData] = useState<object[]>(edges);
  const [showTheme, setShowTheme] = useAtom(showThemeAtom);

  useEffect(() => {
    setNodeData(nodes);
  }, [nodes]);

  useEffect(() => {
    setEdgeData(edges);
  }, [edges]);

  const toggleShowSidebar = () => {
    setShowTheme(!showTheme);
  };

  return (
    <>
      <Tabs defaultValue="map" className="h-full">
        <div className="flex gap-4 items-center">
          <TabsList>
            <TabsTrigger value="map">Map</TabsTrigger>
            <TabsTrigger value="list">List</TabsTrigger>
          </TabsList>
          <div>
            <Switch checked={showTheme} onCheckedChange={toggleShowSidebar} />{' '}
            Show themes
          </div>
        </div>
        <TabsContent value="map" className="h-full">
          <Flow initialNodes={nodeData} initialEdges={edgeData} />
        </TabsContent>
        <TabsContent value="list"></TabsContent>
      </Tabs>
    </>
  );
};

export default Flowmap;
