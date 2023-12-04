import { cookies } from 'next/headers';
import React from 'react';

import { baseUrl } from '@/api/api-client';
import Flowmap from '@/app/flowmap/_components/flowmap';

const getFlowmap = async () => {
  const cookieStore = cookies();
  try {
    const response = await fetch(`${baseUrl}/flowmap`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
};

const getIndustryClassList = async () => {
  const cookieStore = cookies();
  try {
    const response = await fetch(`${baseUrl}/flowmap/industry-classes`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
};

const FlowmapPage = async () => {
  const flowmapData = await getFlowmap();
  // const flowmapData = { node: initialNodes, edge: initialEdges };
  const industryClassListData = await getIndustryClassList();

  return (
    <div className="h-[calc(100vh-45px)] flex flex-col">
      <section className="container">
        <div className=" flex max-w-[980px] flex-col items-start gap-2 pt-8 md:pt-12 page-header pb-8">
          <h2 className="text-3xl font-bold tracking-tight">Value Chain Map</h2>
        </div>
      </section>

      <section className="flex-1">
        {flowmapData && industryClassListData ? (
          <Flowmap
            nodes={flowmapData.node}
            edges={flowmapData.edge}
            industryClassListData={industryClassListData}
          />
        ) : (
          <div className="container">No data found.</div>
        )}
      </section>
    </div>
  );
};

export default FlowmapPage;
