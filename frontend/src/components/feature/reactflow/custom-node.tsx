'use client';

import { useAtomValue } from 'jotai';
import React from 'react';
import { Handle, NodeResizer, Position } from 'reactflow';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { showThemeAtom } from '@/lib/atoms/base';

interface IndustryClass {
  industryClassId: number;
  industryClassCode: number;
  industryClassName: string;
}

interface CustomNodeProps {
  data: {
    domainId: number;
    domainCode: number;
    domainName: string;
    color: number;
    classes: IndustryClass[];
    themes: IndustryClass[];
    contents: object[];
  };
  selected: boolean;
}
// 개별 industryClass 내용은 우선 contents에 저장 예정?

const CustomNode = ({ data, selected }: CustomNodeProps) => {
  const showTheme = useAtomValue(showThemeAtom);

  return (
    <div className="h-full">
      <NodeResizer isVisible={selected} minWidth={100} minHeight={30} />
      <Handle type="target" position={Position.Top} id="top" />
      <Handle type="target" position={Position.Right} id="right" />
      <Handle type="target" position={Position.Left} id="left" />
      <Handle type="target" position={Position.Bottom} id="bottom" />
      <Card className="h-full">
        <CardHeader>
          <CardTitle>{data.domainName}</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex flex-wrap">
            {data.classes.map((industryClass, i) => (
              <a key={i} href="#">
                <div>{industryClass.industryClassName}</div>
              </a>
            ))}
          </div>
          {showTheme && (
            <div>
              {data.themes.map((industryClass, i) => (
                <div key={i}>{industryClass.industryClassName}</div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
      <Handle type="source" position={Position.Top} id="top" />
      <Handle type="source" position={Position.Right} id="right" />
      <Handle type="source" position={Position.Left} id="left" />
      <Handle type="source" position={Position.Bottom} id="bottom" />
    </div>
  );
};

export default CustomNode;
