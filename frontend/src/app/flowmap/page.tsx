import React from 'react';

import { getFlowmap } from '@/api/flowmap/api';
import Flowmap from '@/app/flowmap/_components/flowmap';

const FlowmapPage = async () => {
  const data = await getFlowmap();

  return (
    <div className="container h-full flex flex-col">
      <section>
        <h2>flowmap</h2>
      </section>

      <section className="flex-1">
        <Flowmap nodes={data.node} edges={data.edge} />
      </section>
    </div>
  );
};

export default FlowmapPage;
