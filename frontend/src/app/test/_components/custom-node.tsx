'use client';

import React from 'react';
import { Handle, NodeResizer, Position } from 'reactflow';

import { mvc } from '@/app/test/_components/const';

import styles from './custom-node.module.css';

interface CustomNodeProps {
  data: { label: string };
  selected: boolean;
}

const CustomNode = ({ data, selected }: CustomNodeProps) => {
  const mvcObj = mvc.find((item) => item.category === data.label);
  console.log(mvcObj);
  const color = mvcObj ? mvcObj.color : 1;

  return (
    <div className={`${styles.bg} ${styles[`color-${color}`]}`}>
      <NodeResizer isVisible={selected} minWidth={100} minHeight={30} />
      <Handle type="target" position={Position.Top} id="top" />
      <Handle type="target" position={Position.Right} id="right" />
      <Handle type="target" position={Position.Left} id="left" />
      <Handle type="target" position={Position.Bottom} id="bottom" />
      <div className={styles.container}>
        <label>{data.label}</label>
        <div className={`nowheel ${styles.content}`}>
          <div className={styles.domain}>
            {mvcObj?.domains?.map((domain, i) => (
              <a key={i} href="#">
                <div>{domain.label}</div>
              </a>
            ))}
          </div>
          <div className={styles.theme}>
            {mvcObj?.themes?.map((theme, i) => (
              <div key={i}>{theme.label}</div>
            ))}
          </div>
        </div>
      </div>
      <Handle type="source" position={Position.Top} id="top" />
      <Handle type="source" position={Position.Right} id="right" />
      <Handle type="source" position={Position.Left} id="left" />
      <Handle type="source" position={Position.Bottom} id="bottom" />
    </div>
  );
};

export default CustomNode;
