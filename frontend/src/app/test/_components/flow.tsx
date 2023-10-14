'use client';
import 'reactflow/dist/style.css';

import React from 'react';
import ReactFlow from 'reactflow';

import { edges, nodes } from '@/app/test/_components/const';
import CustomNode from '@/app/test/_components/custom-node';

const nodeTypes = { custom: CustomNode };

const Flow = () => {
  return (
    <ReactFlow nodes={nodes} edges={edges} nodeTypes={nodeTypes} fitView />
  );
};

export default Flow;
