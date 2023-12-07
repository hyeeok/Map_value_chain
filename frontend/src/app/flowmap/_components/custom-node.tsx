'use client';

import { useAtomValue } from 'jotai';
import React from 'react';
import {
  Handle,
  NodeResizer,
  Position,
  useReactFlow,
  useStoreApi,
} from 'reactflow';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { showThemeAtom } from '@/lib/atoms/base';

interface IndustryClass {
  industryClassCode: string;
  industryClassName: string;
  industryClassType: string;
}

interface CustomNodeProps {
  id: string;
  data: {
    domainCode: string;
    domainName: string;
    classes: IndustryClass[];
    themes: IndustryClass[];
    contents: object[];
    color: string;
  };
  selected: boolean;
}
// 개별 industryClass 내용은 우선 contents에 저장 예정?

const CustomNode = ({ id, data, selected }: CustomNodeProps) => {
  const showTheme = useAtomValue(showThemeAtom);
  const { setNodes } = useReactFlow();
  const store = useStoreApi();

  const updateNodeColor = (nodeId: string, color: string) => {
    const { nodeInternals } = store.getState();
    setNodes(
      Array.from(nodeInternals.values()).map((node) => {
        if (node.id === nodeId) {
          node.data = {
            ...node.data,
          };
        }
        return node;
      })
    );
    data = {
      ...data,
      color: color,
    };
  };

  return (
    <div className="h-full">
      <NodeResizer isVisible={selected} minWidth={100} minHeight={30} />
      <Handle type="target" position={Position.Top} id="top" />
      <Handle type="target" position={Position.Right} id="right" />
      <Handle type="target" position={Position.Left} id="left" />
      <Handle type="target" position={Position.Bottom} id="bottom" />
      <Card
        className={`h-full box-border`}
        style={{ backgroundColor: data.color }}
      >
        <CardHeader className="w-full h-[64px]">
          <CardTitle className="inline-block flex justify-between text-primary-foreground">
            <span>{data.domainName}</span>
            <input
              className="nodrag h-full inline-flex ml-auto overflow-hidden"
              type="color"
              onChange={(event) => updateNodeColor(id, event.target.value)}
            />
          </CardTitle>
        </CardHeader>
        <CardContent className="overflow-y-auto h-[calc(100%-64px)] nowheel">
          <div>
            <p className="text-sm font-medium leading-none mb-2 text-primary-foreground">
              Classes
            </p>
            <div className="flex flex-wrap gap-2">
              {data.classes.map((classItem, i) => (
                <>
                  <div
                    key={i}
                    className="
                      inline-flex items-center justify-center whitespace-nowrap
                      rounded-md text-sm font-medium h-9 px-4 py-2
                      bg-primary text-primary-foreground
                    "
                  >
                    {classItem.industryClassName}
                  </div>
                  {/* <Button asChild key={i}>
                    <Link href="#">{classItem.industryClassName}</Link>
                  </Button> */}
                </>
              ))}
            </div>
          </div>
          {showTheme && (
            <div className="pt-4">
              <p className="text-sm font-medium leading-none mb-2 text-primary-foreground">
                Themes
              </p>
              <div className="flex flex-wrap gap-2">
                {data.themes.map((themeItem, i) => (
                  <div
                    key={i}
                    className="
                      inline-flex items-center justify-center whitespace-nowrap
                      rounded-md text-sm font-medium h-9 px-4 py-2
                      bg-secondary text-secondary-foreground
                    "
                  >
                    {themeItem.industryClassName}
                  </div>
                ))}
              </div>
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
