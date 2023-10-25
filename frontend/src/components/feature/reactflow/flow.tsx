'use client';

import 'reactflow/dist/style.css';

import React, { useCallback, useRef, useState } from 'react';
import ReactFlow, {
  addEdge,
  OnConnect,
  updateEdge,
  useEdgesState,
  useNodesState,
} from 'reactflow';

import CustomNode from '@/components/feature/reactflow/custom-node';

interface FlowProps {
  initialEdges?: object[];
  initialNodes?: object[];
}

const nodeTypes = { custom: CustomNode };

const Flow = ({ initialNodes, initialEdges }: FlowProps) => {
  const edgeUpdateSuccessful = useRef(true);
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const [nodeColor, setNodeColor] = useState('#fff');

  const onConnect: OnConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  const onEdgeUpdateStart = useCallback(() => {
    edgeUpdateSuccessful.current = false;
  }, []);

  const onEdgeUpdate = useCallback((oldEdge, newConnection) => {
    edgeUpdateSuccessful.current = true;
    setEdges((els) => updateEdge(oldEdge, newConnection, els));
  }, []);

  const onEdgeUpdateEnd = useCallback((_, edge) => {
    if (!edgeUpdateSuccessful.current) {
      setEdges((eds) => eds.filter((e) => e.id !== edge.id));
    }

    edgeUpdateSuccessful.current = true;
  }, []);

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      nodeTypes={nodeTypes}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      snapToGrid
      onEdgeUpdate={onEdgeUpdate}
      onEdgeUpdateStart={onEdgeUpdateStart}
      onEdgeUpdateEnd={onEdgeUpdateEnd}
      onConnect={onConnect}
      fitView
    />
  );
};

export default Flow;
