'use client';

import cytoscape, { ElementDefinition } from 'cytoscape';
import klay from 'cytoscape-klay';
import React, { useState } from 'react';
import CytoscapeComponent from 'react-cytoscapejs';

import { getOverviewRelation } from '@/api/overview/api';

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

const formatCyElements = (data: OverviewRelationType[]) => {
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
  return elements;
};

const RelationSection = ({
  data,
  corpCode,
}: {
  data: OverviewRelationType[];
  corpCode: string;
}) => {
  const [cyCorpCode, setCyCorpCode] = useState(corpCode);
  const [cyElements, setCyElements] = useState(formatCyElements(data));

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

  const handleClick = (event: cytoscape.EventObject) => {
    const clickedId = event?.target._private.data.id;
    getOverviewRelation(clickedId)
      .then((response) => {
        if (response.data.length > 0) {
          const cyElements = formatCyElements(response.data);
          setCyElements(cyElements);
        }
      })
      .catch((error) => console.log(error))
      .finally(() => setCyCorpCode(clickedId));
  };

  return (
    <section>
      <h3 className="scroll-m-20 text-lg font-bold tracking-tight">
        주요 거래처
      </h3>
      <div className="rounded-md mt-2">
        <CytoscapeComponent
          key={cyCorpCode}
          elements={cyElements}
          layout={layout}
          style={{ width: 'w-full', height: '480px' }}
          stylesheet={cyStyleSheet}
          wheelSensitivity={0.1}
          cy={(cy) => {
            cy.on('tap', 'node', (event) => {
              handleClick(event);
            });
          }}
        />
      </div>
    </section>
  );
};

export default RelationSection;
