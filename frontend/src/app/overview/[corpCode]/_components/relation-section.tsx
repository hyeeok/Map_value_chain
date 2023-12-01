'use client';

import cytoscape, { ElementDefinition } from 'cytoscape';
import klay from 'cytoscape-klay';
import React from 'react';
import CytoscapeComponent from 'react-cytoscapejs';

interface OverviewRelationType {
  id: number;
  industryClass: string;
  corpName: string;
  corpCode: string;
  vendorCorpName: string;
  vendorCorpCode: string;
  vendorClass: string;
  updateDate: string;
}

const RelationSection = ({ data }: { data: OverviewRelationType[] }) => {
  console.log(data);
  let elements: ElementDefinition[] = [];
  data.map((item: OverviewRelationType) => {
    elements.push({
      data: {
        id: item.corpCode,
        label: item.corpName,
      },
    });
    elements.push({
      data: {
        id: item.vendorCorpCode,
        label: item.vendorCorpName,
      },
    });
    if (item.vendorClass === '구매') {
      elements.push({
        data: {
          source: item.corpCode,
          target: item.vendorCorpCode,
        },
      });
    } else if (item.vendorClass === '판매') {
      elements.push({
        data: {
          source: item.vendorCorpCode,
          target: item.corpCode,
        },
      });
    }
  });
  cytoscape.use(klay);
  const layout = { name: 'klay' };
  const cyStyleSheet = [
    {
      selector: 'node',
      style: {
        label: 'data(label)',
        backgroundColor: '#dde0e4',
        fontSize: '0.5em',
      },
    },

    {
      selector: 'edge',
      style: {
        curveStyle: 'bezier',
        targetArrowShape: 'triangle',
        lineColor: '#7d7d7e',
        targetArrowColor: '#7d7d7e',
        opacity: 0.5,
      },
    },
  ];

  return (
    <section>
      <h3 className="scroll-m-20 text-lg font-bold tracking-tight">
        주요 거래처
      </h3>
      <div className="rounded-md mt-2">
        <CytoscapeComponent
          elements={elements}
          layout={layout}
          style={{ width: 'w-full', height: '480px' }}
          stylesheet={cyStyleSheet}
          wheelSensitivity={0.1}
        />
      </div>
    </section>
  );
};

export default RelationSection;
