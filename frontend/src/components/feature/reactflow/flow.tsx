'use client';

import 'reactflow/dist/style.css';

import React, { useCallback, useRef, useState } from 'react';
import ReactFlow, {
  addEdge,
  Connection,
  Edge,
  Node,
  OnConnect,
  Panel,
  ReactFlowInstance,
  ReactFlowProvider,
  updateEdge,
  useEdgesState,
  useNodesState,
} from 'reactflow';

import CustomNode from '@/components/feature/reactflow/custom-node';
import { Button } from '@/components/ui/button';

interface FlowProps {
  initialEdges: Edge[];
  initialNodes: Node[];
}

const flowKey = 'flowmap';

const nodeTypes = { custom: CustomNode };

const Flow = ({ initialNodes, initialEdges }: FlowProps) => {
  const edgeUpdateSuccessful = useRef(true);
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const [rfInstance, setRfInstance] = useState<ReactFlowInstance | null>(null);

  const onConnect: OnConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  const onSave = useCallback(() => {
    console.log('click');
    if (rfInstance) {
      const flow = rfInstance.toObject();
      console.log(JSON.stringify(flow));
      localStorage.setItem(flowKey, JSON.stringify(flow));
    }
  }, [rfInstance]);

  const onEdgeUpdateStart = useCallback(() => {
    edgeUpdateSuccessful.current = false;
  }, []);

  const onEdgeUpdate = useCallback(
    (oldEdge: Edge, newConnection: Connection) => {
      edgeUpdateSuccessful.current = true;
      setEdges((els) => updateEdge(oldEdge, newConnection, els));
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    []
  );

  const onEdgeUpdateEnd = useCallback((_: any, edge: Edge) => {
    if (!edgeUpdateSuccessful.current) {
      setEdges((eds) => eds.filter((e) => e.id !== edge.id));
    }

    edgeUpdateSuccessful.current = true;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <ReactFlowProvider>
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
        onInit={setRfInstance}
        fitView
      >
        <Panel position="top-right">
          <Button onClick={onSave} size="sm">
            Save
          </Button>
        </Panel>
      </ReactFlow>
    </ReactFlowProvider>
  );
};

export default Flow;
