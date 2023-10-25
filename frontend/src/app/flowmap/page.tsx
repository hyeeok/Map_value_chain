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
    throw error;
  }
};

const FlowmapPage = async () => {
  const data = await getFlowmap();

  return (
    <div className="container h-full flex flex-col">
      <section className="flex max-w-[980px] flex-col items-start gap-2 pt-8 md:pt-12 page-header pb-8">
        <h2 className="text-3xl font-bold tracking-tight">Value Chain Map</h2>
      </section>

      <section className="flex-1 w-full">
        {data ? (
          <Flowmap nodes={data.node} edges={data.edge} />
        ) : (
          <div>No data found.</div>
        )}
      </section>
    </div>
  );
};

export default FlowmapPage;
