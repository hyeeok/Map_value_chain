'use client';

import { useAtom } from 'jotai';
import React, { useEffect, useState } from 'react';
import { Edge, Node } from 'reactflow';

import Flow from '@/components/feature/reactflow/flow';
import { Switch } from '@/components/ui/switch';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { showThemeAtom } from '@/lib/atoms/base';

interface FlowmapProps {
  nodes: Node[];
  edges: Edge[];
}

const Flowmap = ({ nodes, edges }: FlowmapProps) => {
  const [nodeData, setNodeData] = useState<Node[]>(nodes);
  const [edgeData, setEdgeData] = useState<Edge[]>(edges);
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
          <div className="flex items-center">
            <Switch checked={showTheme} onCheckedChange={toggleShowSidebar} />
            <span className="text-sm ml-2">Show themes</span>
          </div>
        </div>
        <TabsContent value="map" className="h-[90%] border rounded-md">
          <Flow initialNodes={nodeData} initialEdges={edgeData} />
        </TabsContent>
        <TabsContent value="list"></TabsContent>
      </Tabs>
    </>
  );
};

export default Flowmap;
