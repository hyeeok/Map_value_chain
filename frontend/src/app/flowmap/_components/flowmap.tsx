'use client';

import { useAtom } from 'jotai';
import React, { useEffect, useState } from 'react';
import { Edge, Node } from 'reactflow';

import DomainList, {
  IndustryClass,
} from '@/app/flowmap/_components/industry-class-list';
import Flow from '@/components/feature/reactflow/flow';
import { Switch } from '@/components/ui/switch';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { showThemeAtom } from '@/lib/atoms/base';

interface FlowmapProps {
  nodes: Node[];
  edges: Edge[];
  industryClassListData: {
    length: number;
    data: IndustryClass[];
  };
}

const Flowmap = ({ nodes, edges, industryClassListData }: FlowmapProps) => {
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
      <Tabs defaultValue="map" className="h-full overflow-x-hidden pb-6">
        <div className="container flex gap-4 items-center mb-6">
          <TabsList>
            <TabsTrigger value="map">Map</TabsTrigger>
            <TabsTrigger value="list">List</TabsTrigger>
          </TabsList>
          <div className="flex items-center">
            <Switch checked={showTheme} onCheckedChange={toggleShowSidebar} />
            <span className="text-sm ml-2">Show themes</span>
          </div>
        </div>
        <TabsContent
          value="map"
          className="h-[90%] md:w-screen md:mx-[calc(50%-50vw)]"
        >
          <div className="h-full w-full border rounded-md md:rounded-none bg-muted">
            <Flow initialNodes={nodeData} initialEdges={edgeData} />
          </div>
        </TabsContent>
        <TabsContent
          value="list"
          className="container h-[68vh] overflow-y-auto"
        >
          <DomainList industryClassListData={industryClassListData} />
        </TabsContent>
      </Tabs>
    </>
  );
};

export default Flowmap;
